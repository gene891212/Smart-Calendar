import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

from calendarWindow import CalendarWindow
from detailWindow import DetailWindow

class Calendar(QtWidgets.QMainWindow, CalendarWindow, DetailWindow):
    def __init__(self, parent=None):
        super(Calendar, self).__init__()
        self.startCalendar()

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calendar = Calendar()
    calendar.showMaximized()
    sys.exit(app.exec_())
