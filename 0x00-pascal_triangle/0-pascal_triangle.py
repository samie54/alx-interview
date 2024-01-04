#!/usr/bin/python3
'''Pascal’s Triangle Python Script'''


def pascal_triangle(n):
    '''
    returns lists of integers listed which represents Pascal’s triangle of n
    '''
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        temp = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp)

    return triangle
