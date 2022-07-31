import os
import json
from twophase.solver import solve, solveto

os.system(command='rm -f ./twophase/phase* > /dev/null')

try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        f.close()
except:
    settings = {'solve_type': input('Enter solve type here: '), 'moves': int(input('Enter move number here: '))}

if settings.get('solve_type') == 'rescramble':
    cube = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
    with open('solved_state.txt', 'r') as f:
        solved_state = f.read()
        f.close()
    solution = solveto(cube, solved_state, 20, 10)
else:
    with open('cube.txt', 'r') as f:
        cube = f.read()
        f.close()
    solution = solve(cube, settings.get('moves'), 10)

os.system(command='rm -f ./twophase/phase* > /dev/null')
os.system(command='clear')
print(solution)