"""Files tests simple file read related operations"""
from __future__ import division
from io import open


class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        file = open(file_path, encoding='utf-8')
        lines = file.read()
        for line in lines.splitlines():
            self.numbers.append([int(v) for v in line.split()])
        file.close() 			

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        if self.isIndexError(line_number):
            return 'null'
        return self.get_sum(line_number) / len(self.numbers[line_number])

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        if self.isIndexError(line_number):
            return 'null'
        return max(self.numbers[line_number])

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        if self.isIndexError(line_number):
            return 'null'
        return min(self.numbers[line_number])

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        if self.isIndexError(line_number):
            return 'null'		
        sum = 0
        row = self.numbers[line_number]
        for num in row:
            sum += num
        return sum

    def isIndexError(self, line_number):
        """
        check if line_number exceed range or negative
        """
        return line_number < 0 or line_number + 1 > len(self.numbers)
