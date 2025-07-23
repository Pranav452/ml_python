# vector_matrix_operations.py

# Function to add two vectors
def add_vectors(a, b):
    """
    Adds two vectors element-wise.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")
    return [a[i] + b[i] for i in range(len(a))]

# Function to compute the dot product of two vectors
def dot_product(a, b):
    """
    Computes the dot product of two vectors.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")
    return sum(a[i] * b[i] for i in range(len(a)))

# Function to check if two vectors are orthogonal
def are_orthogonal(a, b):
    """
    Checks if two vectors are orthogonal (dot product is zero).
    """
    return dot_product(a, b) == 0

# Function to multiply two matrices
def multiply_matrices(A, B):
    """
    Multiplies two matrices using nested loops.
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_product = 0
            for k in range(len(B)):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result
