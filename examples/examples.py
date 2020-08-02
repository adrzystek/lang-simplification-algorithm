from typing import List

import matplotlib.pyplot as plt
import numpy as np

from utils import Point, apply_lang_algorithm


POINTS = [
    [3, 5],
    [5, 8],
    [10, 10],
    [16, 9],
    [19, 3],
    [26, 4],
    [31, 7],
    [32, 11],
]


def _draw(points_before: List[Point], points_after: List[Point], title: str) -> None:
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={"hspace": 0.3})
    fig.suptitle(title)

    min_y = min(points_before, key=lambda x: x[1])[1] * 0.9
    max_y = max(points_before, key=lambda x: x[1])[1] * 1.1

    ax1.set_ylim([min_y, max_y])
    ax2.set_ylim([min_y, max_y])

    ax1.title.set_text("before")
    ax2.title.set_text("after")

    kwargs = {"marker": ".", "markersize": 15, "markerfacecolor": "red", "markeredgecolor": "red"}
    ax1.plot(*np.transpose(points_before), "b-", **kwargs)
    ax2.plot(*np.transpose(points_after), "b-", **kwargs)

    plt.savefig(f"{title}.png")


for look_ahead in range(1, 8):
    for tolerance in range(1, 8):
        resulting_points = apply_lang_algorithm(POINTS, tolerance, look_ahead)
        _draw(POINTS, resulting_points, f"tolerance_{tolerance}__look_ahead_{look_ahead}")
