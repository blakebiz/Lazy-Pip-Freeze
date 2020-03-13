import subprocess
import sys


def build_reqs(file_name):
    while True:
        p = subprocess.Popen(['python.exe', file_name], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        output, error = p.communicate()
        error = str(error)
        if p.returncode != 0:
            if 'ModuleNotFoundError' in error:
                module = error[error.index('No module named')+18:]
                module = module[:module.index("'")-1]
                print(f'module: {module} was missing... installing now')
                process = subprocess.Popen([sys.executable, "-m", "pip", "install", module])
                process.wait()
            else:
                print('An unexpected error occured, please resolve this then run program again:')
                print(error)
                break
        else:
            with open('requirements.txt', 'w') as file:
                subprocess.call(['pip', 'freeze'], stdout=file)
            break

def main():
    build_reqs('example_file.py') # replace this with your file name and run that simple

if __name__ == '__main__':
    main()