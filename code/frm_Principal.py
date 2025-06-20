from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from frm_Cadastro import Ui_frm_Cadastro
import main

import sys

import geotecSfundo
import prefeituraRodape

class Ui_frm_Principal(object):
    def setupUi(self, frm_Principal):
        if not frm_Principal.objectName():
            frm_Principal.setObjectName(u"frm_Principal")
        frm_Principal.setFixedSize(680, 673)
        frm_Principal.setStyleSheet(u"QMainWindow{\n"
"	background: #0033A0;\n"
"}")
        self.centralwidget = QWidget(frm_Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 661, 61))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #E0E7FF;\n"
"    font-size: 30px;\n"
"    font-weight: 700;\n"
"    font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 51, 160, 0.3), stop:1 rgba(0, 31, 112, 0.3));\n"
"    padding: 14px 24px;\n"
"    border-radius: 12px;\n"
"    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.4);\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 480, 681, 141))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-image:url(:/Rodape/logo-ouro-branco (1).png);\n"
"}")
        self.btn_visualizar = QPushButton(self.centralwidget)
        self.btn_visualizar.setObjectName(u"btn_visualizar")
        self.btn_visualizar.setGeometry(QRect(230, 390, 221, 61))
        self.btn_visualizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #E0E7FF;\n"
"    color: #0033A0;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;\n"
"    padding: 10px 22px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #C7D2FE;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A5B4FC;\n"
"}")
        self.btn_VerCadastros = QPushButton(self.centralwidget)
        self.btn_VerCadastros.setObjectName(u"btn_VerCadastros")
        self.btn_VerCadastros.setGeometry(QRect(480, 390, 191, 61))
        self.btn_VerCadastros.setStyleSheet(u"QPushButton {\n"
"    background-color: #E0E7FF;\n"
"    color: #0033A0;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;\n"
"    padding: 10px 22px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #C7D2FE;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #A5B4FC;\n"
"}")
        self.btn_cadastrar = QPushButton(self.centralwidget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(10, 390, 191, 61))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #E0E7FF;\n"
"    color: #0033A0;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;\n"
"    padding: 10px 22px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #C7D2FE;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #32CD32;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 70, 681, 311))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background-image:url(:/semFundo/Captura de tela de 2025-06-16 00-54-57 (1) (1).png);\n"
"	background-repeat: no-repeat;\n"
"  	background-position: center;\n"
"}")
        frm_Principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(frm_Principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 22))
        frm_Principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(frm_Principal)
        self.statusbar.setObjectName(u"statusbar")
        frm_Principal.setStatusBar(self.statusbar)

        self.retranslateUi(frm_Principal)

        QMetaObject.connectSlotsByName(frm_Principal)
    # setupUi

    def register(self):

        if not hasattr(self, 'frm_Cadastro') or self.frm_Cadastro is None or not self.frm_Cadastro.isVisible():
            self.frm_Cadastro = QWidget()
            self.ui = Ui_frm_Cadastro()
            self.ui.setupUi(self.frm_Cadastro)

            self.frm_Cadastro.setAttribute(Qt.WA_DeleteOnClose)
            self.frm_Cadastro.destroyed.connect(lambda: setattr(self, 'frm_Cadastro', None))

            self.frm_Cadastro.show()        

        else:
        
            self.frm_Cadastro.raise_()
            self.frm_Cadastro.activateWindow()
        
    def maps(self):
        self.app = QApplication
        self.window = QMainWindow()
        self.window.resize(800, 600)
        self.window.show()

    def retranslateUi(self, frm_Principal):
        frm_Principal.setWindowTitle(QCoreApplication.translate("frm_Principal", u"Tela Principal", None))
        self.label.setText(QCoreApplication.translate("frm_Principal", u"SEGURAN\u00c7A DO A\u00c7UDE", None))
        self.label_2.setText("")
        self.btn_visualizar.setText(QCoreApplication.translate("frm_Principal", u"VISUALIZAR MAPA", None))
        self.btn_VerCadastros.setText(QCoreApplication.translate("frm_Principal", u"Ver cadastros", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("frm_Principal", u"Cadastrar", None))
        self.label_3.setText("")
    # retranslateUi

        self.btn_cadastrar.clicked.connect(self.register)
        self.btn_cadastrar.clicked.connect(self.maps)
        self.btn_visualizar.clicked.connect(self.maps)

if __name__ == "__main__":
    app = QApplication([])
    frm_Principal = QMainWindow()
    ui = Ui_frm_Principal()
    ui.setupUi(frm_Principal)
    frm_Principal.show()
    app.exec()  