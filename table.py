import datetime

class Table:
    def __init__(self, pay_data):
        self.id_usda = ""
        self.id_dod = ""
        self.state = ""
        self.effective_date = None
        self.term_date = None
        self.data = pay_data

    def Update_Pay_Data(self, **data):
        for plan in data.keys():
            for grade in data[plan].keys():
                self.data[plan][grade].update(data[plan][grade])

    def Export_CSV(self):
        return [
            [self.id_dod, self.state, self.id_usda, self.effective_date, self.term_date, plan, grade, step, self.data[plan][grade][step]
            ]
            for plan in self.data for grade in self.data[plan] for step in self.data[plan][grade]
        ]

    def Reset(self):
        for plan in self.data.keys():
            for grade in self.data[plan].keys():
                for step in self.data[plan][grade].keys():
                    self.data[plan][grade][step] = 0

    def Set_Effective_Date(self, date_string, date_format):
        self.effective_date = datetime.datetime.strptime(date_string, date_format).date()
        self.term_date = self.effective_date + datetime.timedelta(days = 364)
