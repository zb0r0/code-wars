# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

#https://www.codewars.com/kata/576757b1df89ecf5bd00073b
#my solution:

def tower_builder(n_floors):
    spacje = n_floors - 1
    gwiazdki = 1
    choinka = []
    poziom = ''
    spacjee = spacje
    gwiazdkii = gwiazdki
    while n_floors > 0:
        while spacjee > 0:
            poziom += ' '
            spacjee -= 1
        while gwiazdkii > 0:
            poziom += '*'
            gwiazdkii -= 1
        spacjee = spacje
        while spacjee > 0:
            poziom += ' '
            spacjee -= 1
        spacje -= 1
        n_floors -= 1
        spacjee = spacje
        gwiazdki += 2
        choinka.append(poziom)
        poziom = ''
        gwiazdkii = gwiazdki
    return choinka