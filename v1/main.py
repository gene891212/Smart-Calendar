import calendar, itertools, datetime
import numpy as np
from segment_code import NUMBER_COMMON_CATHODE

from calendar_credential import google_api_credential

class SmartCalendar():
    calendar.setfirstweekday(calendar.SUNDAY)
    seg_decoder_data = list(itertools.product([0, 1], repeat=7))[:71]
    service = google_api_credential()

    def get_all_calendar_event(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        events_result = self.service.events().list(
            calendarId='85lnb8lqokpbkkt7ckvrgg3pu4@group.calendar.google.com', 
            # timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime'
        ).execute()
        self.events = events_result.get('items', [])

        if not self.events:
            print('No upcoming events found.')
        for event in self.events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    def get_time(self):
        now_time = datetime.datetime.now()
        self.year = now_time.year
        self.month = now_time.month

    def generate_calendar(self):
        calendar1 = calendar.monthcalendar(self.year, self.month)
        self.date = np.array(calendar1)
        if len(self.date) > 5:   # 日期超過5行，將第5行加到第1行
            self.date[0] += self.date[-1]
            self.date = np.delete(self.date, -1, 0)
        elif len(self.date == 4):
            self.date = np.append(self.date, np.zeros((1, 7)), 0) # 日期等於四行，加一行0進去
        else:
            pass

    def analyze_date(self):
        self.display_number = []
        for week in self.date:
            for day in week:
                ten = day // 10
                one = day % 10
                if ten == 0 and one == 0:
                    self.display_number += [10, 10]
                else:
                    self.display_number += [ten, one]

    def output_date(self):
        self.get_time()
        self.generate_calendar()
        self.analyze_date()
        for index, number in enumerate(self.display_number):
            seg = NUMBER_COMMON_CATHODE[number]
            decoder_data = self.seg_decoder_data[index]
            print('decoder: {} seg: {} {}'.format(decoder_data, seg, NUMBER_COMMON_CATHODE.index(seg)))

if __name__ == "__main__":
    test = SmartCalendar()
    # test.output_date()
    test.get_all_calendar_event()
    