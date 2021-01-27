import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from untitled import Ui_MainWindow

class DateDetailWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DateDetailWindow, self).__init__(parent)
        self.label2 = QtWidgets.QLabel(self)

        
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # self.calendarWidget.move(0, 40)  # 位置
        self.startUIWindow()

    def startUIWindow(self):
        self.setWindowTitle("智能日歷")
        self.calendarWidget.clicked[QDate].connect(self.startDateDetail)
        date = self.calendarWidget.selectedDate()  # 获取选中日期，默认当前系统时间
        #self.label.setText(date.toString('yyyy-MM-dd dddd'))

        
    def startDateDetail(self, date):
        self.dateDetail = DateDetailWindow(self)
        self.setWindowTitle(date.toString('yyyy-MM-dd dddd'))
        self.setCentralWidget(self.dateDetail)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
