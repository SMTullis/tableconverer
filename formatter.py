import re

class TableFormatter:
    def __init__(self, **regexes):
        self.reg = regexes

    def CheckRegex(self, regex, line):
        return self.reg[regex].findall(line)
