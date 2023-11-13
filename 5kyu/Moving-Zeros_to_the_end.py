# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

#https://www.codewars.com/kata/52597aa56021e91c93000cb0
#my solution:

def move_zeros(lst):
    count = 0
    new = []
    for x in lst:
        if x != 0:
            new.append(x)
        else:
            count += 1

    while count != 0:
        new.append(0)
        count -= 1

    return new