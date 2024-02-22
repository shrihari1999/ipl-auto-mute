# ipl-auto-mute
Mute IPL advertisements automatically on online platforms.

## Getting Started

### Install System Level Dependencies

 1. Python 3.7 64-bit or above. (This program uses tensorflow, please refer to https://www.tensorflow.org/install/pip#system-requirements for detailed requirements).
 2. pipenv

### Run the program
In the root directory where Pipfile is present, activate the virtual enviroment.
```
pipenv shell
```

If you're running the program for the first time, install required dependencies inside the venv.
```
pipenv install
```

Run the program, pass platform as first arg, event as second arg.
Available platforms: hotstar, jio
Available events: ipl, wc, test
```
# python run.py <platform> <event>
python run.py jio test
```

When the program is running, it is possible to control it using inputs
Available controls:
p - Pause the program
r - Resume the program
