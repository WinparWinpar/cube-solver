#!/usr/bin/env python3

import os
import sys

def main(args: str[0:]):
    aliasrc = False
    varrc = False

    os.chdir(os.path.dirname(args[0]))

    try:
        with open('.aliasrc', 'a') as f:
            f.write(f'\nalias cube-solver=\"cd {os.path.dirname(args[1])}; python3 cube-solver.py\"')
            f.close()
        aliasrc = True
        with open('.varrc', 'a') as f:
            f.write(f'\nexport CUBE_SOLVER={os.path.dirname(args[1])}')
            f.close()
        varrc = True
    except:
        aliasrc = False
        with open('.aliasrc', 'w+') as f:
            f.write(f'alias cube-solver=\"cd {os.path.dirname(args[1])}; python3 cube-solver.py\"')
            f.close()
        varrc = False
        with open('.varrc', 'w+') as f:
            f.write(f'export CUBE_SOLVER={os.path.dirname(args[1])}')
            f.close()

    if not aliasrc:
        with open('.bashrc', 'a') as f:
            f.write(f'\nif [ -f ~/.aliasrc]; then\n\t. ~/.aliasrc')
            f.close()
    if not varrc:
        with open('.bashrc', 'a') as f:
            f.write(f'\nif [ -f ~/.varrc]; then\n\t. ~/.varrc')
            f.close()

if __name__ == '__main__':
    main(sys.argv[1:])