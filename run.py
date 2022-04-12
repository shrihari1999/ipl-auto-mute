import os, sys

OS_NAME = sys.platform

VENV_PATH = os.environ.get("VIRTUAL_ENV")
if not VENV_PATH:
    print('venv not activated!!! Activating venv... Please run "python run.py" again.')
    os.system('pipenv shell')

if OS_NAME == 'win32':
    PYTHON_PATH = os.path.join(os.path.join(VENV_PATH, 'Scripts'), 'python.exe')
elif OS_NAME == 'linux':
    PYTHON_PATH = os.path.join(os.path.join(VENV_PATH, 'bin'), 'python')

os.system(f"{PYTHON_PATH} watch.py")