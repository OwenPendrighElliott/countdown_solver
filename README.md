# Countdown/Letters and Numbers Solver

A simple program to solve problems on Countdown (or Letters and Numbers for fellow Australians). Can also do 'trickshot' solutions to numbers games (a silly solution that is just showing off).

## Example usage:

#### Normal numbers game
`python3 letters_and_numbers.py -g numbers -ns 8-5-7-100-25-50 -t 516`
#### Numbers game with a trickshot solution
`python3 letters_and_numbers.py -g numbers -ns 8-5-7-100-25-50 -t 516 -ts True`
#### Letters game or conundrum
`python3 letters_and_numbers.py -g letters -l faintcase`

#### Each file can also be ran individually with:
+ `python3 numbers.py 50-100-9-1-9-3 727` (for normal)
+ `python3 numbers.py 50-100-9-1-9-3 727 True` (for trickshot)

+ `python3 letters.py faintcase`
