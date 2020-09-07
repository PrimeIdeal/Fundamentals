import numpy as np

def add_ones(x_data):
    """
    If design matrix is missing column of ones, adds a column
    """
    dims = x_data.shape
    new_x = np.ones((dims[0], dims[1]+1))
    new_x[:, :-1] = x_data
    return new_x

def ordinary_least_squares(x_data, y_data, multidot=False):
    """
    Computes parameter vector B for a linear regression model
        Y = X*B + E
    via direct computation:
        B = (X^T * X)^-1 * X^T * Y
    If (X^T * X) is degenerate matrix, computes B using
    Moore-Penrose pseudo-inverse:
        B = P(X) * Y

    Constraints
    -----------
    Design matrix X must contain a column of ones.

    Parameters
    ----------
    x_data : ndarray
        MxN design matrix containing M observations of N
        independent variables
    y_data : ndarray
        Vector containing M observations of the dependent variable
    multidot : bool
        Specifies use of numpy's multi_dot function. Defaults to
        False

    Returns
    -------
    ndarray
        Parameter vector for linear regression model
    """
    x_transpose = x_data.T
    try:
        if not multidot:
            return np.dot(np.dot(np.linalg.inv(np.dot(x_transpose, x_data)), x_transpose), y_data)
        return np.linalg.multi_dot([np.linalg.inv(np.dot(x_transpose, x_data)), x_transpose, y_data])
    except np.linalg.LinAlgError:
        return np.dot(np.linalg.pinv(x_data), y_data)