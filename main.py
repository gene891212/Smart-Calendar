import calendar, itertools, datetime
import numpy as np

from get_credential import generate_credential

class SmartCalendar():
    calendar.setfirstweekday(calendar.SUNDAY)

    def get_calendar_event(self):        
        service = generate_credential('calendar')
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        events_result = service.events().list(
            calendarId='85lnb8lqokpbkkt7ckvrgg3pu4@group.calendar.google.com',
            # timeMin=now,
            maxResults=10,
            singleEvents=True,
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

    def generate_calendar(self):    # 將日期控制在5行
        calendar1 = calendar.monthcalendar(self.year, self.month)
        self.date = np.array(calendar1)
        if len(self.date) > 5:   # 日期超過5行，將第5行加到第1行
            self.date[0] += self.date[-1]
            self.date = np.delete(self.date, -1, 0)
        elif len(self.date == 4):   # 日期等於四行，加一行0進去
            self.date = np.append(self.date, np.zeros((1, 7)), 0)
        else:
            pass
        print(self.date)

    def mail(self):
        service = generate_credential('gmail')
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])

if __name__ == "__main__":
    test = SmartCalendar()
    test.get_time()
    test.generate_calendar()
    test.get_calendar_event()
    # test.mail()