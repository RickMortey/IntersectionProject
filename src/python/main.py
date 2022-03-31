import numpy as np
from PIL import Image
from find_intersection import *
from pathlib import Path

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image",
        type=str,
        default=str(Path("examples/test.png").resolve()),
    )

    args = parser.parse_args()
    image = args.image

    img_array = np.asarray(Image.open(image).convert('L'))
    table = np.copy(img_array)
    key_color = 25

    for i in range(0, table.shape[0]):
        for j in range(1, table.shape[1] - 1):
            if table[i, j] == 0 and table[i, j - 1] == 0 and table[i, j + 1] == 0:
                table[i, j] = key_color

    solver = IntersectionFinder(table, key_color)
    answer = solver.count_intersections()
    print("Graph has {} intersections!".format(answer))