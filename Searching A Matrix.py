# Searching a Matrix

# Given a matrix that is organised such that the numbers will always be sorted from left to right and the first number of each row will always
# be greater than the last element of the last row (mat[i][0] > mat[i-1][-1], search for a specific value in the matrix and return whether it exists.

# How I would answer this problem

#____________________________________________________________________________________________________________________________________________________



def searchMatrix(mat, value):
    if len(mat) == 0:
        return False
    row_len = len(mat)
    col_len = len(mat[0])

    low = 0
    high = row_len * col_len

    while low < high:
        mid = (low + high) // 2
        if mat[mid // col_len][mid % col_len] == value:
            return True
        elif mat[mid //col_len][mid % col_len] < value:
            low = mid + 1
        else:
            high = mid
    return False



mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

# This can be any number (mat,___) if the number is not in the array otherwise it will show "False"
print(searchMatrix(mat, 4))


print(searchMatrix(mat, 10))


print(searchMatrix(mat, 30))


print(searchMatrix(mat, 50))


print(searchMatrix(mat, 27))



