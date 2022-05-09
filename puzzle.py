from PyQt5 import QtCore, QtGui, QtWidgets
from board import find_zero, check_input, check_solvable
from bfs import bfs
from dfs import dfs
<<<<<<< HEAD
from astar import a_star
from main import check_input
=======
from a_star import a_star
>>>>>>> dd5e7b5a6f6b0509ba432c821bde44075d976286
from node import *

goal = "012345678"

class Ui_MainWindow(object):
    i = 0
    path = [Node("012345678", None, None)]
    nodes_expanded = 0
    elapsed_time = 0

    def calc(self):
        self.comment("Processing")
<<<<<<< HEAD
        if check_input(self.initial.toPlainText()):
            node = Node(self.initial.toPlainText(), None, None)
            # BFS chosen
            if self.combo.currentText() == "BFS":
                print("BFS")
                self.path, self.nodes_expanded, self.elapsed_time = bfs(node, "012345678")
            # DFS chosen
            elif self.combo.currentText() == "DFS":
                print("DFS")
                self.path, self.nodes_expanded, self.elapsed_time = dfs(node, "012345678")
            # A-Star chosen
            else:
                print("A-Star")
                self.path, self.nodes_expanded, self.elapsed_time = a_star(node, "012345678",1)
            self.path.reverse()
            self.comments.setText(f"Elapsed Time = {round(self.elapsed_time, 6)} secs.\nExpanded Nodes = "
                                  f"{self.nodes_expanded}.\nDepth = {self.path[len(self.path)-1].depth}")
            self.fill_board(self.path[self.i])
            self.btn2.hide()
            self.clearbtn.show()
=======
        input = self.initial.toPlainText()
        if check_input(input):
            if check_solvable(input):
                node = Node(input, None, None)
                # BFS chosen
                if self.combo.currentText() == "BFS":
                    self.path, self.nodes_expanded, self.elapsed_time = bfs(node, goal)
                # DFS chosen
                elif self.combo.currentText() == "DFS":
                    self.path, self.nodes_expanded, self.elapsed_time = dfs(node, goal)
                # A-Star chosen
                elif self.combo.currentText() == "A-Star Manhattan":
                    self.path, self.nodes_expanded, self.elapsed_time = a_star(node, goal, 1)
                else:
                    self.path, self.nodes_expanded, self.elapsed_time = a_star(node, goal, 2)
                self.path.reverse()
                self.comments.setText(f"Elapsed Time = {round(self.elapsed_time, 6)} secs.\nExpanded Nodes = "
                                      f"{self.nodes_expanded}.\nDepth = {self.path[len(self.path)-1].depth}")
                self.fill_board(self.path[self.i])
                self.btn2.hide()
                self.clearbtn.show()
            else:
                self.comments.setText("Unsolvable State")

>>>>>>> dd5e7b5a6f6b0509ba432c821bde44075d976286
        else:
            self.comments.setText("Invalid")

    def fill_board(self, state):
        def fill():
            if self.i < len(self.path):
                list1 = list(self.path[self.i].state)
                zero = find_zero(self.path[self.i].state)
                list1[zero] = " "
                self.label_1.setText(list1[0])
                self.label_2.setText(list1[1])
                self.label_3.setText(list1[2])
                self.label_4.setText(list1[3])
                self.label_5.setText(list1[4])
                self.label_6.setText(list1[5])
                self.label_7.setText(list1[6])
                self.label_8.setText(list1[7])
                self.label_9.setText(list1[8])
                self.i += 1
        return fill

    def comment(self, message):
        self.comments.setText(message)

    def restart(self):
        self.initial.clear()
        self.comments.clear()
        self.clearbtn.hide()
        self.btn2.show()
        self.path = []
        self.elapsed_time = 0
        self.nodes_expanded = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 750)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.initial = QtWidgets.QTextEdit(self.centralwidget)
        self.initial.setGeometry(QtCore.QRect(460, 180, 400, 50))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.initial.setFont(font)
        self.initial.setStyleSheet("color: rgb(0, 0, 127);")
        self.initial.setAutoFillBackground(False)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.clicked.connect(self.fill_board(self.path[self.i].state))
        self.btn1.setGeometry(QtCore.QRect(780, 380, 160, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("color: rgb(0, 0, 127);")
        self.btn1.setAutoFillBackground(False)
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.clicked.connect(self.restart)
        self.clearbtn.setGeometry(QtCore.QRect(780, 480, 160, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.clearbtn.setFont(font)
        self.clearbtn.setStyleSheet("color: rgb(0, 0, 127);")
        self.clearbtn.setAutoFillBackground(False)
        self.clearbtn.hide()
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.clicked.connect(self.calc)
        self.btn2.setGeometry(QtCore.QRect(780, 480, 160, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("color: rgb(0, 0, 127);")
        self.btn2.setAutoFillBackground(False)
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.addItem("BFS")
        self.combo.addItem("DFS")
        self.combo.addItem("A-Star Manhattan")
        self.combo.addItem("A-Star Eucledian")
        self.combo.setGeometry(QtCore.QRect(810, 300, 100, 50))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.combo.setFont(font)
        self.combo.setAutoFillBackground(False)
        self.combo.setStyleSheet("color: rgb(0, 0, 127)")
        self.comments = QtWidgets.QLabel(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(460, 600, 600, 200))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.comments.setAlignment(QtCore.Qt.AlignLeft)
        self.comments.setFont(font)
        self.comments.setAutoFillBackground(False)
        self.comments.setStyleSheet("color: rgb(0, 0, 127)")
        self.initlbl = QtWidgets.QLabel(self.centralwidget)
        self.initlbl.setGeometry(QtCore.QRect(570, 120, 150, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.initlbl.setFont(font)
        self.initlbl.setAutoFillBackground(False)
        self.initlbl.setStyleSheet("color: rgb(0, 0, 127)")
        self.initlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.initlbl.setObjectName("initlbl")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(460, 280, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAutoFillBackground(False)
        self.label_1.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 280, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 280, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 380, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 380, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 380, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 480, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 480, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 480, 80, 80))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background: rgb(0, 0, 127);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.initlbl.setText(_translate("MainWindow", "Initial State"))
        self.label_1.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", ""))
        self.btn1.setText(_translate("MainWindow", "Next Step"))
        self.btn2.setText(_translate("MainWindow", "Calc"))
        self.clearbtn.setText(_translate("MainWindow", "Restart"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

