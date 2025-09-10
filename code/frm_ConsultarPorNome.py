from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget, QMessageBox)
import pesquisar
import consultar

import controle
import pandas as pd
import pymysql
import requests
import json

class Ui_frm_ConsultarPorNome(object):
    def setupUi(self, frm_ConsultarPorNome):
        if not frm_ConsultarPorNome.objectName():
            frm_ConsultarPorNome.setObjectName(u"frm_ConsultarPorNome")
        frm_ConsultarPorNome.setFixedSize(581, 592)
        self.frm_ConsultarPorNome = frm_ConsultarPorNome
        frm_ConsultarPorNome.setStyleSheet(u"QWidget{\n"
"	background: #0033A0;\n"
"}")
        self.btn_consultar = QPushButton(frm_ConsultarPorNome)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setGeometry(QRect(490, 510, 91, 81))
        self.btn_consultar.setStyleSheet(u"QPushButton{\n"
"    background-color: #f5f5f5; \n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 10px; \n"
"    padding: 10px; \n"
"    color: #333333; \n"
"    font-size: 14px; \n"
"	background-image:url(:/consulta/consultar.png);\n"
"    background-repeat: no-repeat; \n"
"    background-position: center;\n"
"	transition: all 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #e0e0e0; \n"
"    border-color: #aaaaaa;\n"
"	transform: scale(1.05); \n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #d6d6d6;\n"
"	border-color: #888888;\n"
"	transform: scale(0.95);\n"
"}")
        self.btn_pesquisar = QPushButton(frm_ConsultarPorNome)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setGeometry(QRect(550, 110, 21, 21))
        self.btn_pesquisar.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff; \n"
"    border: 2px solid #d1c4b2; \n"
"    border-radius: 12px;\n"
"    color: #5a5a5a; \n"
"    font-size: 14px;\n"
"    font-weight: bold; \n"
"    padding: 10px 16px;\n"
"    background-image:url(:/pesquisa/pesquisar.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    transition: all 0.3s ease; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f2ebe0; \n"
"    border-color: #c4b49e;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e8dfcf;\n"
"    border-color: #b39b8d; \n"
"    padding-left: 12px; \n"
"    padding-top: 4px;\n"
"}")
        self.lbl_nomeCliente = QLabel(frm_ConsultarPorNome)
        self.lbl_nomeCliente.setObjectName(u"lbl_nomeCliente")
        self.lbl_nomeCliente.setGeometry(QRect(0, 110, 241, 21))
        font = QFont()
        font.setBold(True)
        self.lbl_nomeCliente.setFont(font)
        self.lbl_nomeCliente.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nomeMorador = QLineEdit(frm_ConsultarPorNome)
        self.txt_nomeMorador.setObjectName(u"txt_nomeMorador")
        self.txt_nomeMorador.setGeometry(QRect(250, 100, 291, 41))
        font1 = QFont()
        self.txt_nomeMorador.setFont(font1)
        self.txt_nomeMorador.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    color: #000000;\n"
"    padding: 6px; \n"
"    font-size: 14px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.label = QLabel(frm_ConsultarPorNome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-30, 10, 661, 61))
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
        self.tableWidget = QTableWidget(frm_ConsultarPorNome)
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
        self.tableWidget.setGeometry(QRect(0, 160, 581, 331))
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

        self.retranslateUi(frm_ConsultarPorNome)

        QMetaObject.connectSlotsByName(frm_ConsultarPorNome)
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
            columns=["Id", "Coordenadas", "CoordenadasM", "Nome", "Idade", "Gênero", "Telefone", "E-mail", "Logradouro", "Número", "Complemento", "Bairro", "Habitada", " Número-Moradores", "Crianças", "Quantidade-Crianças", "Mobilidade", "Quantidade", "Tipo(s)", "Internet", "Televisão", "Rádio"]   
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

    def pesquisarPorNome(self):
        self.host = controle.host
        self.user = controle.user
        self.password = controle.password
        self.database = controle.database 
        print('Conectando...')
        mydb = pymysql.connect(
                host = controle.host,
                user = controle.user,
                password = controle.password,
                database = controle.database
        )
        print('Conexão bem-sucedida!')

        mycursor = mydb.cursor()

        nomeConsulta = self.txt_nomeMorador.text()
        consultaSQL = """SELECT * FROM cadastroGeral 
WHERE 
    Id LIKE %s OR
    Coordenadas LIKE %s OR
    CoordenadasM LIKE %s OR
    Nome LIKE %s OR
    Idade LIKE %s OR
    Gênero LIKE %s OR
    Telefone LIKE %s OR
    `E-mail` LIKE %s OR
    Logradouro LIKE %s OR
    Número LIKE %s OR
    Complemento LIKE %s OR
    Bairro LIKE %s OR
    Habitada LIKE %s OR
    `Número-Moradores` LIKE %s OR
    Crianças LIKE %s OR
    `Quantidade-Crianças` LIKE %s OR
    Mobilidade LIKE %s OR
    Quantidade LIKE %s OR
    `Tipo(s)` LIKE %s OR
    Internet LIKE %s OR
    Televisão LIKE %s OR
    Rádio LIKE %s"""
        valores = tuple('%' + nomeConsulta + '%' for _ in range(22))  # repete para cada coluna
        mycursor.execute(consultaSQL, valores)

        myresult = mycursor.fetchall()

        df = pd.DataFrame(myresult, columns=["Id", "Coordenadas", "CoordenadasM", "Nome", "Idade", "Gênero", "Telefone", "E-mail", "Logradouro", "Número", "Complemento", "Bairro", "Habitada", "Número-Moradores", "Crianças", "Quantidade-Crianças", "Mobilidade", "Quantidade", "Tipo(s)", "Internet", "Televisão", "Rádio"])
        self.all_data = df

        numRows = len(self.all_data.index)
        numCols = len(self.all_data.columns)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(numRows):
                for j in range(numCols):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        mycursor.close()
    
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

    def retranslateUi(self, frm_ConsultarPorNome):
        frm_ConsultarPorNome.setWindowTitle(QCoreApplication.translate("frm_ConsultarPorNome", u"Consultar Morador por Nome", None))
        self.btn_consultar.setText("")
        self.btn_pesquisar.setText("")
        self.lbl_nomeCliente.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Nome do morador responsav\u00e9l:", None))
        self.label.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"PESQUISAR MORADOR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Coordenadas UTM", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Coordenadas ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Logradouro", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"N\u00famero", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Bairro", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Habitada", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"N\u00famero-Moradores", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Crian\u00e7as", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Quantidade-Crian\u00e7as", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Nome", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Idade", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"G\u00eanero", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Telefone", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"E-mail", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Mobilidade", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Quantidade", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Tipo", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Internet", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"Televis\u00e3o", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("frm_ConsultarPorNome", u"R\u00e1dio", None));
    # retranslateUi
        self.tabela()
        self.btn_pesquisar.clicked.connect(self.pesquisarPorNome)
        self.btn_consultar.clicked.connect(self.visualizar)
        self.pesquisarPorNome()

if __name__ == "__main__":
    app = QApplication([])
    frm_ConsultarPorNome = QWidget()
    ui = Ui_frm_ConsultarPorNome()
    ui.setupUi(frm_ConsultarPorNome)
    frm_ConsultarPorNome.show()
    app.exec()  