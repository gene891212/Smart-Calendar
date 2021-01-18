import calendar
import numpy as np
import time

NUMBER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class SmartCalendar(calendar.Calendar):
    calendar.setfirstweekday(calendar.SUNDAY)

    def get_time(self):
        now_time = time.localtime(time.time())
        year = now_time.tm_year
        month = now_time.tm_mon
        return year, month

    def generate_calendar(self):
        year, month = self.get_time()
        calendar1 = calendar.monthcalendar(year, month)
        date = np.array(calendar1)
        if len(date) > 5:   # 日期超過5行，將第5行加到第1行
            date[0] += date[-1]
            date = np.delete(date, -1, 0)
        elif len(date == 4):
            date = np.append(date, np.zeros((1, 7)), 0) # 日期等於四行，加一行0進去
        else:
            return date
        return date

    def analyze_date(self):
        date = self.generate_calendar()
        self.display_number = np.array([])
        print(self.display_number)
        for week in date:
            for day in week:
                ten = day // 10
                one = day % 10
                self.display_number += [[ten, one]]
                # self.display_number = np.append(self.display_number, np.array([ten, one], ndmin=2))
        print(self.display_number)
        print(type(self.display_number))

if __name__ == "__main__":
    test = SmartCalendar()
    test.analyze_date()