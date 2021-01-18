import calendar
import numpy as np
import itertools
from segment_code import NUMBER_COMMON_CATHODE

class SmartCalendar():
    calendar.setfirstweekday(calendar.SUNDAY)
    all_decoder_data = list(itertools.product([0, 1], repeat=3))

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
    
    def output(self):
        for index, number in enumerate(display_date):
            seg = NUMBER_COMMON_CATHODE[number]
            decoder_data = all_decoder_data[index]
            print(decoder_data, seg, NUMBER_COMMON_CATHODE.index(seg))

if __name__ == "__main__":
    test = SmartCalendar()
    print(test.generate_calendar(2021, 1))