import cmd
from shlex import *
import pynames
import pkgutil
import sys

if sys.platform.startswith('linux'):
    import readline
elif sys.platform.startswith('win'):
    import pyreadline3


class NamesCmd(cmd.Cmd):
    intro = "Welcome to python names generator. Type 'help' for quick start"
    prompt = '=>'
    possible_info_subs = ['male', 'female', 'language']
    possible_gender = ['male', 'female']
    gen_language = pynames.LANGUAGE.NATIVE

    if (True):
        available_gens = [module_name for _, module_name, _ in
                          pkgutil.iter_modules([pynames.generators.generators_root])]
        available_sub_gens = {
            gen_name: {subgen_name.replace('FullnameGenerator', '').replace('NamesGenerator', ''): gen
                       for subgen_name, gen in pynames.generators.__dict__[gen_name].__dict__.items()
                       if (subgen_name.endswith('FullnameGenerator') or subgen_name.endswith('NamesGenerator'))}
            for gen_name in available_gens
        }

    available_gens = dict(map(lambda x: x if len(x[1]) == 1 else (x[0], {}), available_sub_gens.items()))
    available_sub_gens = dict(map(lambda x: x if len(x[1]) > 1 else (x[0], {}), available_sub_gens.items()))

    def do_language(self, arg):
        """Set language"""
        arg = split(arg)
        if len(arg) != 1:
            print(f'Too {"many" if len(arg) > 1 else "few"} arguments')
        elif arg[0] not in pynames.LANGUAGE.ALL:
            print(f'Wrong language arguments. Possible are {", ".join(pynames.LANGUAGE.ALL)}')
        else:
            self.gen_language = arg[0]

    def do_generate(self, arg):
        """Generate few world"""
        args = split(arg)
        command = args[-1] if len(args) > 0 and args[-1] in self.possible_gender else 'gen'
        generator = args if command == 'count' else args[:-1]

        gen_class = None
        if len(generator) < 1 or len(generator) > 2:
            print(f'Too {"many" if len(generator) > 2 else "few"} generator arguments')
        elif len(generator) == 1:
            if generator[0] not in self.available_gens:
                print('Generator not found')
            else:
                if len(self.available_gens[generator[0]]) == 0:
                    gen_class = self.available_sub_gens[generator[0]]
                else:
                    gen_class = self.available_gens[generator[0]]
                gen_class = [*gen_class.values()][0]
        else:  # len(generator) == 2
            if generator[0] not in self.available_sub_gens:
                print('Generator not found')
            elif generator[1] not in self.available_sub_gens[generator[0]]:
                print('Sub generator not found')
            else:
                gen_class = self.available_sub_gens[generator[0]][generator[1]]
        cur_language = self.gen_language if self.gen_language in gen_class.language else pynames.LANGUAGE.NATIVE
        if command == 'gen' or command == 'male':
            print(gen_class().get_name_simple(language=cur_language))
        elif command == 'female':
            print(gen_class().get_name_simple(pynames.GENDER.FEMALE, language=cur_language))

    def do_info(self, arg):
        """Get some info about generator"""
        args = split(arg)
        command = args[-1] if len(args) > 0 and args[-1] in self.possible_info_subs else 'count'
        generator = args if command == 'count' else args[:-1]

        gen_class = None
        if len(generator) < 1 or len(generator) > 2:
            print(f'Too {"many" if len(generator) > 2 else "few"} generator arguments')
        elif len(generator) == 1:
            if generator[0] not in self.available_gens:
                print('Generator not found')
            else:
                if len(self.available_gens[generator[0]]) == 0:
                    gen_class = self.available_sub_gens[generator[0]]
                else:
                    gen_class = self.available_gens[generator[0]]
                gen_class = [*gen_class.values()][0]
        else:  # len(generator) == 2
            if generator[0] not in self.available_sub_gens:
                print('Generator not found')
            elif generator[1] not in self.available_sub_gens[generator[0]]:
                print('Sub generator not found')
            else:
                gen_class = self.available_sub_gens[generator[0]][generator[1]]
        if command == 'count':
            print(gen_class().get_names_number())
        elif command == 'male':
            print(gen_class().get_names_number(pynames.GENDER.MALE))
        elif command == 'female':
            print(gen_class().get_names_number(pynames.GENDER.FEMALE))
        elif command == 'language':
            print(', '.join(gen_class().languages))

    def do_exit(self, arg):
        """Stop"""
        return True

    def do_EOF(self, arg):
        self.do_exit(arg)
        return True

    def complete_language(self, text: str, line: str, begidx, endidx):
        arg_count = len(split(line))
        if arg_count == 1 or len(split(line)) == 2 and text != '':
            return list(filter(lambda x: x.startswith(text), pynames.LANGUAGE.ALL))
        else:
            return []

    def complete_generate(self, text: str, line: str, begidx, endidx):
        args = split(line)
        arg_count = len(args)
        if arg_count == 1 or len(split(line)) == 2 and text != '':
            return list(filter(lambda x: x.startswith(text), self.available_gens))
        if arg_count == 2 or len(split(line)) == 3 and text != '':
            if args[1] in self.available_gens:
                return list(filter(lambda x: x.startswith(text), self.available_sub_gens[args[1]]))
            else:
                return []
        else:
            return []

    def complete_info(self, text: str, line: str, begidx, endidx):
        arg_count = len(split(line))
        if arg_count == 1 or len(split(line)) == 2 and text != '':
            return list(filter(lambda x: x.startswith(text), self.available_gens))
        if arg_count == 2 or len(split(line)) == 3 and text != '':
            return list(filter(lambda x: x.startswith(text), self.possible_info_subs))
        else:
            return []


if __name__ == '__main__':
    NamesCmd().cmdloop()
