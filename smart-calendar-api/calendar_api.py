import datetime
from dateutil import parser

from get_credential import generate_credential


class SmartCalendarAPI():
    calendar_service = generate_credential('calendar')
    mail_service = generate_credential('gmail')

    def get_event(self):
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = self.calendar_service.events().list(
            calendarId='primary',
            # timeMin=now,
            # maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        event_detail = []
        if not events:
            print('No upcoming events found.')
        for event in events:
            if event.get('summary') == "self.summary":
                self.delete_event(event.get('id'))
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_detail += [(parser.parse(start).strftime('%Y-%m-%d'), event.get('summary'))]
        # print(event_detail)
        return event_detail

    def delete_event(self, eventId):
        self.calendar_service.events().delete(calendarId='primary', eventId=eventId).execute()

    def insert_event(self, date, summary):
        end_date = parser.parse(date) + datetime.timedelta(days=1)
        event = {
            'summary': summary,
            'start': {
                'date': date,
            },
            'end': {
                'date': end_date.strftime('%Y-%m-%d'),
            },
        }
        event = self.calendar_service.events().insert(
            calendarId='primary',
            body=event
        ).execute()

    def mail(self):
        results = self.mail_service.users().messages().list(
            userId='me',
            maxResults=10,
            labelIds='IMPORTANT',
        ).execute()
        labels = results.get('messages')

        message_details = []
        for label in labels:
            title = ''
            date = ''

            message = self.mail_service.users().messages().get(
                userId='me',
                id=label.get('id'),
            ).execute()

            content = message.get('snippet')
            for header in message['payload']['headers']:
                if header['name'] == 'Subject':
                    title = header.get('value')
                elif header['name'] == 'Date':
                    date = header.get('value')
            date = parser.parse(date).strftime('%Y-%m-%d')
            # print(date)
            message_details += [(date, title, content)]
        # print(message_details)
        return message_details


if __name__ == "__main__":
    test = SmartCalendarAPI()

    now = datetime.date(2021, 2, 2).strftime('%Y-%m-%d')
    test.insert_event(now, "test")
    test.get_event()
    # test.mail()
