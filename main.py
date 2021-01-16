import calendar
import numpy as np

class SmartCalendar(calendar.Calendar):
    calendar.setfirstweekday(calendar.SUNDAY)
    def generate_calendar(self, year, month):
        calendar1 = calendar.monthcalendar(year, month)
        date = np.array(calendar1)
        if len(date) > 5:
            date[0] += date[-1]
            date = np.delete(date, -1, 0)
            date = np.append(date, np.zeros((1, 7)).astype('int64'), 0)
        elif len(date == 4):
            pass
        else:
            return date
        return date

if __name__ == "__main__":
    test = SmartCalendar()
    print(test.generate_calendar(2021, 1))