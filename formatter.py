import re

class TableFormatter:
    def __init__(self, *regexes):
        self.reg = regexes

    def MatchLine(self, line):
        for regex in self.reg:
            x = regex.findall(line)
            if len(x) > 0:
                return x

        return x
