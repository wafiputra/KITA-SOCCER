# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from futsal import *
import mysql.connector

class Ui_MainWindow(object):

    def koneksi(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database = "futsal"
        )

        mycursor = con.cursor()
        if(mycursor):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 623)
        self.koneksi()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_background1 = QtWidgets.QLabel(self.centralwidget)
        self.label_background1.setGeometry(QtCore.QRect(0, -3, 751, 591))
        self.label_background1.setStyleSheet("background-image: url(lapangan.jpg);\n"
        "border-image: url(lapangan.jpg);")
        self.label_background1.setObjectName("label_background1")
        self.label_background2 = QtWidgets.QLabel(self.centralwidget)
        self.label_background2.setGeometry(QtCore.QRect(140, 80, 461, 391))
        self.label_background2.setStyleSheet("BACKGROUND:rgb(138, 170, 140)")
        self.label_background2.setObjectName("label_background2")
        self.label_background3 = QtWidgets.QLabel(self.centralwidget)
        self.label_background3.setGeometry(QtCore.QRect(150, 89, 441, 61))
        self.label_background3.setStyleSheet("BACKGROUND:rgb(0, 80, 0)")
        self.label_background3.setText("")
        self.label_background3.setObjectName("label_background3")
        
        self.label_logo_login = QtWidgets.QLabel(self.centralwidget)
        self.label_logo_login.setGeometry(QtCore.QRect(320, 110, 101, 81))
        self.label_logo_login.setStyleSheet("image: url(logo login.png);\n"
        "color: rgb(255, 255, 255);")
        self.label_logo_login.setText("")
        self.label_logo_login.setObjectName("label_logo_login")
        
        self.label_background4 = QtWidgets.QLabel(self.centralwidget)
        self.label_background4.setGeometry(QtCore.QRect(150, 400, 441, 61))
        self.label_background4.setStyleSheet("BACKGROUND:rgb(0, 80, 0)")
        self.label_background4.setText("")
        self.label_background4.setObjectName("label_background4")
        
        self.label_logo_user = QtWidgets.QLabel(self.centralwidget)
        self.label_logo_user.setGeometry(QtCore.QRect(200, 270, 51, 31))
        self.label_logo_user.setStyleSheet("image: url(user.png);")
        self.label_logo_user.setText("")
        self.label_logo_user.setObjectName("label_logo_user")
        
        self.lineUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUser.setGeometry(QtCore.QRect(270, 270, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        
        self.lineUser.setFont(font)
        self.lineUser.setStyleSheet("background: transparent;\n"
        "color:black;\n"
        "border:none;\n"
        "border-bottom:1px solid")
        self.lineUser.setObjectName("lineUser")
        
        self.label_logo_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_logo_pass.setGeometry(QtCore.QRect(200, 340, 55, 31))
        self.label_logo_pass.setStyleSheet("image: url(gembok.png);")
        self.label_logo_pass.setObjectName("label_logo_pass")
        
        self.linePass = QtWidgets.QLineEdit(self.centralwidget)
        self.linePass.setGeometry(QtCore.QRect(270, 340, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        
        self.linePass.setFont(font)
        self.linePass.setStyleSheet("background: transparent;\n"
        "color:black;\n"
        "border:none;\n"
        "border-bottom:1px solid")
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(320, 190, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("")
        self.label_login.setObjectName("label_login")
        self.push_OK = QtWidgets.QPushButton(self.centralwidget)
        self.push_OK.setGeometry(QtCore.QRect(320, 420, 93, 28))
        self.push_OK.clicked.connect(self.login)
        
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.push_OK.setFont(font)
        self.push_OK.setObjectName("push_OK")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupUtama(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_background1 = QtWidgets.QLabel(self.centralwidget)
        self.label_background1.setGeometry(QtCore.QRect(0, 0, 771, 621))
        self.label_background1.setStyleSheet("background-image: url(lapangan.jpg);")
        self.label_background1.setText("")
        self.label_background1.setPixmap(QtGui.QPixmap("lapangan.jpg"))
        self.label_background1.setScaledContents(True)
        self.label_background1.setObjectName("label_background1")
        self.label_background2 = QtWidgets.QLabel(self.centralwidget)
        self.label_background2.setGeometry(QtCore.QRect(140, 100, 471, 431))
        self.label_background2.setStyleSheet("BACKGROUND:rgb(138, 170, 140)")
        self.label_background2.setText("")
        self.label_background2.setObjectName("label_background2")
        self.label_background3 = QtWidgets.QLabel(self.centralwidget)
        self.label_background3.setGeometry(QtCore.QRect(150, 110, 451, 61))
        self.label_background3.setStyleSheet("BACKGROUND:rgb(0, 80, 0)")
        self.label_background3.setText("")
        self.label_background3.setObjectName("label_background3")
        self.label_logo_bola = QtWidgets.QLabel(self.centralwidget)
        self.label_logo_bola.setGeometry(QtCore.QRect(250, 110, 61, 61))
        self.label_logo_bola.setStyleSheet("image: url(ball.png);")
        self.label_logo_bola.setText("")
        self.label_logo_bola.setObjectName("label_logo_bola")
        self.label_kita_soccer = QtWidgets.QLabel(self.centralwidget)
        self.label_kita_soccer.setGeometry(QtCore.QRect(310, 110, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setBold(True)
        font.setWeight(75)
        self.label_kita_soccer.setFont(font)
        self.label_kita_soccer.setStyleSheet("")
        self.label_kita_soccer.setObjectName("label_kita_soccer")
        self.label_background4 = QtWidgets.QLabel(self.centralwidget)
        self.label_background4.setGeometry(QtCore.QRect(150, 460, 451, 61))
        self.label_background4.setStyleSheet("BACKGROUND:rgb(0, 80, 0)")
        self.label_background4.setText("")
        self.label_background4.setObjectName("label_background4")
        self.label_nama_team = QtWidgets.QLabel(self.centralwidget)
        self.label_nama_team.setGeometry(QtCore.QRect(210, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_nama_team.setFont(font)
        self.label_nama_team.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_nama_team.setObjectName("label_nama_team")
        self.label_booking = QtWidgets.QLabel(self.centralwidget)
        self.label_booking.setGeometry(QtCore.QRect(210, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_booking.setFont(font)
        self.label_booking.setObjectName("label_booking")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(390, 260, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_main.setFont(font)
        self.label_main.setObjectName("label_main")
        self.label_durasi = QtWidgets.QLabel(self.centralwidget)
        self.label_durasi.setGeometry(QtCore.QRect(480, 320, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_durasi.setFont(font)
        self.label_durasi.setObjectName("label_durasi")
        self.label_pembayaran = QtWidgets.QLabel(self.centralwidget)
        self.label_pembayaran.setGeometry(QtCore.QRect(210, 380, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_pembayaran.setFont(font)
        self.label_pembayaran.setObjectName("label_pembayaran")
        self.date_booking = QtWidgets.QDateEdit(self.centralwidget)
        self.date_booking.setGeometry(QtCore.QRect(210, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.date_booking.setFont(font)
        self.date_booking.setStyleSheet("background: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.date_booking.setObjectName("date_booking")
        self.line_nama_team = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nama_team.setGeometry(QtCore.QRect(210, 220, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.line_nama_team.setFont(font)
        self.line_nama_team.setStyleSheet("background: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.line_nama_team.setObjectName("line_nama_team")
        self.date_main = QtWidgets.QDateEdit(self.centralwidget)
        self.date_main.setGeometry(QtCore.QRect(390, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.date_main.setFont(font)
        self.date_main.setStyleSheet("background: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.date_main.setObjectName("date_main")
        self.spin_durasi = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_durasi.setGeometry(QtCore.QRect(480, 340, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.spin_durasi.setFont(font)
        self.spin_durasi.setStyleSheet("background: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.spin_durasi.setObjectName("spin_durasi")
        self.combo_pembayaran = QtWidgets.QComboBox(self.centralwidget)
        self.combo_pembayaran.setGeometry(QtCore.QRect(210, 400, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.combo_pembayaran.setFont(font)
        self.combo_pembayaran.setStyleSheet("background: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.combo_pembayaran.setObjectName("combo_pembayaran")
        self.combo_pembayaran.addItem("Belum")
        self.combo_pembayaran.addItem("Lunas")
        self.push_OK = QtWidgets.QPushButton(self.centralwidget)
        self.push_OK.setGeometry(QtCore.QRect(440, 480, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.push_OK.setFont(font)
        self.push_OK.setObjectName("push_OK")
        self.push_OK.clicked.connect(self.simpan)
        self.label_waktu_main = QtWidgets.QLabel(self.centralwidget)
        self.label_waktu_main.setGeometry(QtCore.QRect(210, 320, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_waktu_main.setFont(font)
        self.label_waktu_main.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_waktu_main.setObjectName("label_waktu_main")
        self.line_waktu_main = QtWidgets.QLineEdit(self.centralwidget)
        self.line_waktu_main.setGeometry(QtCore.QRect(210, 340, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.line_waktu_main.setFont(font)
        self.line_waktu_main.setStyleSheet("background: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.line_waktu_main.setObjectName("line_waktu_main")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUtama(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUtama(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_kita_soccer.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">KITA SOCCER</span></p></body></html>"))
        self.label_nama_team.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Nama Team</span></p></body></html>"))
        self.label_booking.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Tgl Booking</span></p></body></html>"))
        self.label_main.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Tgl Main</span></p></body></html>"))
        self.label_durasi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Durasi</span></p></body></html>"))
        self.label_pembayaran.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Pembayaran</span></p></body></html>"))
        self.line_nama_team.setText(_translate("MainWindow", "Nama Team"))
        self.combo_pembayaran.setItemText(0, _translate("MainWindow", "Belum"))
        self.combo_pembayaran.setItemText(1, _translate("MainWindow", "Lunas"))
        self.push_OK.setText(_translate("MainWindow", "OK"))
        self.label_waktu_main.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Waktu Main</span></p></body></html>"))
        self.line_waktu_main.setText(_translate("MainWindow", "Pukul"))


    def login(self):
        user = self.lineUser.text()
        pw = self.linePass.text()

        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "futsal"
        )

        mycursor = con.cursor()
        sql = "SELECT * FROM admin WHERE Username LIKE %s AND Password LIKE %s"
        val = ("%{}%".format(user), "%{}%".format(pw))
        mycursor.execute(sql, val)
        results = mycursor.fetchall()
  
        if mycursor.rowcount < 0:
            self.messagebox("Log In", "Log In GAGAL !")
        else:
            for data in results:
                 self.messagebox("Log In", "Log In SUKSES !")
                 self.setupUtama(MainWindow)

    def simpan(self):
        nama = self.line_nama_team.text()
        book = str(self.date_booking.date())
        books = str(book)
        main = str(self.date_main.date())
        mains = str(main)
        waktu = self.line_waktu_main.text()
        durasi = self.spin_durasi.text()
        status = self.combo_pembayaran.currentText()
        
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "futsal"
        )

        mycursor = con.cursor()
        sql = "INSERT INTO data(Nama_Team, Tgl_Boking, Tgl_Main, Waktu_Main, Durasi, Pembayaran) VALUES (%s,%s,%s,%s,%s,%s)"
        data = mycursor.execute(sql,(nama, books, mains, waktu, durasi, status))
        con.commit()        
        if(con.commit()):
            self.messagebox("GAGAL", "Data Futsal Tidak Tersimpan")
        else:
            self.messagebox("SUKSES", "Data Futsal Tersimpan")
            print(books, mains)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_background1.setText(_translate("MainWindow", ""))
        self.label_background2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineUser.setText(_translate("MainWindow", "Username"))
        self.label_logo_pass.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.linePass.setText(_translate("MainWindow", "Password"))
        self.label_login.setText(_translate("MainWindow", "LOGIN"))
        self.push_OK.setText(_translate("MainWindow", "OK"))

#import test1_rc
#import test2_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

