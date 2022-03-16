from sys import argv
import importlib
import inspect
import ast
import textwrap
import difflib
import itertools

def get_all_functions(class_to_parse, name_prefix):
    functions = list(map(lambda x: x, filter(lambda x: inspect.isfunction(x[1]), inspect.getmembers(class_to_parse))))
    classes = list(
        filter(lambda x: not x[0].startswith('__') and inspect.isclass(x[1]), inspect.getmembers(class_to_parse)))
    add_func = list(map(lambda x: get_all_functions(x[1], x[0]), classes))

    return list(map(lambda x: (f'{name_prefix}.{x[0]}', x[1]), functions + sum(add_func, [])))


def prepare_functions(funcs):
    field_names = ['name', 'id', 'arg', 'attr']
    new_funcs = []
    for fun in funcs:
        ass = ast.parse(textwrap.dedent(inspect.getsource(fun[1])))
        for item in ast.walk(ass):
            map(lambda x: item.__setattr__(x, '_'), field_names)
        new_funcs.append((fun[0], ast.unparse(ass)))
    return new_funcs


nice_funcs = []
for module_name in argv[1:]:
    imported_lib = importlib.import_module(module_name)
    nice_funcs += prepare_functions(get_all_functions(imported_lib, module_name))

for fun1, fun2 in itertools.combinations(nice_funcs, 2):
    if difflib.SequenceMatcher(a=fun1[1], b=fun2[1]).ratio() > 0.95:
        print(f'{fun1[0]:30} {fun2[0]:30}')
