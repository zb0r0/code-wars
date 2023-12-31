# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.
#
# This is the first kata in series:
#
# Find the unique number (this kata)
# Find the unique string
# Find The Unique

#https://www.codewars.com/kata/585d7d5adb20cf33cb000235
#my solution:

def find_uniq(arr):
    count = 0
    for x in arr:
        if arr[0] != arr[1] and arr[1] == arr[2]:
            return arr[0]
        if ((x + arr[count+1])/2) != x:
            return arr[count+1]

        count += 1