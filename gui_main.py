import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from threading import Timer

sys.path.extend(["./windows", "./smart-calendar-api"])

from calendar_api import SmartCalendarAPI
from detailWindow import DetailWindow
from calendarWindow import CalendarWindow

# from get_speech_text import get_speech_text


class SmartCalendar(QtWidgets.QMainWindow, CalendarWindow, DetailWindow):
    def __init__(self, parent=None):
        super(SmartCalendar, self).__init__()
        self.startCalendar()
        self.api = SmartCalendarAPI()

    def startCalendar(self):
        self.setupCalendar(self)
        self.setWindowTitle("智能日歷")
        self.calendarWidget.clicked[QDate].connect(self.startDateDetail)

    def startDateDetail(self, date):
        self.setupDetail(self)
        self.setWindowTitle(date.toString('yyyy-MM-dd dddd'))
        self.return_button.clicked.connect(self.startCalendar)
        self.input_button.clicked.connect(self.speechToText)

        self.select_date = date.toPyDate().strftime('%Y-%m-%d')
        Timer(0, self.insertToDoList).start()
        Timer(0, self.insertMailList).start()

    def insertToDoList(self):
        self.event_detail = self.api.get_event()
        for date, summary in self.event_detail:
            if self.select_date == date:
                self.to_Do_listWidget.addItem(summary)

    def insertMailList(self):
        self.message_details = self.api.mail()
        for date, title, content in self.message_details:
            if self.select_date == date:
                self.mail_listWidget.addItem(f'{title}----{content}...')

    def speechToText(self):
        def clear():
            self.input_label.setText("")

        def send():
            clear()
            self.api.insert_event(self.select_date, "test")
            Timer(0, self.insertToDoList).start()

        self.send_button.clicked.connect(send)
        self.cancel_button.clicked.connect(clear)
        self.input_label.setText("Listening...")

        # speech-to-text features
        # self.summary = get_speech_text()
        # self.input_label.setText(self.summary)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calendar = SmartCalendar()
    calendar.show()
    sys.exit(app.exec_())
