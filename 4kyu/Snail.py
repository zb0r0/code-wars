# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
#my solution:

def snail(snail_map):
    x = 0
    y = 0
    waz = []
    i = 0
    n = 0
    print(snail_map)

    for wiersz in snail_map:
        n += 1

    if snail_map == [[]]:
        return []
    else:
        #prawo
        while i < n:
            waz.append(snail_map[x][y])
            y += 1
            i += 1

        i = 0
        n -= 1
        y -= 1
        while n > 0:
            #dół
            while i < n:
                x += 1
                waz.append(snail_map[x][y])
                i += 1
            i = 0
            #lewo
            while i < n:
                y -= 1
                waz.append(snail_map[x][y])
                i += 1
            i = 0
            n -= 1
            #góra
            while i < n:
                x -= 1
                waz.append(snail_map[x][y])
                i += 1
            i = 0
            #prawo
            while i < n:
                y += 1
                waz.append(snail_map[x][y])
                i += 1
            i = 0
            n -= 1


        return waz