# Google api
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

API_DETIALS = {
    'calendar': {
        'SCOPES': ['https://www.googleapis.com/auth/calendar.readonly'],
        'NAME': 'calendar',
        'VERSION': 'v3',
        'TOKEN_NAME': 'calendar-token.pickle'
    },
    'gmail': {
        'SCOPES': ['https://www.googleapis.com/auth/gmail.readonly'],
        'NAME': 'gmail',
        'VERSION': 'v1',
        'TOKEN_NAME': 'gmail-token.pickle'
    }
}


def generate_credential(name):
    api = API_DETIALS[name]
    creds = None
    if os.path.exists(api['TOKEN_NAME']):
        with open(api['TOKEN_NAME'], 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_TOKEN:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', api['SCOPES'])
            creds = flow.run_local_server(port=0)
        with open(api['TOKEN_NAME'], 'wb') as token:   # Save the credentials for the next run
            pickle.dump(creds, token)

    service = build(api['NAME'], api['VERSION'], credentials=creds)
    return service


