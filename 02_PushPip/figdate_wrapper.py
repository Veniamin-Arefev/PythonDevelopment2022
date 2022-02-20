import os
import sys
import subprocess
import tempfile
import shutil
import venv

temp_path = tempfile.mkdtemp()
print(temp_path)

venv.create(temp_path, with_pip=True)

args = [temp_path + os.sep + 'bin' + os.sep + 'pip', 'install', 'pyfiglet']
print(f"Run with args:{args}")
subprocess.run(args)
args = [temp_path + os.sep + 'bin' + os.sep + 'python', '-m', 'figdate'] + sys.argv[1:]
print(f"Run with args:{args}")
subprocess.run(args)

shutil.rmtree(temp_path)
