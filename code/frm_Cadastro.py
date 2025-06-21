from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget, QMessageBox)

import controle
import mysql.connector
import pandas

class Ui_frm_Cadastro(object):
    def setupUi(self, frm_Cadastro):
        if not frm_Cadastro.objectName():
            frm_Cadastro.setObjectName(u"frm_Cadastro")
        frm_Cadastro.resize(676, 676)
        frm_Cadastro.setStyleSheet(u"QWidget{\n"
"	background: #0033A0;\n"
"}")
        self.lbl_bairro = QLabel(frm_Cadastro)
        self.lbl_bairro.setObjectName(u"lbl_bairro")
        self.lbl_bairro.setGeometry(QRect(-360, 250, 121, 41))
        self.lbl_bairro.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_6 = QLabel(frm_Cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-370, 440, 371, 41))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas = QLabel(frm_Cadastro)
        self.lbl_coordernadas.setObjectName(u"lbl_coordernadas")
        self.lbl_coordernadas.setGeometry(QRect(-360, 110, 311, 41))
        self.lbl_coordernadas.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_bairro = QLineEdit(frm_Cadastro)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(-240, 240, 181, 51))
        self.txt_bairro.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_log = QLabel(frm_Cadastro)
        self.lbl_log.setObjectName(u"lbl_log")
        self.lbl_log.setGeometry(QRect(-360, 180, 121, 41))
        self.lbl_log.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.groupBox_2 = QGroupBox(frm_Cadastro)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(-360, 490, 251, 81))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #4DA8DA;\n"
"    border-radius: 8px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #FFFFFF; \n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"}\n"
"r")
        self.radio_sim1 = QRadioButton(self.groupBox_2)
        self.radio_sim1.setObjectName(u"radio_sim1")
        self.radio_sim1.setGeometry(QRect(20, 40, 91, 23))
        self.radio_sim1.setStyleSheet(u"QRadioButton {\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6;  /* Azul moderno e suave */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"")
        self.radio_nao2 = QRadioButton(self.groupBox_2)
        self.radio_nao2.setObjectName(u"radio_nao2")
        self.radio_nao2.setGeometry(QRect(150, 40, 91, 23))
        self.radio_nao2.setStyleSheet(u"QRadioButton {\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6;  /* Azul moderno e suave */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"")
        self.btn_continuar = QPushButton(frm_Cadastro)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setGeometry(QRect(190, 580, 321, 61))
        self.btn_continuar.setStyleSheet(u"QPushButton {\n"
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
"}r")
        self.lbl_bairro_2 = QLabel(frm_Cadastro)
        self.lbl_bairro_2.setObjectName(u"lbl_bairro_2")
        self.lbl_bairro_2.setGeometry(QRect(10, 230, 121, 41))
        self.lbl_bairro_2.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_7 = QLabel(frm_Cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 420, 371, 41))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_2 = QLabel(frm_Cadastro)
        self.lbl_coordernadas_2.setObjectName(u"lbl_coordernadas_2")
        self.lbl_coordernadas_2.setGeometry(QRect(0, 90, 311, 41))
        self.lbl_coordernadas_2.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_numeroMoradores = QLineEdit(frm_Cadastro)
        self.txt_numeroMoradores.setObjectName(u"txt_numeroMoradores")
        self.txt_numeroMoradores.setGeometry(QRect(370, 410, 71, 51))
        self.txt_numeroMoradores.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.label_8 = QLabel(frm_Cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 500, 221, 41))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.groupBox = QGroupBox(frm_Cadastro)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(370, 220, 261, 80))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #4DA8DA;\n"
"    border-radius: 8px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #FFFFFF; \n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"}\n"
"r")
        self.radio_sim = QRadioButton(self.groupBox)
        self.radio_sim.setObjectName(u"radio_sim")
        self.radio_sim.setGeometry(QRect(20, 40, 91, 23))
        self.radio_sim.setStyleSheet(u"QRadioButton {\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6;  /* Azul moderno e suave */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"")
        self.radio_nao = QRadioButton(self.groupBox)
        self.radio_nao.setObjectName(u"radio_nao")
        self.radio_nao.setGeometry(QRect(150, 40, 91, 23))
        self.radio_nao.setStyleSheet(u"QRadioButton {\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6;  /* Azul moderno e suave */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"")
        self.txt_coordenadas = QLineEdit(frm_Cadastro)
        self.txt_coordenadas.setObjectName(u"txt_coordenadas")
        self.txt_coordenadas.setGeometry(QRect(320, 80, 331, 51))
        self.txt_coordenadas.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_numero = QLabel(frm_Cadastro)
        self.lbl_numero.setObjectName(u"lbl_numero")
        self.lbl_numero.setGeometry(QRect(430, 160, 81, 41))
        self.lbl_numero.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_quantidadeCrianca = QLineEdit(frm_Cadastro)
        self.txt_quantidadeCrianca.setObjectName(u"txt_quantidadeCrianca")
        self.txt_quantidadeCrianca.setGeometry(QRect(510, 490, 61, 51))
        self.txt_quantidadeCrianca.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.txt_bairro_2 = QLineEdit(frm_Cadastro)
        self.txt_bairro_2.setObjectName(u"txt_bairro_2")
        self.txt_bairro_2.setGeometry(QRect(130, 220, 181, 51))
        self.txt_bairro_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.label_9 = QLabel(frm_Cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 681, 41))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_log_2 = QLabel(frm_Cadastro)
        self.lbl_log_2.setObjectName(u"lbl_log_2")
        self.lbl_log_2.setGeometry(QRect(0, 160, 121, 41))
        self.lbl_log_2.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_10 = QLabel(frm_Cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 330, 681, 41))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_log = QLineEdit(frm_Cadastro)
        self.txt_log.setObjectName(u"txt_log")
        self.txt_log.setGeometry(QRect(120, 150, 291, 51))
        self.txt_log.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.txt_numero = QLineEdit(frm_Cadastro)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setGeometry(QRect(510, 150, 101, 51))
        self.txt_numero.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.groupBox_3 = QGroupBox(frm_Cadastro)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 470, 251, 81))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #4DA8DA;\n"
"    border-radius: 8px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #FFFFFF; \n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"}\n"
"r")
        self.radio_sim1_2 = QRadioButton(self.groupBox_3)
        self.radio_sim1_2.setObjectName(u"radio_sim1_2")
        self.radio_sim1_2.setGeometry(QRect(20, 40, 91, 23))
        self.radio_sim1_2.setStyleSheet(u"QRadioButton {\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6;  /* Azul moderno e suave */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"")
        self.radio_nao2_2 = QRadioButton(self.groupBox_3)
        self.radio_nao2_2.setObjectName(u"radio_nao2_2")
        self.radio_nao2_2.setGeometry(QRect(150, 40, 91, 23))
        self.radio_nao2_2.setStyleSheet(u"QRadioButton {\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 7px;\n"
"    border: 1px solid #CCCCCC;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6;  /* Azul moderno e suave */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"")

        self.retranslateUi(frm_Cadastro)

        QMetaObject.connectSlotsByName(frm_Cadastro)
    # setupUi

    def register_home(self):
        campos_inteiros = {
            "Número": self.txt_numero.text().strip(),
            "Número-Moradores": self.txt_numeroMoradores.text().strip(),
            "Quantidade-de-Crianças": self.txt_quantidadeCrianca.text().strip(),
        }
        campos_texto = {
            "Coordenadas": self.txt_coordenadas.text().strip(),
            "Logradouro": self.txt_log.text().strip(),
            "Bairro": self.txt_bairro_2.text().strip(),
            "Habitada": "Sim" if self.radio_sim.isChecked() else "Não" if self.radio_nao.isChecked() else "",
            "Crianças": self.radio_sim1_2.text().strip(),
            "Crianças": self.radio_nao2_2.text().strip(),
        }

        for campo, preenchido in campos_inteiros.items():
            if not preenchido.strip():
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"O campo '{campos_inteiros} é obrigatório, e não pode ficar vazio!' ")
                icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                msg.setWindowIcon(QIcon(icon_path)) 
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        
        for campo, preenchidos in campos_texto.items():
            if not preenchido.strip():
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText(f"O campo '{campos_texto} é obrigatório, e não pode ficar vazio!' ")
                icon_path = r"C:\Users\Ariel\PycharmProjects\Scripts\Sistema\avsIcon.png"
                msg.setWindowIcon(QIcon(icon_path)) 
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return
        
        coordenadas = self.txt_coordenadas.text()
        logradouro = self.txt_log.text()
        numeroResidencial = self.txt_numero.text()
        bairro = self.txt_bairro_2.text()
        habitacao = "Sim" if self.radio_sim else "Não"
        crianca = "Sim" if self.radio_sim1_2 else "Não"
        numeroMoradores = self.txt_numeroMoradores.text()
        quantidadeCrianca = self.txt_quantidadeCrianca.text()

        mydb = mysql.connector.connect(
            host = controle.host,
            user = controle.user,
            password = controle.password,
            database = controle.database
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO cadastroMorades(`Coordenadas`, `Logradouro`, `Número`, `Bairro`, `Habitada`, `Número-Moradores`, `Crianças`, `Quantidade-Crianças`) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (
                coordenadas,
                logradouro,
                numeroResidencial,
                bairro,
                habitacao,
                numeroMoradores,
                crianca,
                quantidadeCrianca
        )
        mycursor.execute(sql, valores   )
        mydb.commit()
        print(mycursor.rowcount, 'Record(s) inserted')
        mycursor.close()

        print("ok")


    def retranslateUi(self, frm_Cadastro):
        frm_Cadastro.setWindowTitle(QCoreApplication.translate("frm_Cadastro", u"Cadastro", None))
        self.lbl_bairro.setText(QCoreApplication.translate("frm_Cadastro", u"Bairro:", None))
        self.label_6.setText(QCoreApplication.translate("frm_Cadastro", u"N\u00famero total de moradores na resid\u00eancia:", None))
        self.lbl_coordernadas.setText(QCoreApplication.translate("frm_Cadastro", u"Coordenadas - latitude e longitude):", None))
        self.lbl_log.setText(QCoreApplication.translate("frm_Cadastro", u"Logradouro:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("frm_Cadastro", u"H\u00e1 crian\u00e7as na resid\u00eancia?", None))
        self.radio_sim1.setText(QCoreApplication.translate("frm_Cadastro", u"Sim", None))
        self.radio_nao2.setText(QCoreApplication.translate("frm_Cadastro", u"N\u00e3o", None))
        self.btn_continuar.setText(QCoreApplication.translate("frm_Cadastro", u"Cadastrar Moradores", None))
        self.lbl_bairro_2.setText(QCoreApplication.translate("frm_Cadastro", u"Bairro:", None))
        self.label_7.setText(QCoreApplication.translate("frm_Cadastro", u"N\u00famero total de moradores na resid\u00eancia:", None))
        self.lbl_coordernadas_2.setText(QCoreApplication.translate("frm_Cadastro", u"Coordenadas - latitude e longitude):", None))
        self.label_8.setText(QCoreApplication.translate("frm_Cadastro", u"Se sim, quantas crian\u00e7as?", None))
        self.groupBox.setTitle(QCoreApplication.translate("frm_Cadastro", u"A resid\u00eancia est\u00e1 habitada?", None))
        self.radio_sim.setText(QCoreApplication.translate("frm_Cadastro", u"Sim", None))
        self.radio_nao.setText(QCoreApplication.translate("frm_Cadastro", u"N\u00e3o", None))
        self.lbl_numero.setText(QCoreApplication.translate("frm_Cadastro", u"N\u00famero:", None))
        self.txt_quantidadeCrianca.setText(QCoreApplication.translate("frm_Cadastro", u"0", None))
        self.label_9.setText(QCoreApplication.translate("frm_Cadastro", u"1. Informa\u00e7\u00f5es Gerais sobre a Resid\u00eancia:", None))
        self.lbl_log_2.setText(QCoreApplication.translate("frm_Cadastro", u"Logradouro:", None))
        self.label_10.setText(QCoreApplication.translate("frm_Cadastro", u"2. Composi\u00e7\u00e3o Familiar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("frm_Cadastro", u"H\u00e1 crian\u00e7as na resid\u00eancia?", None))
        self.radio_sim1_2.setText(QCoreApplication.translate("frm_Cadastro", u"Sim", None))
        self.radio_nao2_2.setText(QCoreApplication.translate("frm_Cadastro", u"N\u00e3o", None))
    # retranslateUi
        self.btn_continuar.clicked.connect(self.register_home)

if __name__ == "__main__":
    app = QApplication([])
    frm_Cadastro = QWidget()
    ui = Ui_frm_Cadastro()
    ui.setupUi(frm_Cadastro)
    frm_Cadastro.show()
    app.exec()  