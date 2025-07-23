# mlmath.py

"""
mlmath: A simple math library for basic machine learning operations.

Functions:
    - dot_product(a, b)
    - matrix_multiply(A, B)
    - conditional_probability(events)
"""

def dot_product(a, b):
    """
    Calculate the dot product of two lists or tuples of numbers.

    Args:
        a (list or tuple): First vector.
        b (list or tuple): Second vector.

    Returns:
        float: The dot product of a and b.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length.")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.

    Args:
        A (list of lists): First matrix (m x n).
        B (list of lists): Second matrix (n x p).

    Returns:
        list of lists: The result of matrix multiplication (m x p).
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(val)
        result.append(row)
    return result


def conditional_probability(events):
    """
    Calculate the conditional probability P(A|B) = P(A and B) / P(B).

    Args:
        events (dict): Dictionary with keys 'A', 'B', and 'A_and_B' representing probabilities.

    Returns:
        float: The conditional probability P(A|B).
    """
    P_B = events.get('B')
    P_A_and_B = events.get('A_and_B')
    if P_B is None or P_A_and_B is None:
        raise ValueError("Dictionary must contain 'B' and 'A_and_B' keys.")
    if P_B == 0:
        raise ZeroDivisionError("Probability of B cannot be zero.")
    return P_A_and_B / P_B
