import sys
import argparse

# letters and numbers classes
import letters
import numbers


parser = argparse.ArgumentParser()

parser.add_argument('-g',
                    choices=['letters', 'numbers'],
                    help='The type of game being played',
                    type=str)

parser.add_argument('-ls',
                    help='The letters for a letters game',
                    type=str)

parser.add_argument('-ws',
                    help='Custom word list file location',
                    type=str)

parser.add_argument('-ns',
                    help='The hyphen separated numbers for a numbers game',
                    type=str)

parser.add_argument('-t',
                    help='The target number for a numbers game',
                    type=int)

parser.add_argument('-st',
                    help='Solve type for the numbers solver (True for BFS False for DFS)',
                    type=bool,
                    default=False)

arguments = parser.parse_args()

game = arguments.g
ls = arguments.ls
ws = arguments.ws
ns = arguments.ns
g = arguments.t
st = arguments.st

if game == 'letters':
    ls = ls.lower()
    countdown_game = letters.letters_game(ls, ws)
else:
    nums = [int(n) for n in ns.split('-')]
    countdown_game = numbers.numbers_game(g, nums, st)

solution = countdown_game.solve()

if game == "letters":
    print(solution)
else:
    for a, op, b, r in solution:
        print(f"{op.capitalize()} {a} and {b} to get {r}")

