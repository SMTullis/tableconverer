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

    def Run(self, data):
        for line in data:
            match = None
            match = self.FindGrade(line)
            if len(match) > 0:
                rates = self.FindPayRates(line)
                pass

            match = self.FindUSDANo(line)
            if len(match) > 0:
                out = self.table.Export_CSV()
                self.table.Reset()

                self.table.usda_no = match
                dod = self.FindDODNo(line)
                if len(dod) > 0:
                    self.table.dod_no = dod

                continue

            match = self.FindDODNo(line)
            if len(match) > 0:
                self.table.dod_no = match
                continue

            match = self.FindState(line):
            if len(match) > 0:
                self.table.state = match
                continue

            match = self.FindEffectiveDate(line):
            if len(match) > 0:
                self.table.SetEffectiveDate(match, "%d %B %Y")
                continue
            
