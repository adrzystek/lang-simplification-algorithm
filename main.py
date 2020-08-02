import argparse

from utils import apply_lang_algorithm


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply the Lang simplification algorithm on a list of points.")
    parser.add_argument(
        "-p",
        "--points",
        required=True,
        nargs="+",
        action="append",
        type=float,
        help="points that the algorithm is to be applied on",
    )
    parser.add_argument(
        "-t",
        "--tolerance",
        required=True,
        type=float,
        help="the maximum distance that an intermediate point can be located from the segment",
    )
    parser.add_argument(
        "-l"
        "--look_ahead",
        required=True,
        type=int,
        help="how many points to look ahead when defining a segment",
        dest="look_ahead",
    )

    args = parser.parse_args()

    print(apply_lang_algorithm(args.points, args.tolerance, args.look_ahead))
