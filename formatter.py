import csv
import re
import table

class TableFormatter:
    def __init__(self, pay_data, csv_writer, **regexes):
        self.reg = regexes
        self.data_table = table.Table(pay_data)
        self.writer = csv_writer

    def Check_Regex(self, regex, line):
        return self.reg[regex].findall(line)

    def Find_USDA_No(self, line):
        return self.Check_Regex("USDA", line)

    def Find_DOD_No(self, line):
        self.Check_Regex("DOD", line)

    def Find_Effective_Date(self, line):
        return self.Check_Regex("date", line)

    def Find_State(self, line):
        return self.Check_Regex("state", line)

    def Find_Grade(self, line):
        return self.Check_Regex("grade", line)

    def Find_Pay_Rates(self, line):
        return self.Check_Regex("rates", line)

    def Run(self, data):
        for line in data:
            match = None
            match = self.Find_Grade(line)
            if len(match) > 0:
                grade = int(match[0])
                rates = self.Find_Pay_Rates(line)

                pay_dict = {}

                if len(rates) == 3:
                    pay_dict["WG"] = {
                        grade:
                        {
                            i + 1: float(rate) for i, rate in enumerate(rates[0])
                        }
                    }
                    pay_dict["WL"] = {
                        grade:
                        {
                            i + 1: float(rate) for i, rate in enumerate(rates[1])
                        }
                    }
                    pay_dict["WS"] = {
                        grade:
                        {
                            i + 1: float(rate) for i, rate in enumerate(rates[2])
                        }
                    }
                else:
                    pay_dict["WS"] = {
                        grade:
                        {
                            i + 1: float(rate) for i, rate in enumerate(rates[0])
                        }
                    }

                self.data_table.Update_Pay_Data(**pay_dict)
                continue

            match = self.Find_USDA_No(line)
            if len(match) > 0:
                self.writer.writerows(self.data_table.Export_CSV())
                self.data_table.Reset()

                self.data_table.id_usda = match[0]
                dod = self.Find_DOD_No(line)
                if dod is not None:
                    self.data_table.id_dod = dod[0]

                continue

            match = self.Find_DOD_No(line)
            if len(match) > 0:
                self.data_table.id_dod = match[0]
                continue

            match = self.Find_State(line)
            if len(match) > 0:
                print(match)
                self.data_table.state = match[0]
                continue

            match = self.Find_Effective_Date(line)
            if len(match) > 0:
                self.data_table.Set_Effective_Date(match[0], "%d %B %Y")
                continue
