from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget, QMessageBox)
from frm_ConsultarPorNome import Ui_frm_ConsultarPorNome

import pandas as pd
import controle
import pymysql
import requests
import json

class Ui_frm_VerCadastros(object):
    def setupUi(self, frm_VerCadastros):
        if not frm_VerCadastros.objectName():
            frm_VerCadastros.setObjectName(u"frm_VerCadastros")
        frm_VerCadastros.setFixedSize(884, 575)
        self.frm_VerCadastros = frm_VerCadastros
        frm_VerCadastros.setStyleSheet(u"QWidget{\n"
"	background: #0033A0;\n"
"}")
        self.tableWidget = QTableWidget(frm_VerCadastros)
        if (self.tableWidget.columnCount() < 20):
            self.tableWidget.setColumnCount(20)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 100, 841, 331))
        self.tableWidget.setStyleSheet(u"QTableWidget, QTableView {\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 5px; \n"
"    gridline-color: #dcdcdc; \n"
"    background-color: #ffffff; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; \n"
"    color: #333333;\n"
"    font-weight: bold; \n"
"    border: 1px solid #dcdcdc; \n"
"    padding: 4px; \n"
"}\n"
"\n"
"QTableWidget::item:selected, QTableView::item:selected {\n"
"    background-color: #b3d9ff; \n"
"    color: #000000;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f0f0f0; \n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #f0f0f0;\n"
"    width: 12px; \n"
"    margin: 2px 0 2px 0; \n"
"    border: none; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #b0bec5; \n"
"    min-height: 20px; \n"
"    border-radius: 6px; \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar:"
                        ":add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; \n"
"    height: 0px; \n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; \n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #f0f0f0; \n"
"    height: 12px; \n"
"    margin: 0 2px 0 2px; \n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #b0bec5;\n"
"    min-width: 20px; \n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #90a4ae; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.pushButton_3 = QPushButton(frm_VerCadastros)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(550, 460, 231, 61))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
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
        self.label = QLabel(frm_VerCadastros)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 841, 61))
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
        self.pushButton_4 = QPushButton(frm_VerCadastros)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(330, 460, 181, 61))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_5 = QPushButton(frm_VerCadastros)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(110, 460, 181, 61))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
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
"    background-color: #ffcdd2;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e57373;\n"
"\n"
"}")

        self.retranslateUi(frm_VerCadastros)

        QMetaObject.connectSlotsByName(frm_VerCadastros)
    # setupUi

    def tabela(self):
        mydb = pymysql.connect(
            host=controle.host,
            user=controle.user,
            password=controle.password,
            database=controle.database,
        )

        mycursor = mydb.cursor()

        querySQL = "SELECT * FROM cadastroGeral"

        mycursor.execute(querySQL)
        myresult = mycursor.fetchall()

        df = pd.DataFrame(
            myresult,
            columns=["Id", "Coordenadas", "CoordenadasM", "Nome", "Idade", "Gênero", "Telefone", "E-mail", "Logradouro", "Número", "Bairro", "Habitada", " Número-Moradores", "Crianças", "Quantidade-Crianças", "Mobilidade", "Quantidade", "Tipo(s)", "Internet", "Televisão", "Rádio"]   
        )
        self.all_data = df

        numRows, numCols = self.all_data.shape
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i, row in enumerate(self.all_data.itertuples(index=False)):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i,j, QTableWidgetItem(str(value)))
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        mycursor.close()
        mydb.close()

    def consultarNome(self):
        if not hasattr(self, 'frm_ConsultarPorNome') or self.frm_ConsultarPorNome is None or not self.frm_ConsultarPorNome.isVisible():
            self.frm_ConsultarPorNome = QWidget()
            self.ui = Ui_frm_ConsultarPorNome()
            self.ui.setupUi(self.frm_ConsultarPorNome)

            self.frm_ConsultarPorNome.setAttribute(Qt.WA_DeleteOnClose)
            self.frm_ConsultarPorNome.destroyed.connect(lambda: setattr(self, 'frm_Cadastro', None))

            self.frm_ConsultarPorNome.show()        

        else:
        
            self.frm_ConsultarPorNome.raise_()
            self.frm_ConsultarPorNome.activateWindow()
        
    def close(self):
        self.frm_VerCadastros.close()

    def visualizar(self):
        line = self.tableWidget.currentRow()

        if line == -1:
            msg = QMessageBox()
            msg.setWindowTitle("ERRO!")
            msg.setText("Por favor, selecione um morador para visualizar.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return

        col_coordenadas = 2 
        item = self.tableWidget.item(line, col_coordenadas)

        if item:
            coords_text = item.text()
            print("Coordenadas lidas:", coords_text)

            try:
                valores = [float(v.strip()) for v in coords_text.split(",")]

                pontos = []
                for i in range(0, len(valores), 2):
                    pontos.append({"lat": valores[i], "lng": valores[i+1]})

                response = requests.post(
                    "http://localhost:5001/receber-coordenadas",
                    json={"pontos": pontos}
                )
                print("Pontos enviados para o Flask:", pontos)
                print("Resposta do Flask:", response.json())

            except Exception as e:
                print("Erro ao enviar coordenadas:", e)
        

    def retranslateUi(self, frm_VerCadastros):
        frm_VerCadastros.setWindowTitle(QCoreApplication.translate("frm_VerCadastros", u"Ver cadastros", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_VerCadastros", u"Coordenadas UTM", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_VerCadastros", u"Coordenadas ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_VerCadastros", u"Logradouro", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_VerCadastros", u"N\u00famero", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_VerCadastros", u"Bairro", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_VerCadastros", u"Habitada", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_VerCadastros", u"N\u00famero-Moradores", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_VerCadastros", u"Crian\u00e7as", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_VerCadastros", u"Quantidade-Crian\u00e7as", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("frm_VerCadastros", u"Nome", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("frm_VerCadastros", u"Idade", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("frm_VerCadastros", u"G\u00eanero", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("frm_VerCadastros", u"Telefone", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("frm_VerCadastros", u"E-mail", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("frm_VerCadastros", u"Mobilidade", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("frm_VerCadastros", u"Quantidade", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("frm_VerCadastros", u"Tipo", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("frm_VerCadastros", u"Internet", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("frm_VerCadastros", u"Televis\u00e3o", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("frm_VerCadastros", u"R\u00e1dio", None));
        self.pushButton_3.setText(QCoreApplication.translate("frm_VerCadastros", u"Pesquisar por nome", None))
        self.label.setText(QCoreApplication.translate("frm_VerCadastros", u"VISUALIZAR CADASTROS", None))
        self.pushButton_4.setText(QCoreApplication.translate("frm_VerCadastros", u"Visualizar", None))
        self.pushButton_5.setText(QCoreApplication.translate("frm_VerCadastros", u"Voltar", None))
    # retranslateUi
        self.tabela()
        #pushButton_3 PESQUISAR POR NOME
        self.pushButton_3.clicked.connect(self.consultarNome)
        self.pushButton_3.clicked.connect(self.close)
        #pushButton_4 VISUALIZAR
        self.pushButton_4.clicked.connect(self.visualizar)
        #pushButton_5 VOLTAR

if __name__ == "__main__":
    app = QApplication([])
    frm_VerCadastros = QWidget()
    ui = Ui_frm_VerCadastros()
    ui.setupUi(frm_VerCadastros)
    frm_VerCadastros.show()
    app.exec()  