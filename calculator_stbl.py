from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLabel, QApplication, QWidget, QVBoxLayout
import sys
from sympy import sympify

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def oneclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("1")
        else:
            line = line + "1"
            self.tex.setText(line)

    def twoclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("2")
        else:
            line = line + "2"
            self.tex.setText(line)

    def thrclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("3")
        else:
            line = line + "3"
            self.tex.setText(line)

    def fouclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("4")
        else:
            line = line + "4"
            self.tex.setText(line)

    def fivclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("5")
        else:
            line = line + "5"
            self.tex.setText(line)

    def sixclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("6")
        else:
            line = line + "6"
            self.tex.setText(line)

    def sevclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("7")
        else:    
            line = line + "7"
            self.tex.setText(line)

    def eigclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("8")
        else:
            line = line + "8"
            self.tex.setText(line)

    def ninclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("9")
        else:
            line = line + "9"
            self.tex.setText(line)

    def zerclick(self):
        line = self.tex.text()
        if line == "Error!":
            self.tex.setText("0")
        else:
            line = line + "0"
            self.tex.setText(line)

    def equclick(self):
        line = self.tex.text()
        try:
            proc = (line.replace("x","*"))
            self.tex.setText(str(sympify(proc)))
        except Exception as e:
            self.tex.setText("Error!")

    def addclick(self):
        line = self.tex.text()
        if line == "Error!":
            pass
        else:
            if self.tex.text().endswith(" "):
                list1 = list()
                full_string = ""
                for a in self.tex.text():
                    list1.append(a)

                list1[-2] = "+"

                for b in list1:
                    full_string = full_string + b

                self.tex.setText(full_string)

            else:
                line = self.tex.text()
                line = line + " + "
                self.tex.setText(line)



    def mulclick(self):
        line = self.tex.text()
        if line == "Error!":
            pass
        else:
            if self.tex.text().endswith(" "):
                list1 = list()
                full_string = ""
                for a in self.tex.text():
                    list1.append(a)

                list1[-2] = "x"

                for b in list1:
                    full_string = full_string + b

                self.tex.setText(full_string)

            else:
                line = self.tex.text()
                line = line + " x "
                self.tex.setText(line)

    def subclick(self):
        line = self.tex.text()
        if line == "Error!":
            pass
        else:
            if self.tex.text().endswith(" "):
                list1 = list()
                full_string = ""
                for a in self.tex.text():
                    list1.append(a)

                list1[-2] = "-"

                for b in list1:
                    full_string = full_string + b

                self.tex.setText(full_string)

            else:
                line = self.tex.text()
                line = line + " - "
                self.tex.setText(line)

    def divclick(self):
        line = self.tex.text()
        if line == "Error!":
            pass
        else:
            if self.tex.text().endswith(" "):
                list1 = list()
                full_string = ""
                for a in self.tex.text():
                    list1.append(a)

                list1[-2] = "/"

                for b in list1:
                    full_string = full_string + b

                self.tex.setText(full_string)

            else:
                line = self.tex.text()
                line = line + " / "
                self.tex.setText(line)

    def clrclick(self):
        self.tex.setText("")

    def init_ui(self):
        self.one = QPushButton("1")
        self.two = QPushButton("2")
        self.thr = QPushButton("3")
        self.fou = QPushButton("4")
        self.fiv = QPushButton("5")
        self.six = QPushButton("6")
        self.sev = QPushButton("7")
        self.eig = QPushButton("8")
        self.nin = QPushButton("9")
        self.zer = QPushButton("0")
        self.add = QPushButton("+")
        self.sub = QPushButton("-")
        self.mul = QPushButton("x")
        self.div = QPushButton("/")
        self.tex = QLabel("")
        self.equ = QPushButton("=")
        self.clr = QPushButton("CLR")

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        vbox1 = QVBoxLayout()

        hbox1.addWidget(self.one)
        hbox1.addWidget(self.two)
        hbox1.addWidget(self.thr)
        hbox1.addWidget(self.sub)
        hbox1.addStretch()
        hbox2.addWidget(self.fou)
        hbox2.addWidget(self.fiv)
        hbox2.addWidget(self.six)
        hbox2.addWidget(self.mul)
        hbox2.addStretch()
        hbox3.addWidget(self.sev)
        hbox3.addWidget(self.eig)
        hbox3.addWidget(self.nin)
        hbox3.addWidget(self.div)
        hbox3.addStretch()
        hbox4.addWidget(self.zer,4)
        hbox4.addWidget(self.add, 1)
        hbox4.addStretch()
        hbox5.addWidget(self.tex,4)
        hbox5.addWidget(self.clr,1)
        vbox1.addLayout(hbox5)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox4)
        vbox1.addWidget(self.equ)
        vbox1.addStretch()

        self.one.clicked.connect(self.oneclick)
        self.two.clicked.connect(self.twoclick)
        self.thr.clicked.connect(self.thrclick)
        self.fou.clicked.connect(self.fouclick)
        self.fiv.clicked.connect(self.fivclick)
        self.six.clicked.connect(self.sixclick)
        self.sev.clicked.connect(self.sevclick)
        self.eig.clicked.connect(self.eigclick)
        self.nin.clicked.connect(self.ninclick)
        self.zer.clicked.connect(self.zerclick)
        self.equ.clicked.connect(self.equclick)
        self.div.clicked.connect(self.divclick)
        self.mul.clicked.connect(self.mulclick)
        self.add.clicked.connect(self.addclick)
        self.sub.clicked.connect(self.subclick)
        self.clr.clicked.connect(self.clrclick)

        self.setLayout(vbox1)
        self.show()


app = QApplication(sys.argv)
win = Win()
win.setFixedSize(0,0)
win.setWindowTitle("Calculator")
win.show()
sys.exit(app.exec_())
