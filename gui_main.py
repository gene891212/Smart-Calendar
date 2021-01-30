import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

sys.path.extend(["./windows", "./smart-calendar-api"])

from calendarWindow import CalendarWindow
from detailWindow import DetailWindow

from calendar_api import SmartCalendarAPI

class SmartCalendar(QtWidgets.QMainWindow, CalendarWindow, DetailWindow):
    def __init__(self, parent=None):
        super(SmartCalendar, self).__init__()
        self.startCalendar()
        self.api = SmartCalendarAPI()

    def startCalendar(self):
        self.setupCalendar(self)
        self.setWindowTitle("智能日歷")
        self.calendarWidget.clicked[QDate].connect(self.startDateDetail)
        # today = self.calendarWidget.selectedDate()  # 获取选中日期，默认当前系统时间
        # print(today.toPyDate())

    def startDateDetail(self, date):
        print(date)
        self.setupDetail(self)
        self.setWindowTitle(date.toString('yyyy-MM-dd dddd'))
        self.return_Button.clicked.connect(self.startCalendar)

    def changeMailContent(self):
        pass
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calendar = SmartCalendar()
    calendar.showMaximized()
    sys.exit(app.exec_())
