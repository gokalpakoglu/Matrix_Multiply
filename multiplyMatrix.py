# -- coding: utf-8 --Gokalp Akoglu 181805035
def firstMatrix(row, column):
    # Initialize matrix
    matrix1 = []
    print("Please enter numbers of first matrix:")
    for a in range(row):
        x = []
        for b in range(column):
            x.append(int(input()))
        matrix1.append(x)
    # For printing the matrix
    print("First matrix is:\n")
    for a in range(row):
        for b in range(column):
            print(matrix1[a][b], end=" ")
        print()
    return matrix1


def secondMatrix(row2, column2):
    # Initialize matrix
    matrix2 = []
    print("Please enter numbers of second matrix:")
    for a in range(row2):
        y = []
        for b in range(column2):
            y.append(int(input()))
        matrix2.append(y)
    # For printing the matrix
    print("Second matrix is:\n")
    for a in range(row2):
        for b in range(column2):
            print(matrix2[a][b], end=" ")
        print()
    return matrix2


def multiplymatrices(firstMatrix, secondMatrix):
    #second column first row
    resultMatrix = [[0 for column in range(len(secondMatrix[0]))] for row in range(len(firstMatrix))]
    for a in range(len(firstMatrix)):
        for b in range(len(secondMatrix[0])):
            for c in range(len(secondMatrix)):
                resultMatrix[a][b] += firstMatrix[a][c] * secondMatrix[c][b]
    print("Your multiply matrices result is:\n")
    for z in resultMatrix:
        print(z)


def main():
    row = int(input("Enter the number of first matrix rows:"))
    column = int(input("Enter the number of first matrix columns:"))
    x = firstMatrix(row, column)
    row2 = int(input("Enter the number of second matrix rows:"))
    column2 = int(input("Enter the number of second matrix columns:"))
    y = secondMatrix(row2, column2)
    if row2 != column:
        print("This multiplication is not possible.")
        exit(0)
    else:
        multiplymatrices(x, y)


main()
