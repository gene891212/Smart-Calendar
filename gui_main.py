import pyaudio
import speech_recognition as sr
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from threading import Thread

sys.path.extend(["./windows", "./smart-calendar-api"])

from calendar_api import SmartCalendarAPI
from detailWindow import DetailWindow
from calendarWindow import CalendarWindow


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
        self.setWindowTitle(date.toString("yyyy-MM-dd dddd"))

        self.return_button.clicked.connect(self.startCalendar)
        self.input_button.clicked.connect(self.startListening)
        self.send_button.clicked.connect(self.sendToGoogle)
        self.cancel_button.clicked.connect(self.clearInput)

        self.select_date = date.toPyDate().strftime("%Y-%m-%d")
        Thread(target=self.insertToDoList).start()
        Thread(target=self.insertMailList).start()

    def insertToDoList(self):
        self.event_detail = self.api.get_event()
        for date, summary in self.event_detail:
            if self.select_date == date:
                self.to_Do_listWidget.addItem(summary)

    def insertMailList(self):
        self.message_details = self.api.mail()
        for date, title, content in self.message_details:
            if self.select_date == date:
                self.mail_listWidget.addItem(f"{title}----{content}...")

    # speech-to-text
    def sendToGoogle(self):
        self.api.insert_event(self.select_date, self.result)
        Thread(target=self.insertToDoList).start()

    def clearInput(self):
        self.result = ""
        self.input_label.setText("")

    def startListening(self):
        Thread(target=self.speechToText).start()

    def speechToText(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.input_label.setText("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            self.result = r.recognize_google(audio, language="zh-TW")
        except sr.UnknowValueError:
            self.result = "無法翻譯"
        except sr.RequestError as e:
            self.result = "無法翻譯{0}".format(e)
        self.input_label.setText(self.result)

    # def test(self):
    #     self.input_label.setText("hihi")
    #     self.result = "today"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calendar = SmartCalendar()
    calendar.show()
    sys.exit(app.exec_())
