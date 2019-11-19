import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import  QTime, Qt

class DCBA(QMainWindow, QWidget):
    f = []
    f2 = []
    def __init__(self):
        super().__init__()

        self.time = QTime.currentTime()
        self.initUI()

    # 초기화 담당 함수
    def initUI(self):
        file = []
        exitAction = QAction(QIcon('exit.png'), '종료하기', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)
        FileOpenAction = QAction(QIcon('web.png'), '파일 열기', self)
        FileOpenAction.setShortcut('Ctrl+O')
        FileOpenAction.setStatusTip('파일을 엽니다.')
        FileOpenAction.triggered.connect(self.showDialog)
        test = QAction('테스트', self)
        test.triggered.connect(self.OpenFile)

        #self.statusBar().showMessage('develop by DDC_Semicolon_Network/Security Team')
        self.statusBar().showMessage(self.time.toString('hh:mm:ss'))

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('파일')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(FileOpenAction)
        fileMenu.addAction(test)

        self.toolbar = self.addToolBar('종료')
        self.toolbar.addAction(exitAction)


        #Label
        # label1 = QLabel('Label1', self)
        # label1.move(20, 20)
        # label2 = QLabel('Label2', self)
        # label2.move(20, 60)
        EventLabel = QLabel("크래킹된 비밀번호 :", self)

        #button
        # btn1 = QPushButton('Button1', self)
        # btn1.move(80,13)
        # btn2 = QPushButton('Button2', self)
        # btn2.move(80, 53)
        EncBtn = QPushButton('Encryption', self).move(16,70)

        #place
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addStretch(1)
        # vbox = QVBoxLayout()
        # vbox.addStretch(3)
        # vbox.addLayout(hbox)
        # vbox.addStretch(1)
        EventLabel.move(16,200)

        # self.setLayout(vbox)
        self.setWindowTitle('대덕뚫어')
        self.setWindowIcon(QIcon('DCBA_icon.png'))
        self.resize(300,500)
        self.show()

        #동작 코드
        # EncBtn.clicked.connect(self.crack)

    # 화면 중앙배치 함수
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'파일 열기', './')
        print(fname)
        print(fname[0])
        if fname[0]:
            self.f = open(fname[0], 'r')
            self.f.read()
            print(self.f)
            self.f.close()
            # with f:
            #     f = f.read()
            #     return f;
            #


    def OpenFile(self):
        f2 = open('test.txt', 'r')
        print(f2)

    def testf(self):
        print(self.f)


    def crack(self):
        crack=[]
        for i in range(0, 123):
            crack.append(chr(i))
        Password = self.f
        found_pw=[]
        start_index = 0
        for i in range(0, len(Password)):
            if(Password[i] == ':'):
                start_index = Password[i]

        for i in range(start_index, 8):
            for j in range(0, len(crack)):
                if (Password[i] == crack[j]):
                    found_pw.append(crack[j])
        print(str(found_pw))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DCBA()
    sys.exit(app.exec_())
