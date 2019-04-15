import re
import table

class TableFormatter:
    def __init__(self, pay_data, **regexes):
        self.reg = regexes
        self.data_table = table.Table(pay_data)

    def CheckRegex(self, regex, line):
        return self.reg[regex].findall(line)

    def FindUSDANo(self, line):
        return self.CheckRegex("USDA", line)

    def FindDODNo(self, line):
        self.CheckRegex("DOD", line)

    def FindEffectiveDate(self, line):
        return self.CheckRegex("date", line)

    def FindState (self):
        return self.CheckRegex("state", line)

    def FindGrade(self, line):
        return self.CheckRegex("grade", line)

    def FindPayRates(self, line):
        return self.CheckRegex("rates", line)
