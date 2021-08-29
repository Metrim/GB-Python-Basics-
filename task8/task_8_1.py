class Date:
    def __init__(self, cal):
        self.date = cal

    @classmethod
    def datetoint(cls, self):
        Date.datevalid(self)
        date, month, year = self.date.split("-")
        print(date, month, year)

    @staticmethod
    def datevalid(self):
        date, month, year = self.date.split("-")
        if 1 > int(date) or int(date) > 31:
            print(f"Введена дата с неверным числом: {date}")
        if 1 > int(month) or  int(month) > 12:
            print(f"Введена дата с неверным месяцем: {month}")
        if 1880 > int(year) or int(year) > 2020:
            print(f"Введена дата с неверным годом: {date}")
        if 32 > int(date) > 0 and 13 > int(month) > 0 and 2021 > int(year) > 1879:
            print(f"Дата введена полностью верно: {self.date}")


my_date = Date("32-13-2026")
my_date_1 = Date("1-12-1880")
my_date_2 = Date("26-05-1975")

Date.datevalid(my_date)
Date.datevalid(my_date_1)
my_date_1.datevalid(my_date_1)

Date.datetoint(my_date_2)

