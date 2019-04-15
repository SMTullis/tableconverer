import re
import table

class TableFormatter:
    def __init__(self, pay_data, **regexes):
        self.reg = regexes
        self.data_table = table.Table(pay_data)

    def CheckRegex(self, regex, line):
        return self.reg[regex].findall(line)
