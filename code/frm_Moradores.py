from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget, QMessageBox)

import pymysql
import pandas as pd
import controle

class Ui_frm_Moradores(object):
    def setupUi(self, frm_Moradores):
        if not frm_Moradores.objectName():
            frm_Moradores.setObjectName(u"frm_Moradores")
        frm_Moradores.setFixedSize(1061, 708)
        self.frm_Moradores = frm_Moradores
        frm_Moradores.setStyleSheet(u"QWidget{\n"
"	background: #0033A0;\n"
"}")
        self.label_9 = QLabel(frm_Moradores)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 1061, 41))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_Nome = QLineEdit(frm_Moradores)
        self.txt_Nome.setObjectName(u"txt_Nome")
        self.txt_Nome.setGeometry(QRect(170, 120, 331, 51))
        self.txt_Nome.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_2 = QLabel(frm_Moradores)
        self.lbl_coordernadas_2.setObjectName(u"lbl_coordernadas_2")
        self.lbl_coordernadas_2.setGeometry(QRect(20, 130, 151, 41))
        self.lbl_coordernadas_2.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_10 = QLabel(frm_Moradores)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 70, 311, 41))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_idade = QLineEdit(frm_Moradores)
        self.txt_idade.setObjectName(u"txt_idade")
        self.txt_idade.setGeometry(QRect(90, 190, 61, 51))
        self.txt_idade.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_3 = QLabel(frm_Moradores)
        self.lbl_coordernadas_3.setObjectName(u"lbl_coordernadas_3")
        self.lbl_coordernadas_3.setGeometry(QRect(20, 200, 71, 41))
        self.lbl_coordernadas_3.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_email = QLineEdit(frm_Moradores)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(240, 190, 261, 51))
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_4 = QLabel(frm_Moradores)
        self.lbl_coordernadas_4.setObjectName(u"lbl_coordernadas_4")
        self.lbl_coordernadas_4.setGeometry(QRect(160, 200, 91, 41))
        self.lbl_coordernadas_4.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_5 = QLabel(frm_Moradores)
        self.lbl_coordernadas_5.setObjectName(u"lbl_coordernadas_5")
        self.lbl_coordernadas_5.setGeometry(QRect(20, 270, 161, 41))
        self.lbl_coordernadas_5.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_Contato = QLineEdit(frm_Moradores)
        self.txt_Contato.setObjectName(u"txt_Contato")
        self.txt_Contato.setGeometry(QRect(190, 260, 261, 51))
        self.txt_Contato.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_6 = QLabel(frm_Moradores)
        self.lbl_coordernadas_6.setObjectName(u"lbl_coordernadas_6")
        self.lbl_coordernadas_6.setGeometry(QRect(20, 330, 91, 41))
        self.lbl_coordernadas_6.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.comboBox = QComboBox(frm_Moradores)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 330, 261, 41))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #888;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    selection-background-color: #4CAF50;\n"
"    selection-color: #9C27B0;\n"
"    border: 1px solid #aaa;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.lbl_coordernadas_7 = QLabel(frm_Moradores)
        self.lbl_coordernadas_7.setObjectName(u"lbl_coordernadas_7")
        self.lbl_coordernadas_7.setGeometry(QRect(20, 650, 91, 41))
        self.lbl_coordernadas_7.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_Nome1 = QLineEdit(frm_Moradores)
        self.txt_Nome1.setObjectName(u"txt_Nome1")
        self.txt_Nome1.setGeometry(QRect(170, 440, 331, 51))
        self.txt_Nome1.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_8 = QLabel(frm_Moradores)
        self.lbl_coordernadas_8.setObjectName(u"lbl_coordernadas_8")
        self.lbl_coordernadas_8.setGeometry(QRect(160, 520, 91, 41))
        self.lbl_coordernadas_8.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_idade1 = QLineEdit(frm_Moradores)
        self.txt_idade1.setObjectName(u"txt_idade1")
        self.txt_idade1.setGeometry(QRect(90, 510, 61, 51))
        self.txt_idade1.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_9 = QLabel(frm_Moradores)
        self.lbl_coordernadas_9.setObjectName(u"lbl_coordernadas_9")
        self.lbl_coordernadas_9.setGeometry(QRect(20, 520, 71, 41))
        self.lbl_coordernadas_9.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_10 = QLabel(frm_Moradores)
        self.lbl_coordernadas_10.setObjectName(u"lbl_coordernadas_10")
        self.lbl_coordernadas_10.setGeometry(QRect(20, 590, 161, 41))
        self.lbl_coordernadas_10.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.comboBox_2 = QComboBox(frm_Moradores)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(120, 650, 261, 41))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #888;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    selection-background-color: #4CAF50;\n"
"    selection-color: #9C27B0;\n"
"    border: 1px solid #aaa;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.txt_email1 = QLineEdit(frm_Moradores)
        self.txt_email1.setObjectName(u"txt_email1")
        self.txt_email1.setGeometry(QRect(240, 510, 261, 51))
        self.txt_email1.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_11 = QLabel(frm_Moradores)
        self.lbl_coordernadas_11.setObjectName(u"lbl_coordernadas_11")
        self.lbl_coordernadas_11.setGeometry(QRect(20, 450, 151, 41))
        self.lbl_coordernadas_11.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_11 = QLabel(frm_Moradores)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 390, 141, 41))
        self.label_11.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_contato1 = QLineEdit(frm_Moradores)
        self.txt_contato1.setObjectName(u"txt_contato1")
        self.txt_contato1.setGeometry(QRect(190, 580, 261, 51))
        self.txt_contato1.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.btn_cadastrarM = QPushButton(frm_Moradores)
        self.btn_cadastrarM.setObjectName(u"btn_cadastrarM")
        self.btn_cadastrarM.setGeometry(QRect(660, 500, 300, 61))
        self.btn_cadastrarM.setStyleSheet(u"QPushButton {\n"
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
        self.lbl_coordernadas_12 = QLabel(frm_Moradores)
        self.lbl_coordernadas_12.setObjectName(u"lbl_coordernadas_12")
        self.lbl_coordernadas_12.setGeometry(QRect(540, 330, 91, 41))
        self.lbl_coordernadas_12.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_13 = QLabel(frm_Moradores)
        self.lbl_coordernadas_13.setObjectName(u"lbl_coordernadas_13")
        self.lbl_coordernadas_13.setGeometry(QRect(700, 200, 91, 41))
        self.lbl_coordernadas_13.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_14 = QLabel(frm_Moradores)
        self.lbl_coordernadas_14.setObjectName(u"lbl_coordernadas_14")
        self.lbl_coordernadas_14.setGeometry(QRect(540, 200, 71, 41))
        self.lbl_coordernadas_14.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_15 = QLabel(frm_Moradores)
        self.lbl_coordernadas_15.setObjectName(u"lbl_coordernadas_15")
        self.lbl_coordernadas_15.setGeometry(QRect(550, 270, 161, 41))
        self.lbl_coordernadas_15.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_contato2 = QLineEdit(frm_Moradores)
        self.txt_contato2.setObjectName(u"txt_contato2")
        self.txt_contato2.setGeometry(QRect(720, 260, 261, 51))
        self.txt_contato2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.txt_idade2 = QLineEdit(frm_Moradores)
        self.txt_idade2.setObjectName(u"txt_idade2")
        self.txt_idade2.setGeometry(QRect(630, 190, 61, 51))
        self.txt_idade2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.label_12 = QLabel(frm_Moradores)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(540, 70, 141, 41))
        self.label_12.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.comboBox_3 = QComboBox(frm_Moradores)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(660, 330, 261, 41))
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #888;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"	color: #000000;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #aaa;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    selection-background-color: #4CAF50;\n"
"    selection-color: #9C27B0;\n"
"    border: 1px solid #aaa;\n"
"    padding: 4px;\n"
"    font-size: 13px;\n"
"}\n"
"")
        self.txt_Nome_2 = QLineEdit(frm_Moradores)
        self.txt_Nome_2.setObjectName(u"txt_Nome_2")
        self.txt_Nome_2.setGeometry(QRect(690, 120, 331, 51))
        self.txt_Nome_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.txt_email2 = QLineEdit(frm_Moradores)
        self.txt_email2.setObjectName(u"txt_email2")
        self.txt_email2.setGeometry(QRect(780, 190, 261, 51))
        self.txt_email2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_16 = QLabel(frm_Moradores)
        self.lbl_coordernadas_16.setObjectName(u"lbl_coordernadas_16")
        self.lbl_coordernadas_16.setGeometry(QRect(540, 130, 151, 41))
        self.lbl_coordernadas_16.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.line = QFrame(frm_Moradores)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(510, 60, 20, 641))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(frm_Moradores)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 380, 1061, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_Finalizar = QPushButton(frm_Moradores)
        self.btn_Finalizar.setObjectName(u"btn_Finalizar")
        self.btn_Finalizar.setGeometry(QRect(630, 580, 350, 61))
        self.btn_Finalizar.setStyleSheet(u"QPushButton {\n"
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
        self.line_3 = QFrame(frm_Moradores)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-3, 60, 1061, 20))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(frm_Moradores)

        QMetaObject.connectSlotsByName(frm_Moradores)
    # setupUi

    def cadastroMoradores(self):

        nome = self.txt_Nome.text().strip()
        idade = self.txt_idade.text().strip()
        email = self.txt_email.text().strip()
        contato = self.txt_Contato.text().strip()
        genero = self.comboBox.currentText().strip()

        campos = [nome, idade, email, contato, genero]

        #adiciona a lista cada campo preenchido em campos
        prenchidos = [campo for campo in campos if campo]

        if 0 < len(prenchidos) < len(campos):
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"Preencha todos os campos de morador 1")
                icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                msg.setWindowIcon(QIcon(icon_path)) 
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        
        
        nome1 = self.txt_Nome1.text()
        idade1 = self.txt_idade1.text()
        email1 = self.txt_email1.text()
        contato1 = self.txt_contato1.text()
        genero1 = self.comboBox_2.itemText()

        campos1 = [nome1, idade1, email1, contato1, genero1]

        preenchidos1 = [campos1 for campo in campos1 if campo]

        if 0 < len(preenchidos1) < len(campos1):
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"Preencha todos os campos de morador 2")
                icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                msg.setWindowIcon(QIcon(icon_path)) 
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return


        nome2 = self.txt_Nome_2.text()
        idade2 = self.txt_idade2.text()
        email2 = self.txt_email2.text()
        contato2 = self.txt_contato2.text()
        genero2 = self.comboBox_2.itemText()

        campos2 = [nome2, idade2, email2, contato2, genero2]

        prenchidos = [campos2 for campo in campos2 if campo]

        if 0 < len(preenchidos1) < len(campos2):
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"Preencha todos os campos de morador 3")
                icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                msg.setWindowIcon(QIcon(icon_path)) 
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return


    def retranslateUi(self, frm_Moradores):
        frm_Moradores.setWindowTitle(QCoreApplication.translate("frm_Moradores", u"Cadastro Moradores", None))
        self.label_9.setText(QCoreApplication.translate("frm_Moradores", u"2. Moradores", None))
        self.lbl_coordernadas_2.setText(QCoreApplication.translate("frm_Moradores", u"Nome completo:", None))
        self.label_10.setText(QCoreApplication.translate("frm_Moradores", u"Morador 1 (Respons\u00e1vel):", None))
        self.lbl_coordernadas_3.setText(QCoreApplication.translate("frm_Moradores", u"Idade:", None))
        self.lbl_coordernadas_4.setText(QCoreApplication.translate("frm_Moradores", u"E-mail:", None))
        self.lbl_coordernadas_5.setText(QCoreApplication.translate("frm_Moradores", u"Telefone(contato):", None))
        self.txt_Contato.setInputMask(QCoreApplication.translate("frm_Moradores", u"(00) 0 0000-0000", None))
        self.lbl_coordernadas_6.setText(QCoreApplication.translate("frm_Moradores", u"G\u00eanero:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("frm_Moradores", u"Masculino", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("frm_Moradores", u"Feminino", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("frm_Moradores", u"Prefiro n\u00e3o responder", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("frm_Moradores", u"Outro", None))

        self.lbl_coordernadas_7.setText(QCoreApplication.translate("frm_Moradores", u"G\u00eanero:", None))
        self.lbl_coordernadas_8.setText(QCoreApplication.translate("frm_Moradores", u"E-mail:", None))
        self.lbl_coordernadas_9.setText(QCoreApplication.translate("frm_Moradores", u"Idade:", None))
        self.lbl_coordernadas_10.setText(QCoreApplication.translate("frm_Moradores", u"Telefone(contato):", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("frm_Moradores", u"Masculino", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("frm_Moradores", u"Feminino", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("frm_Moradores", u"Prefiro n\u00e3o responder", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("frm_Moradores", u"Outro", None))

        self.lbl_coordernadas_11.setText(QCoreApplication.translate("frm_Moradores", u"Nome completo:", None))
        self.label_11.setText(QCoreApplication.translate("frm_Moradores", u"Morador 2:", None))
        self.txt_contato1.setInputMask(QCoreApplication.translate("frm_Moradores", u"(00) 0 0000-0000", None))
        self.btn_cadastrarM.setText(QCoreApplication.translate("frm_Moradores", u"Cadastrar mais moradores", None))
        self.lbl_coordernadas_12.setText(QCoreApplication.translate("frm_Moradores", u"G\u00eanero:", None))
        self.lbl_coordernadas_13.setText(QCoreApplication.translate("frm_Moradores", u"E-mail:", None))
        self.lbl_coordernadas_14.setText(QCoreApplication.translate("frm_Moradores", u"Idade:", None))
        self.lbl_coordernadas_15.setText(QCoreApplication.translate("frm_Moradores", u"Telefone(contato):", None))
        self.txt_contato2.setInputMask(QCoreApplication.translate("frm_Moradores", u"(00) 0 0000-0000", None))
        self.label_12.setText(QCoreApplication.translate("frm_Moradores", u"Morador 3:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("frm_Moradores", u"Masculino", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("frm_Moradores", u"Feminino", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("frm_Moradores", u"Prefiro n\u00e3o responder", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("frm_Moradores", u"Outro", None))

        self.lbl_coordernadas_16.setText(QCoreApplication.translate("frm_Moradores", u"Nome completo:", None))
        self.btn_Finalizar.setText(QCoreApplication.translate("frm_Moradores", u"Finalizar cadastro de moradores", None))
    # retranslateUi
        self.btn_cadastrarM.clicked.connect(self.cadastroMoradores)

if __name__ == "__main__":
    app = QApplication([])
    frm_Moradores = QWidget()
    ui = Ui_frm_Moradores()
    ui.setupUi(frm_Moradores)
    frm_Moradores.show()
    app.exec()  