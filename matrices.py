import numpy as np 

def basic_matrix(): 
    # Create matrix 
    A = np.array([[0, 1, 2, 3, 4], [1, 2, 3, 4, 5]])

    # Print matrix
    print("The matrix is")
    print(A)

def basic_matrix_operations():
    A = np.array([[2, 3], [8, 4]])
    print("The matrix is")
    print(A)

    # Find the determinant of the matrix
    A_det = np.linalg.det(A)
    print("Determinant of A is ")
    print(A_det)

    # Find the transpose of a matrix
    A_t = A.transpose()
    print("Transpose of a matrix is")
    print(A_t)

    # Find the inverse of a matrix
    A_inv = np.linalg.inv(A)
    print("The inverse of matrix A is ")
    print(A_inv)

basic_matrix()
basic_matrix_operations()
