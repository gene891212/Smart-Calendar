# Smart-Calendar

## Environment

- Install numpy

```shell
pip install numpy
```

- Install Google Client Library

```sh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

- Download project

Select "Download ZIP" and extract file
![download-code](img/download-code.png)

- Google Calendar API

Follow the step of [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python) to turn on Google Calendar API
![Calendar API quick start](img/calendar-api.png)

Save the file credential.json to the working directory

- Gmail API

Select your project in [Google API Console](https://console.developers.google.com/apis/library/gmail.googleapis.com?q=gmail)
![select project](img/select-project.png)

Turn on Gmail API
![enable-mail-api](img/enable-mail-api.png)

## Usage

- Run code

```sh
cd Smart-Calendar
python main.py
```

## Reference

- [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python)
- [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python)
