import re

class TableFormatter:
    def __init__(self, *regexes):
        self.reg = regexes

    def MatchLine(self, line):
        for regex in self.reg:
            x = regex.match(line)

        return x
