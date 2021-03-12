alexa@ubuntu-xenial:0x00-linear_algebra$ cat 3-main.py 
#!/usr/bin/env python3
def matrix_transpose(matrix):
    nm = []
    for i1 in range(len(matrix[0])):
        r = []
        for i2 in range(len(matrix)):
            r.append(matrix[i2][i1])
        nm.append(r)
    return nm
mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))