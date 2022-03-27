"""
Class to represent the stack of glasses and process the water flow.
"""

from .glass import Glass
from .utils import log_time


class GlassController:
    """
    Class to represent the stack of glasses and process the water flow.
        `row`: `int` row of glass to check
        `col`: `int` column of glass to check
        `volume`: `float` remaining number of liters flowing
        `glasses`: `list` of Glass objects
    """

    def __init__(self, i, j, k):
        self.row = i
        self.col = j
        self.volume = k
        self.glasses = self._initialize_glasses()

    def _initialize_glasses(self):
        """Initialize empty glasses"""
        number_of_glasses = self._get_number_of_glasses()
        return [Glass() for glass in range(number_of_glasses)]

    def _get_number_of_glasses(self):
        """Calculate number of glasses only until the given row"""
        return int((self.row + 1) * (self.row + 2) / 2)

    def _get_glass_idx(self):
        """Convert row and column to glass index"""
        return int(self.row * (self.row + 1) / 2) + self.col

    @log_time
    def run(self):
        """
        Process water flow and return:
            - list of volume of glasses only until ith row
            - volume of the jth glass of ith row
        """

        # Pour volume on the top glass
        glass_idx = 0
        self.glasses[glass_idx].pour(self.volume)

        # Process downward flow on each row and column
        for _row in range(0, self.row):
            for _col in range(0, _row + 1):
                self.volume = self.glasses[glass_idx].overflow
                # Distribute overflows, half into left and half into right
                self.glasses[glass_idx + _row + 1].pour(self.volume / 2)
                self.glasses[glass_idx + _row + 2].pour(self.volume / 2)
                glass_idx += 1

        glasses = [g.volume for g in self.glasses]
        return (
            glasses,
            glasses[self._get_glass_idx()],
        )
