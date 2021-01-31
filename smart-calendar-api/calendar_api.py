import datetime
import json
from dateutil import parser

from get_credential import generate_credential

class SmartCalendarAPI():
    def get_calendar_event(self):
        service = generate_credential('calendar')
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(
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
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_detail += [(parser.parse(start).strftime("%Y/%m/%d"), event.get('summary'))]
        return event_detail

    def mail(self):
        service = generate_credential('gmail')
        results = service.users().messages().list(
            userId='me',
            maxResults=15,
            labelIds='IMPORTANT',
        ).execute()
        labels = results.get('messages')

        message_details = []
        for label in labels:
            title = ''
            date = ''

            message = service.users().messages().get(
                userId='me',
                id=label.get('id'),
            ).execute()

            content = message.get('snippet')
            for header in message['payload']['headers']:
                if header['name'] == 'Subject':
                    title = header.get('value')
                elif header['name'] == 'Date':
                    date = header.get('value')
            date = parser.parse(date).strftime("%Y/%m/%d")
            print(date)
            message_details += [(date, title, content)]
        return message_details
if __name__ == "__main__":
    test = SmartCalendarAPI()
    # test.get_calendar_event()
    # test.get_time()
    test.mail()
