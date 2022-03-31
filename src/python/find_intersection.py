class IntersectionFinder:
    table = None
    key_color = None

    def __init__(self, table, key_color):
        """
        Fits table and key_color into class
        """
        self.table = table
        self.key_color = key_color

    def count_neighbors(self, i, j):
        """
        i, j - value type: int, ledeng: incides
        key - value type: int, legend: neighbor value to consider it as ally
        is neighbor has value key, then it is ally neighbor
        return number of ally neighbors
        """
        count = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a != 0 and b != 0:
                    if self.table[i + a][j + b] == self.key_color:
                        count += 1
        return count

    def has_symmetric_points(self, i, j):
        """
        i, j - value type: int, legend: indices
        due to the task two edges can not lie on one line. Therefore if there is any symmetric dots relatively our point
        and it is not usual line's point (see count_neighbors function), then it is intersection
        """
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a != 0 and b != 0:
                    if self.table[i + a][j + b] == self.table[i - a][j - b] and self.table[i - a][j - b] == self.key_color:
                        return True
        return False

    def is_intersection(self, i, j):
        """
        i, j - value type: int, legend: indices
        Checks whether given point is intersection of two lines
        """
        if self.count_neighbors(i, j) >= 4 and self.has_symmetric_points(i, j):
            return True
        return False

    def count_intersections(self):
        """
        Counts intersections
        """
        count_inters = 0
        for i in range(1, self.table.shape[0] - 1):
            for j in range(1, self.table.shape[1] - 1):
                if self.is_intersection(i, j):
                    count_inters += 1
        return count_inters

    def __del__(self):
        """
        Sets fields to None
        """
        self.table = None
        self.key_color = None
