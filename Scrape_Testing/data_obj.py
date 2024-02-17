"""
This file contains the data objects used in the project.  The LithiumData object will store all data from a given
row, and has specialized functions to convert data into a format readable for xlsxwriter.
"""


class LithiumData:
    def __init__(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date


class GFEXData:
    def __init__(self, name, price, date, lit_High, lit_Low, Volume):
        self.name = name
        self.price = price
        self.date = date
        self.lit_High = lit_High
        self.lit_Low = lit_Low
        self.volume = Volume
