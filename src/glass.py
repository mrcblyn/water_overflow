"""Class to represent a single glass"""

import os


class Glass:
    """
    Each object represents a single glass, with attributes:
        `limit`: `float` capacity of each glass in liters.
                 Set environment variable `LIMIT` to modify. 0.25 by default.
        `volume`: `float` number of liters in the glass
        `overflow`: `float` number of liters over the limit
    """

    LIMIT = float(os.getenv("LIMIT", "0.25"))

    def __init__(self, limit=LIMIT):
        self.limit = limit
        self.volume = 0
        self.overflow = 0

    def pour(self, volume):
        """Pour volume into glass and calculate overflow"""
        if volume is None or volume < 0:
            raise ValueError(f"Volume should be > 0, provided: {volume}")

        self.volume += volume
        if self.volume >= self.limit:
            self.overflow = max(self.volume - self.limit, 0)
            self.volume = self.limit
