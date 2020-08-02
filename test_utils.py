import numpy as np
import pytest

from utils import apply_lang_algorithm, calculate_perpendicular_distance, get_points_within_tolerance


@pytest.mark.parametrize(
    "start_point, end_point, intermediate_points, expected_result",
    [
        (np.array([-2, 0]), np.array([2, 0]), np.array([0, 5]), 5),
        (np.array([-2, 0]), np.array([2, 0]), np.array([0, -5]), 5),
        (np.array([-2, 0]), np.array([2, 0]), np.array([[0, 5], [0, -3]]), [5, 3]),
    ]
)
def test_calculate_perpendicular_distance(start_point, end_point, intermediate_points, expected_result):
    result = calculate_perpendicular_distance(start_point, end_point, intermediate_points)
    if type(result) == np.ndarray:
        result = result.tolist()
    assert result == expected_result


@pytest.mark.parametrize(
    "points, tolerance, expected_result",
    [
        (
            np.array([[3, 5], [5, 8], [10, 10], [16, 9], [19, 3]]),
            10,
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3]],
        ),
        (
            np.array([[3, 5], [5, 8], [10, 10], [16, 9], [19, 3]]),
            5,
            [[3, 5], [5, 8], [10, 10], [16, 9]],
        ),
        (
            np.array([[3, 5], [5, 8], [10, 10], [16, 9], [19, 3]]),
            1,
            [[3, 5], [5, 8]],
        ),
    ]
)
def test_get_points_within_tolerance(points, tolerance, expected_result):
    assert get_points_within_tolerance(points, tolerance).tolist() == expected_result


@pytest.mark.parametrize(
    "input_points, tolerance, look_ahead, expected_result",
    [
        (
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
            5,
            4,
            [[3, 5], [16, 9], [26, 4], [32, 11]],
        ),
        (
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
            5,
            10,
            [[3, 5], [31, 7], [32, 11]],
        ),
        (
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
            10,
            10,
            [[3, 5], [32, 11]],
        ),
        (
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
            1,
            10,
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
        ),
        (
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
            10,
            1,
            [[3, 5], [5, 8], [10, 10], [16, 9], [19, 3], [26, 4], [31, 7], [32, 11]],
        ),
    ]
)
def test_apply_lang_algorithm(input_points, tolerance, look_ahead, expected_result):
    assert apply_lang_algorithm(input_points, tolerance, look_ahead) == expected_result
