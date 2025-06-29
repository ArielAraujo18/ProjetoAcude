from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_frm_fimCadastro(object):
    def setupUi(self, frm_fimCadastro):
        if not frm_fimCadastro.objectName():
            frm_fimCadastro.setObjectName(u"frm_fimCadastro")
        frm_fimCadastro.setFixedSize(676, 733)
        frm_fimCadastro.setStyleSheet(u"QWidget{\n"
"	background: #0033A0;\n"
"}")
        self.label_9 = QLabel(frm_fimCadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 676, 41))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.lbl_coordernadas_2 = QLabel(frm_fimCadastro)
        self.lbl_coordernadas_2.setObjectName(u"lbl_coordernadas_2")
        self.lbl_coordernadas_2.setGeometry(QRect(20, 190, 211, 41))
        self.lbl_coordernadas_2.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.txt_coordenadas = QLineEdit(frm_fimCadastro)
        self.txt_coordenadas.setObjectName(u"txt_coordenadas")
        self.txt_coordenadas.setGeometry(QRect(240, 180, 81, 51))
        self.txt_coordenadas.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.btn_continuar = QPushButton(frm_fimCadastro)
        self.btn_continuar.setObjectName(u"btn_continuar")
        self.btn_continuar.setGeometry(QRect(160, 640, 351, 61))
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
        self.groupBox = QGroupBox(frm_fimCadastro)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 80, 431, 80))
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
        self.line = QFrame(frm_fimCadastro)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 50, 661, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.txt_coordenadas_2 = QLineEdit(frm_fimCadastro)
        self.txt_coordenadas_2.setObjectName(u"txt_coordenadas_2")
        self.txt_coordenadas_2.setGeometry(QRect(210, 250, 211, 51))
        self.txt_coordenadas_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;  \n"
"    color: #1E1E1E;             \n"
"    font-size: 16px;\n"
"    padding: 6px 10px;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.lbl_coordernadas_3 = QLabel(frm_fimCadastro)
        self.lbl_coordernadas_3.setObjectName(u"lbl_coordernadas_3")
        self.lbl_coordernadas_3.setGeometry(QRect(20, 260, 181, 41))
        self.lbl_coordernadas_3.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 18px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.label_10 = QLabel(frm_fimCadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 350, 676, 41))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;\n"
"    font-size: 26px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.line_2 = QFrame(frm_fimCadastro)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 400, 661, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(frm_fimCadastro)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 330, 661, 20))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.groupBox_2 = QGroupBox(frm_fimCadastro)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 430, 481, 80))
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
        self.radio_sim_3 = QRadioButton(self.groupBox_2)
        self.radio_sim_3.setObjectName(u"radio_sim_3")
        self.radio_sim_3.setGeometry(QRect(20, 40, 91, 23))
        self.radio_sim_3.setStyleSheet(u"QRadioButton {\n"
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
        self.radio_nao_3 = QRadioButton(self.groupBox_2)
        self.radio_nao_3.setObjectName(u"radio_nao_3")
        self.radio_nao_3.setGeometry(QRect(150, 40, 91, 23))
        self.radio_nao_3.setStyleSheet(u"QRadioButton {\n"
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
        self.groupBox_3 = QGroupBox(frm_fimCadastro)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 530, 261, 80))
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
        self.radio_sim_4 = QRadioButton(self.groupBox_3)
        self.radio_sim_4.setObjectName(u"radio_sim_4")
        self.radio_sim_4.setGeometry(QRect(20, 40, 91, 23))
        self.radio_sim_4.setStyleSheet(u"QRadioButton {\n"
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
        self.radio_nao_4 = QRadioButton(self.groupBox_3)
        self.radio_nao_4.setObjectName(u"radio_nao_4")
        self.radio_nao_4.setGeometry(QRect(150, 40, 91, 23))
        self.radio_nao_4.setStyleSheet(u"QRadioButton {\n"
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
        self.groupBox_4 = QGroupBox(frm_fimCadastro)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(310, 530, 311, 80))
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
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
        self.radio_sim_5 = QRadioButton(self.groupBox_4)
        self.radio_sim_5.setObjectName(u"radio_sim_5")
        self.radio_sim_5.setGeometry(QRect(20, 40, 91, 23))
        self.radio_sim_5.setStyleSheet(u"QRadioButton {\n"
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
        self.radio_nao_5 = QRadioButton(self.groupBox_4)
        self.radio_nao_5.setObjectName(u"radio_nao_5")
        self.radio_nao_5.setGeometry(QRect(150, 40, 91, 23))
        self.radio_nao_5.setStyleSheet(u"QRadioButton {\n"
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

        self.retranslateUi(frm_fimCadastro)

        QMetaObject.connectSlotsByName(frm_fimCadastro)
    # setupUi

    #def registroMobilidade(self):




    def retranslateUi(self, frm_fimCadastro):
        frm_fimCadastro.setWindowTitle(QCoreApplication.translate("frm_fimCadastro", u"Cadastro de mobilidade", None))
        self.label_9.setText(QCoreApplication.translate("frm_fimCadastro", u"3. Condi\u00e7\u00f5es especiais dos moradores", None))
        self.lbl_coordernadas_2.setText(QCoreApplication.translate("frm_fimCadastro", u"Se sim, quantas pessoas?", None))
        self.btn_continuar.setText(QCoreApplication.translate("frm_fimCadastro", u"Finalizar cadastro de resid\u00eancia", None))
        self.groupBox.setTitle(QCoreApplication.translate("frm_fimCadastro", u"Algum morador possui mobilidade reduzida?", None))
        self.radio_sim.setText(QCoreApplication.translate("frm_fimCadastro", u"Sim", None))
        self.radio_nao.setText(QCoreApplication.translate("frm_fimCadastro", u"N\u00e3o", None))
        self.txt_coordenadas_2.setText("")
        self.lbl_coordernadas_3.setText(QCoreApplication.translate("frm_fimCadastro", u"Tipo(s) de defici\u00eancia:", None))
        self.label_10.setText(QCoreApplication.translate("frm_fimCadastro", u"4. Meios de comunica\u00e7\u00e3o e acesso a informa\u00e7\u00e3o", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("frm_fimCadastro", u"Os moradores t\u00eam acesso \u00e0 internet na resid\u00eancia?", None))
        self.radio_sim_3.setText(QCoreApplication.translate("frm_fimCadastro", u"Sim", None))
        self.radio_nao_3.setText(QCoreApplication.translate("frm_fimCadastro", u"N\u00e3o", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("frm_fimCadastro", u"H\u00e1 televis\u00e3o na resid\u00eancia?", None))
        self.radio_sim_4.setText(QCoreApplication.translate("frm_fimCadastro", u"Sim", None))
        self.radio_nao_4.setText(QCoreApplication.translate("frm_fimCadastro", u"N\u00e3o", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("frm_fimCadastro", u"A resid\u00eancia tem acesso a r\u00e1dio?", None))
        self.radio_sim_5.setText(QCoreApplication.translate("frm_fimCadastro", u"Sim", None))
        self.radio_nao_5.setText(QCoreApplication.translate("frm_fimCadastro", u"N\u00e3o", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    frm_fimCadastro = QWidget()
    ui = Ui_frm_fimCadastro()
    ui.setupUi(frm_fimCadastro)
    frm_fimCadastro.show()
    app.exec()  