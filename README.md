# Countdown/Letters and Numbers Solver

A simple program to solve problems on Countdown (or Letters and Numbers for fellow Australians).

## Example usage:

#### Numbers game with DFS
`python3 letters_and_numbers.py -g numbers -ns 8-5-7-100-25-50 -t 516`
#### Numbers game with BFS
`python3 letters_and_numbers.py -g numbers -ns 8-5-7-100-25-50 -t 516 -st True`
#### Letters game or conundrum
`python3 letters_and_numbers.py -g letters -l faintcase`

#### Each file can also be ran individually with:
`python3 numbers.py 50-100-9-1-9-3 727` (for DFS)
`python3 numbers.py 50-100-9-1-9-3 727` (for BFS)

`python3 letters.py faintcase`
