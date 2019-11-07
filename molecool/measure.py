# have to import because you need it!
import numpy as np

def calculate_distance(pointA, pointB):
    """
    This function calculates the distance between two points.

    Parameters
    ----------
    pointA, pointB: np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between two points.

    Examples
    --------
    >>> r1 = np.array([0,0,0])
    >>> r2 = np.array([3,0,0])
    >>> calculate_distance(r1,r2)
    3.0
    """

    dist_vec = (pointA - pointB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_angle(pointA, pointB, pointC, degrees = False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees = True
    AB = pointB - pointA
    BC = pointB - pointC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
