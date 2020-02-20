# HashCode2020

This is the repository for team `<b>No BOLD</b>`.
Our final results:

A: 21

B: 5 822 900

C: 5 643 156

D: 4 815 395

E: 3 714 416

F: 5 227 905


## Setup

To get the code running, make a `hashcode2020` virtual python environment. Do `conda active hashcode2020` to get the environment running. Do `pip install -r requirements.txt` to install the python requirements. If you install new dependencies, don't forget to do `pip freeze > requirements.txt`.

## Usage

Use the `hashcode2020` virtual environment. To run with default settings, simply run `python .`. For more information, run `python . -h`.

## Solution

The code automatically generates the solution in the desired format. All the files required can be found in the `solution` folder.

## secret.py

For security reasons, `secret.py` is not in the git repo. Here is the template:

```python
SUBMISSION_URL = ''
```

## time_manager.py 

A simple script to keep track of the competition sprints. You'll hear a beep when sprint changed. Recomended that the script should be run in a seperate window.
