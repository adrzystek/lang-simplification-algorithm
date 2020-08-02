import logging
from typing import List, Union

import numpy as np


logger = logging.getLogger(__name__)

Point = List[int]


def apply_lang_algorithm(input_points: List[Point], tolerance: Union[int, float], look_ahead: int) -> List[Point]:
    """
    Apply the Lang simplification algorithm on a list of points.

    :param input_points: points that the algorithm is to be applied on
    :param tolerance: the maximum distance that an intermediate point can be located from the segment
    :param look_ahead: how many points to look ahead while defining a segment
    :return: a subset of `input_points` that is the result of the algorithm run
    """
    output_points = [input_points[0]]
    key_index = 0
    while True:
        segment = np.array(input_points[key_index : key_index + look_ahead + 1])
        points_from_segment_within_tolerance = get_points_within_tolerance(segment, tolerance)
        new_key = points_from_segment_within_tolerance[-1].tolist()
        output_points.append(new_key)
        key_index = input_points.index(new_key)
        if key_index == len(input_points) - 1:
            # we reached the end of the input points list
            break
    return output_points


def get_points_within_tolerance(points: np.ndarray, tolerance: Union[int, float]) -> np.ndarray:
    """
    This recurrent function returns a subset of `points` that fall within the tolerance limit.

    :param points: points forming a segment
    :param tolerance: the maximum distance between a point and the line between the first and the last point forming a
    segment
    :return: points for which the calculated distance falls below the tolerance level
    """
    points = points.copy()

    start_point = points[0]
    end_point = points[-1]
    intermediate_points = points[1:-1]

    if intermediate_points.shape[0] < 1:
        logger.debug("No more intermediate points.")
        return points

    intermediate_points_distance = calculate_perpendicular_distance(start_point, end_point, points[1:-1])
    if np.any(intermediate_points_distance > tolerance):
        logger.debug("At least one distance was larger than the tolerance.")
        points = points[:-1]
        return get_points_within_tolerance(points, tolerance)

    return points


def calculate_perpendicular_distance(
    start_point: np.ndarray, end_point: np.ndarray, intermediate_points: np.ndarray,
) -> Union[np.ndarray, float]:
    """
    Calculate the shortest (ie. perpendicular) distance from point(s) to a line drawn between `start_point` and
    `end_point`.

    :param start_point: one of the two points that determine the line location
    :param end_point: another of the two points that determine the line location
    :param intermediate_points: a point or an array of points that the distance is to be calculated for
    :return: either a single distance from an intermediate point to the line or - if the `intermediate_points` is an
    array of more than 1 point - an array of distances
    """
    return np.abs(
        np.cross(end_point - start_point, start_point - intermediate_points) / np.linalg.norm(end_point - start_point)
    )
