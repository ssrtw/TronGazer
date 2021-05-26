import sys
# qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
# view
from loginui import Ui_LoginWindow
from gazerui import Ui_GazerWindow
# util poster
from TronGazer import TronGazer

gazer = TronGazer()
app = QApplication(sys.argv)
LoginWindow = QMainWindow()
loginUI = Ui_LoginWindow()
GazerWindow = QMainWindow()
gazerUI = Ui_GazerWindow()

# style from https://github.com/liaokongVFX/QFlat
with open('dark_style.css') as cssfile:
    css = cssfile.read()


def loginBtnEvent():
    uid = loginUI.uidBox.text()
    password = loginUI.pwdBox.text()
    check = gazer.login_ttu(uid, password)
    if check:
        QMessageBox(QMessageBox.Information, "提示", "登入成功").exec()
        LoginWindow.close()
        initGazerWindow()
    else:
        QMessageBox(QMessageBox.Critical, "提示", "登入失敗").exec()


def courseBtnEvent():
    indexes = gazerUI.courseListView.selectedIndexes()
    if len(indexes) == 0:
        QMessageBox(QMessageBox.Warning, "提示", "請選擇課程").exec()
    else:
        idx = indexes[0].row()
        gazer.getVideos(gazer.all_course[idx]['id'])
        model = QStandardItemModel()
        gazerUI.videoListView.setModel(model)
        for video in gazer.videos:
            item = QStandardItem(video['title'])
            model.appendRow(item)
        gazerUI.gazeBtn.setEnabled(True)


def gazeBtnEvent():
    indexes = gazerUI.videoListView.selectedIndexes()
    if len(indexes) == 0:
        QMessageBox(QMessageBox.Warning, "提示", "請選擇影片").exec()
    else:
        try:
            for v in indexes:
                idx = v.row()
                gazer.watchVideo(gazer.videos[idx])
            QMessageBox(QMessageBox.Information, "提示", "影片觀看完畢").exec()
        except:
            QMessageBox(QMessageBox.Critical, "錯誤", "發生錯誤，請再次嘗試").exec()


def initGazerWindow():
    gazer.getUserInfo()
    gazer.getAllCourse()

    gazerUI.setupUi(GazerWindow)
    GazerWindow.setStyleSheet(css)
    gazerUI.courseBtn.setProperty('class', 'DarkGray')
    gazerUI.gazeBtn.setProperty('class', 'DarkGray')
    model = QStandardItemModel()
    gazerUI.courseListView.setModel(model)
    for course in gazer.all_course:
        item = QStandardItem(course['name'])
        model.appendRow(item)
    gazerUI.courseBtn.clicked.connect(courseBtnEvent)
    gazerUI.gazeBtn.setEnabled(False)
    gazerUI.gazeBtn.clicked.connect(gazeBtnEvent)
    GazerWindow.show()


def initLoginWindow():
    loginUI.setupUi(LoginWindow)
    loginUI.loginBtn.clicked.connect(loginBtnEvent)
    LoginWindow.setStyleSheet(css)
    loginUI.loginBtn.setProperty('class', 'DarkGray')
    LoginWindow.show()


initLoginWindow()
sys.exit(app.exec())
