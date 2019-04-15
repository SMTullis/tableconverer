import datetime

class Table:
    def __init__(self, pay_data):
        self.id_usda = ""
        self.id_dod = ""
        self.effective_date = None
        self.term_date = None
        self.data = pay_data

    def Update_Pay_Data(self, **data):
        for plan in data.keys():
            for grade in data[plan].keys():
                self.data[plan][grade].update(data[plan][grade])

    def Export_CSV(self):
        return [
            [self.id_dod, self.id_usda, self.effective_date, self.term_date, plan, grade, step, self.data[plan][grade][step]
            ]
            for plan in self.data for grade in self.data[plan] for step in self.data[plan][grade]
        ]
