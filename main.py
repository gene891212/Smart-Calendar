import calendar, itertools, time
import numpy as np
from segment_code import NUMBER_COMMON_CATHODE

class SmartCalendar():
    calendar.setfirstweekday(calendar.SUNDAY)
    seg_decoder_data = list(itertools.product([0, 1], repeat=7))[:71]

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
        display_number = []
        for week in date:
            for day in week:
                ten = day // 10
                one = day % 10
                if ten == 0 and one == 0:
                    display_number += [10, 10]
                else:
                    display_number += [ten, one]
        return display_number

    def output_date(self):
        display_number = self.analyze_date()
        for index, number in enumerate(display_number):
            seg = NUMBER_COMMON_CATHODE[number]
            decoder_data = self.seg_decoder_data[index]
            print('decoder: {} seg: {} {}'.format(decoder_data, seg, NUMBER_COMMON_CATHODE.index(seg)))

if __name__ == "__main__":
    test = SmartCalendar()
    test.output_date()