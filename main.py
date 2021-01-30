import datetime
import numpy as np

from dateutil import parser
from get_credential import generate_credential


class SmartCalendar():

    def get_calendar_event(self):
        service = generate_credential('calendar')
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        events_result = service.events().list(
            calendarId='primary',
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

    def mail(self):
        service = generate_credential('gmail')
        results = service.users().messages().list(
            userId='me',
            maxResults=1,
            labelIds='IMPORTANT',
        ).execute()
        labels = results.get('messages')

        for label in labels:
            title = ''
            date = ''

            message_detail = service.users().messages().get(
                userId='me',
                id=label.get('id'),
            ).execute()

            content = message_detail.get('snippet')
            for header in message_detail['payload']['headers']:
                if header['name'] == 'Subject':
                    title = header.get('value')
                elif header['name'] == 'Date':
                    date = header.get('value')
            print(title, date, content)


if __name__ == "__main__":
    test = SmartCalendar()
    test.get_time()
    # test.get_clendar_event()
    test.mail()
