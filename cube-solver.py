import os
import json
from twophase.solver import solve, solveto
from sys import exit

global settings

def error(error: str, exitnum: int):
    print(f'Error: {error}')
    exit(exitnum)

os.system(command='rm -f ./twophase/phase* > /dev/null')

try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        f.close()
    importedfromfile = True
except:
    settings = {'solve_type': input('Enter solve type here: '), 'moves': int(input('Enter move number here: '))}
    importedfromfile = False

if settings.get('solve_type') == 'rescramble':
    cube = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
    with open('solved_state.txt', 'r') as f:
        solved_state = f.read()
        f.close()
    try:
        solution = solveto(cube, solved_state, 20, 10)
    except:
        error('cube-solver.py at line 29:\n\tCannot generate solution', 1)
elif settings.get('solve_type') == 'solve':
    with open('cube.txt', 'r') as f:
        cube = f.read()
        f.close()
    try:
        solution = solve(cube, settings.get('moves'), 10)
    except:
        error('cube-solver.py at line 37:\n\tCannot generate solution', 1)
else:
    if importedfromfile:
        error(f'settings.json at line 2:\n\tUnknown solve type: {0}'.format(settings.get('solve_type')), 1)
    else:
        error(f'cube-solver.py at line 20:\n\tUnknown solve type: {0}'.format(settings.get('solve_type')), 1)

os.system(command='rm -f ./twophase/phase* > /dev/null')
os.system(command='clear')
print(solution)
