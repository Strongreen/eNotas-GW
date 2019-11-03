# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmitirNota.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from emitenota import notaFiscalServico

from PyQt5 import QtCore, QtGui, QtWidgets

NFS = notaFiscalServico()

class Ui_MainWindow(object):

    def Getinformation(self):

        idExterno = self.IDExterno_Led.text()
        nome = self.Nome_Led.text()
        email = self.Email_Led.text()
        telefone = self.Telefone_Led.text()
        cpfCnpj = self.CPFCNP_Led.text()
        uf = self.Estado_Led.text()
        cidade = self.CIdade_Led.text()
        logradouro = self.Logradouro_Led.text()
        numero = self.Numero_Led.text()
        complemento = self.Complemento_Led.text()
        bairro = self.Bairro_Led.text()
        cep = self.CEP_Led.text()
        descricao = self.DescricaoServico_Txed.toPlainText()
        aliquotaIss = self.Aliquota_Led.text()
        valorTotal = self.ValorTotal_Led.text()

        if self.AmbienteEmissao_Cbx.currentText() == "Homologação":
            ambienteEmissao = "Homologacao"
        else:
            ambienteEmissao = "Producao"
        if self.EnviaEmail_Cbx.currentText() == "Sim":
            enviarPorEmail = "true"
        else:
            enviarPorEmail = "false"
        if self.TipoPessoa_Cbx.currentText() == "Pessoa Fisica":
            tipoPessoa = "F"
        else:
            tipoPessoa = "J"
        if self.ISSRetidoFonte_Cbx.currentText() == "Sim":
            issRetidoFonte = "true"
        else:
            issRetidoFonte = "false"
        
        nfse = NFS.notaFiscalS(idExterno,ambienteEmissao, enviarPorEmail, tipoPessoa, nome, email, telefone, cpfCnpj, uf, cidade, logradouro, numero, complemento, bairro,cep, descricao, aliquotaIss, issRetidoFonte,valorTotal)
        NFS.Emite(nfse)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1061, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollContents = QtWidgets.QWidget()
        self.scrollContents.setGeometry(QtCore.QRect(0, 0, 1059, 649))
        self.scrollContents.setMaximumSize(QtCore.QSize(16777215, 1169))
        self.scrollContents.setObjectName("scrollContents")
        self.Cliente_lb = QtWidgets.QLabel(self.scrollContents)
        self.Cliente_lb.setGeometry(QtCore.QRect(220, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Cliente_lb.setFont(font)
        self.Cliente_lb.setObjectName("Cliente_lb")
        self.AmbienteEmissao_Cbx = QtWidgets.QComboBox(self.scrollContents)
        self.AmbienteEmissao_Cbx.setGeometry(QtCore.QRect(800, 480, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AmbienteEmissao_Cbx.setFont(font)
        self.AmbienteEmissao_Cbx.setObjectName("AmbienteEmissao_Cbx")
        self.AmbienteEmissao_Cbx.addItem("")
        self.AmbienteEmissao_Cbx.addItem("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 551, 591))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TipoPessoa_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TipoPessoa_Lb.setFont(font)
        self.TipoPessoa_Lb.setObjectName("TipoPessoa_Lb")
        self.verticalLayout_2.addWidget(self.TipoPessoa_Lb)
        self.nome_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nome_Lb.setFont(font)
        self.nome_Lb.setObjectName("nome_Lb")
        self.verticalLayout_2.addWidget(self.nome_Lb)
        self.email_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_Lb.setFont(font)
        self.email_Lb.setObjectName("email_Lb")
        self.verticalLayout_2.addWidget(self.email_Lb)
        self.Telefone_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Telefone_Lb.setFont(font)
        self.Telefone_Lb.setObjectName("Telefone_Lb")
        self.verticalLayout_2.addWidget(self.Telefone_Lb)
        self.CPFCNPJ_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CPFCNPJ_Lb.setFont(font)
        self.CPFCNPJ_Lb.setObjectName("CPFCNPJ_Lb")
        self.verticalLayout_2.addWidget(self.CPFCNPJ_Lb)
        self.Estado_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Estado_Lb.setFont(font)
        self.Estado_Lb.setObjectName("Estado_Lb")
        self.verticalLayout_2.addWidget(self.Estado_Lb)
        self.Cidade_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Cidade_Lb.setFont(font)
        self.Cidade_Lb.setObjectName("Cidade_Lb")
        self.verticalLayout_2.addWidget(self.Cidade_Lb)
        self.Logradouro_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Logradouro_Lb.setFont(font)
        self.Logradouro_Lb.setObjectName("Logradouro_Lb")
        self.verticalLayout_2.addWidget(self.Logradouro_Lb)
        self.Numero_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Numero_Lb.setFont(font)
        self.Numero_Lb.setObjectName("Numero_Lb")
        self.verticalLayout_2.addWidget(self.Numero_Lb)
        self.Complemento_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Complemento_Lb.setFont(font)
        self.Complemento_Lb.setObjectName("Complemento_Lb")
        self.verticalLayout_2.addWidget(self.Complemento_Lb)
        self.Bairro_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Bairro_Lb.setFont(font)
        self.Bairro_Lb.setObjectName("Bairro_Lb")
        self.verticalLayout_2.addWidget(self.Bairro_Lb)
        self.CEP_Lb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CEP_Lb.setFont(font)
        self.CEP_Lb.setObjectName("CEP_Lb")
        self.verticalLayout_2.addWidget(self.CEP_Lb)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TipoPessoa_Cbx = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TipoPessoa_Cbx.setFont(font)
        self.TipoPessoa_Cbx.setObjectName("TipoPessoa_Cbx")
        self.TipoPessoa_Cbx.addItem("")
        self.TipoPessoa_Cbx.addItem("")
        self.verticalLayout.addWidget(self.TipoPessoa_Cbx)
        self.Nome_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Nome_Led.setFont(font)
        self.Nome_Led.setObjectName("Nome_Led")
        self.verticalLayout.addWidget(self.Nome_Led)
        self.Email_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Email_Led.setFont(font)
        self.Email_Led.setObjectName("Email_Led")
        self.verticalLayout.addWidget(self.Email_Led)
        self.Telefone_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Telefone_Led.setFont(font)
        self.Telefone_Led.setObjectName("Telefone_Led")
        self.verticalLayout.addWidget(self.Telefone_Led)
        self.CPFCNP_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CPFCNP_Led.setFont(font)
        self.CPFCNP_Led.setObjectName("CPFCNP_Led")
        self.verticalLayout.addWidget(self.CPFCNP_Led)
        self.Estado_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Estado_Led.setFont(font)
        self.Estado_Led.setObjectName("Estado_Led")
        self.verticalLayout.addWidget(self.Estado_Led)
        self.CIdade_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CIdade_Led.setFont(font)
        self.CIdade_Led.setObjectName("CIdade_Led")
        self.verticalLayout.addWidget(self.CIdade_Led)
        self.Logradouro_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Logradouro_Led.setFont(font)
        self.Logradouro_Led.setObjectName("Logradouro_Led")
        self.verticalLayout.addWidget(self.Logradouro_Led)
        self.Numero_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Numero_Led.setFont(font)
        self.Numero_Led.setObjectName("Numero_Led")
        self.verticalLayout.addWidget(self.Numero_Led)
        self.Complemento_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Complemento_Led.setFont(font)
        self.Complemento_Led.setObjectName("Complemento_Led")
        self.verticalLayout.addWidget(self.Complemento_Led)
        self.Bairro_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Bairro_Led.setFont(font)
        self.Bairro_Led.setObjectName("Bairro_Led")
        self.verticalLayout.addWidget(self.Bairro_Led)
        self.CEP_Led = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CEP_Led.setFont(font)
        self.CEP_Led.setObjectName("CEP_Led")
        self.verticalLayout.addWidget(self.CEP_Led)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.AmbienteEmissao_LB = QtWidgets.QLabel(self.scrollContents)
        self.AmbienteEmissao_LB.setGeometry(QtCore.QRect(570, 470, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AmbienteEmissao_LB.setFont(font)
        self.AmbienteEmissao_LB.setObjectName("AmbienteEmissao_LB")
        self.IDExterno_Led = QtWidgets.QLineEdit(self.scrollContents)
        self.IDExterno_Led.setGeometry(QtCore.QRect(800, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IDExterno_Led.setFont(font)
        self.IDExterno_Led.setObjectName("IDExterno_Led")
        self.IDExterno = QtWidgets.QLabel(self.scrollContents)
        self.IDExterno.setGeometry(QtCore.QRect(570, 390, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.IDExterno.setFont(font)
        self.IDExterno.setObjectName("IDExterno")
        self.ValorTotal_Led = QtWidgets.QLineEdit(self.scrollContents)
        self.ValorTotal_Led.setGeometry(QtCore.QRect(800, 530, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ValorTotal_Led.setFont(font)
        self.ValorTotal_Led.setObjectName("ValorTotal_Led")
        self.EmiteNota_Bt = QtWidgets.QPushButton(self.scrollContents)
        self.EmiteNota_Bt.setGeometry(QtCore.QRect(700, 590, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.EmiteNota_Bt.setFont(font)
        self.EmiteNota_Bt.setObjectName("EmiteNota_Bt")

        #Clica no Botão
        self.EmiteNota_Bt.clicked.connect(self.Getinformation)


        self.ServicoPrestado_Lb = QtWidgets.QLabel(self.scrollContents)
        self.ServicoPrestado_Lb.setGeometry(QtCore.QRect(720, 0, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ServicoPrestado_Lb.setFont(font)
        self.ServicoPrestado_Lb.setObjectName("ServicoPrestado_Lb")
        self.ValorTotal_Lb = QtWidgets.QLabel(self.scrollContents)
        self.ValorTotal_Lb.setGeometry(QtCore.QRect(570, 530, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ValorTotal_Lb.setFont(font)
        self.ValorTotal_Lb.setObjectName("ValorTotal_Lb")
        self.EnviaEmail_Lb = QtWidgets.QLabel(self.scrollContents)
        self.EnviaEmail_Lb.setGeometry(QtCore.QRect(570, 430, 181, 44))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EnviaEmail_Lb.setFont(font)
        self.EnviaEmail_Lb.setObjectName("EnviaEmail_Lb")
        self.EnviaEmail_Cbx = QtWidgets.QComboBox(self.scrollContents)
        self.EnviaEmail_Cbx.setGeometry(QtCore.QRect(800, 430, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.EnviaEmail_Cbx.setFont(font)
        self.EnviaEmail_Cbx.setObjectName("EnviaEmail_Cbx")
        self.EnviaEmail_Cbx.addItem("")
        self.EnviaEmail_Cbx.addItem("")
        self.DescricaoServico_Txed = QtWidgets.QTextEdit(self.scrollContents)
        self.DescricaoServico_Txed.setEnabled(True)
        self.DescricaoServico_Txed.setGeometry(QtCore.QRect(560, 90, 487, 161))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DescricaoServico_Txed.setFont(font)
        self.DescricaoServico_Txed.setObjectName("DescricaoServico_Txed")
        self.ISSRetidoFonte_Cbx = QtWidgets.QComboBox(self.scrollContents)
        self.ISSRetidoFonte_Cbx.setGeometry(QtCore.QRect(800, 323, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ISSRetidoFonte_Cbx.setFont(font)
        self.ISSRetidoFonte_Cbx.setObjectName("ISSRetidoFonte_Cbx")
        self.ISSRetidoFonte_Cbx.addItem("")
        self.ISSRetidoFonte_Cbx.addItem("")
        self.Aliquota_Led = QtWidgets.QLineEdit(self.scrollContents)
        self.Aliquota_Led.setGeometry(QtCore.QRect(800, 270, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Aliquota_Led.setFont(font)
        self.Aliquota_Led.setObjectName("Aliquota_Led")
        self.DescricaoServico_Lb = QtWidgets.QLabel(self.scrollContents)
        self.DescricaoServico_Lb.setGeometry(QtCore.QRect(560, 50, 197, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DescricaoServico_Lb.setFont(font)
        self.DescricaoServico_Lb.setObjectName("DescricaoServico_Lb")
        self.Aliquota_Lb = QtWidgets.QLabel(self.scrollContents)
        self.Aliquota_Lb.setGeometry(QtCore.QRect(570, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Aliquota_Lb.setFont(font)
        self.Aliquota_Lb.setObjectName("Aliquota_Lb")
        self.ISSRetidoFonte_Lb = QtWidgets.QLabel(self.scrollContents)
        self.ISSRetidoFonte_Lb.setGeometry(QtCore.QRect(570, 330, 197, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ISSRetidoFonte_Lb.setFont(font)
        self.ISSRetidoFonte_Lb.setObjectName("ISSRetidoFonte_Lb")
        self.scrollArea.setWidget(self.scrollContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setStyleSheet("QToolTip\n"
        "{\n"
        "     border: 1px solid black;\n"
        "     background-color: #ffa02f;\n"
        "     padding: 1px;\n"
        "     border-radius: 3px;\n"
        "     opacity: 100;\n"
        "}\n"
        "\n"
        "QWidget\n"
        "{\n"
        "    color: #b1b1b1;\n"
        "    background-color: #323232;\n"
        "}\n"
        "\n"
        "QWidget:item:hover\n"
        "{\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
        "    color: #000000;\n"
        "}\n"
        "\n"
        "QWidget:item:selected\n"
        "{\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "}\n"
        "\n"
        "QMenuBar::item\n"
        "{\n"
        "    background: transparent;\n"
        "}\n"
        "\n"
        "QMenuBar::item:selected\n"
        "{\n"
        "    background: transparent;\n"
        "    border: 1px solid #ffaa00;\n"
        "}\n"
        "\n"
        "QMenuBar::item:pressed\n"
        "{\n"
        "    background: #444;\n"
        "    border: 1px solid #000;\n"
        "    background-color: QLinearGradient(\n"
        "        x1:0, y1:0,\n"
        "        x2:0, y2:1,\n"
        "        stop:1 #212121,\n"
        "        stop:0.4 #343434/*,\n"
        "        stop:0.2 #343434,\n"
        "        stop:0.1 #ffaa00*/\n"
        "    );\n"
        "    margin-bottom:-1px;\n"
        "    padding-bottom:1px;\n"
        "}\n"
        "\n"
        "QMenu\n"
        "{\n"
        "    border: 1px solid #000;\n"
        "}\n"
        "\n"
        "QMenu::item\n"
        "{\n"
        "    padding: 2px 20px 2px 20px;\n"
        "}\n"
        "\n"
        "QMenu::item:selected\n"
        "{\n"
        "    color: #000000;\n"
        "}\n"
        "\n"
        "QWidget:disabled\n"
        "{\n"
        "    color: #404040;\n"
        "    background-color: #323232;\n"
        "}\n"
        "\n"
        "QAbstractItemView\n"
        "{\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
        "}\n"
        "\n"
        "QWidget:focus\n"
        "{\n"
        "    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
        "}\n"
        "\n"
        "QLineEdit\n"
        "{\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
        "    padding: 1px;\n"
        "    border-style: solid;\n"
        "    border: 1px solid #1e1e1e;\n"
        "    border-radius: 5;\n"
        "}\n"
        "\n"
        "QPushButton\n"
        "{\n"
        "    color: #b1b1b1;\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
        "    border-width: 1px;\n"
        "    border-color: #1e1e1e;\n"
        "    border-style: solid;\n"
        "    border-radius: 6;\n"
        "    padding: 3px;\n"
        "    font-size: 12px;\n"
        "    padding-left: 5px;\n"
        "    padding-right: 5px;\n"
        "}\n"
        "\n"
        "QPushButton:pressed\n"
        "{\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
        "}\n"
        "\n"
        "QComboBox\n"
        "{\n"
        "    selection-background-color: #ffaa00;\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
        "    border-style: solid;\n"
        "    border: 1px solid #1e1e1e;\n"
        "    border-radius: 5;\n"
        "}\n"
        "\n"
        "QComboBox:hover,QPushButton:hover\n"
        "{\n"
        "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "}\n"
        "\n"
        "\n"
        "QComboBox:on\n"
        "{\n"
        "    padding-top: 3px;\n"
        "    padding-left: 4px;\n"
        "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
        "    selection-background-color: #ffaa00;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView\n"
        "{\n"
        "    border: 2px solid darkgray;\n"
        "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down\n"
        "{\n"
        "     subcontrol-origin: padding;\n"
        "     subcontrol-position: top right;\n"
        "     width: 15px;\n"
        "\n"
        "     border-left-width: 0px;\n"
        "     border-left-color: darkgray;\n"
        "     border-left-style: solid; /* just a single line */\n"
        "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
        "     border-bottom-right-radius: 3px;\n"
        " }\n"
        "\n"
        "QComboBox::down-arrow\n"
        "{\n"
        "     image: url(:/down_arrow.png);\n"
        "}\n"
        "\n"
        "QGroupBox:focus\n"
        "{\n"
        "border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "}\n"
        "\n"
        "QTextEdit:focus\n"
        "{\n"
        "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "}\n"
        "\n"
        "QScrollBar:horizontal {\n"
        "     border: 1px solid #222222;\n"
        "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
        "     height: 7px;\n"
        "     margin: 0px 16px 0 16px;\n"
        "}\n"
        "\n"
        "QScrollBar::handle:horizontal\n"
        "{\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
        "      min-height: 20px;\n"
        "      border-radius: 2px;\n"
        "}\n"
        "\n"
        "QScrollBar::add-line:horizontal {\n"
        "      border: 1px solid #1b1b19;\n"
        "      border-radius: 2px;\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "      width: 14px;\n"
        "      subcontrol-position: right;\n"
        "      subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::sub-line:horizontal {\n"
        "      border: 1px solid #1b1b19;\n"
        "      border-radius: 2px;\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "      width: 14px;\n"
        "     subcontrol-position: left;\n"
        "     subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
        "{\n"
        "      border: 1px solid black;\n"
        "      width: 1px;\n"
        "      height: 1px;\n"
        "      background: white;\n"
        "}\n"
        "\n"
        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
        "{\n"
        "      background: none;\n"
        "}\n"
        "\n"
        "QScrollBar:vertical\n"
        "{\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
        "      width: 7px;\n"
        "      margin: 16px 0 16px 0;\n"
        "      border: 1px solid #222222;\n"
        "}\n"
        "\n"
        "QScrollBar::handle:vertical\n"
        "{\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
        "      min-height: 20px;\n"
        "      border-radius: 2px;\n"
        "}\n"
        "\n"
        "QScrollBar::add-line:vertical\n"
        "{\n"
        "      border: 1px solid #1b1b19;\n"
        "      border-radius: 2px;\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
        "      height: 14px;\n"
        "      subcontrol-position: bottom;\n"
        "      subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::sub-line:vertical\n"
        "{\n"
        "      border: 1px solid #1b1b19;\n"
        "      border-radius: 2px;\n"
        "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
        "      height: 14px;\n"
        "      subcontrol-position: top;\n"
        "      subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
        "{\n"
        "      border: 1px solid black;\n"
        "      width: 1px;\n"
        "      height: 1px;\n"
        "      background: white;\n"
        "}\n"
        "\n"
        "\n"
        "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
        "{\n"
        "      background: none;\n"
        "}\n"
        "\n"
        "QTextEdit\n"
        "{\n"
        "    background-color: #242424;\n"
        "}\n"
        "\n"
        "QPlainTextEdit\n"
        "{\n"
        "    background-color: #242424;\n"
        "}\n"
        "\n"
        "QHeaderView::section\n"
        "{\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
        "    color: white;\n"
        "    padding-left: 4px;\n"
        "    border: 1px solid #6c6c6c;\n"
        "}\n"
        "\n"
        "QCheckBox:disabled\n"
        "{\n"
        "color: #414141;\n"
        "}\n"
        "\n"
        "QDockWidget::title\n"
        "{\n"
        "    text-align: center;\n"
        "    spacing: 3px; /* spacing between items in the tool bar */\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
        "}\n"
        "\n"
        "QDockWidget::close-button, QDockWidget::float-button\n"
        "{\n"
        "    text-align: center;\n"
        "    spacing: 1px; /* spacing between items in the tool bar */\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
        "}\n"
        "\n"
        "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
        "{\n"
        "    background: #242424;\n"
        "}\n"
        "\n"
        "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
        "{\n"
        "    padding: 1px -1px -1px 1px;\n"
        "}\n"
        "\n"
        "QMainWindow::separator\n"
        "{\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
        "    color: white;\n"
        "    padding-left: 4px;\n"
        "    border: 1px solid #4c4c4c;\n"
        "    spacing: 3px; /* spacing between items in the tool bar */\n"
        "}\n"
        "\n"
        "QMainWindow::separator:hover\n"
        "{\n"
        "\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
        "    color: white;\n"
        "    padding-left: 4px;\n"
        "    border: 1px solid #6c6c6c;\n"
        "    spacing: 3px; /* spacing between items in the tool bar */\n"
        "}\n"
        "\n"
        "QToolBar::handle\n"
        "{\n"
        "     spacing: 3px; /* spacing between items in the tool bar */\n"
        "     background: url(:/images/handle.png);\n"
        "}\n"
        "\n"
        "QMenu::separator\n"
        "{\n"
        "    height: 2px;\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
        "    color: white;\n"
        "    padding-left: 4px;\n"
        "    margin-left: 10px;\n"
        "    margin-right: 5px;\n"
        "}\n"
        "\n"
        "QProgressBar\n"
        "{\n"
        "    border: 2px solid grey;\n"
        "    border-radius: 5px;\n"
        "    text-align: center;\n"
        "}\n"
        "\n"
        "QProgressBar::chunk\n"
        "{\n"
        "    background-color: #d7801a;\n"
        "    width: 2.15px;\n"
        "    margin: 0.5px;\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "    color: #b1b1b1;\n"
        "    border: 1px solid #444;\n"
        "    border-bottom-style: none;\n"
        "    background-color: #323232;\n"
        "    padding-left: 10px;\n"
        "    padding-right: 10px;\n"
        "    padding-top: 3px;\n"
        "    padding-bottom: 2px;\n"
        "    margin-right: -1px;\n"
        "}\n"
        "\n"
        "QTabWidget::pane {\n"
        "    border: 1px solid #444;\n"
        "    top: 1px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:last\n"
        "{\n"
        "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
        "    border-top-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:first:!selected\n"
        "{\n"
        " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
        "\n"
        "\n"
        "    border-top-left-radius: 3px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected\n"
        "{\n"
        "    color: #b1b1b1;\n"
        "    border-bottom-style: solid;\n"
        "    margin-top: 3px;\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected\n"
        "{\n"
        "    border-top-left-radius: 3px;\n"
        "    border-top-right-radius: 3px;\n"
        "    margin-bottom: 0px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected:hover\n"
        "{\n"
        "    /*border-top: 2px solid #ffaa00;\n"
        "    padding-bottom: 3px;*/\n"
        "    border-top-left-radius: 3px;\n"
        "    border-top-right-radius: 3px;\n"
        "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
        "}\n"
        "\n"
        "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
        "    color: #b1b1b1;\n"
        "    background-color: #323232;\n"
        "    border: 1px solid #b1b1b1;\n"
        "    border-radius: 6px;\n"
        "}\n"
        "\n"
        "QRadioButton::indicator:checked\n"
        "{\n"
        "    background-color: qradialgradient(\n"
        "        cx: 0.5, cy: 0.5,\n"
        "        fx: 0.5, fy: 0.5,\n"
        "        radius: 1.0,\n"
        "        stop: 0.25 #ffaa00,\n"
        "        stop: 0.3 #323232\n"
        "    );\n"
        "}\n"
        "\n"
        "QCheckBox::indicator{\n"
        "    color: #b1b1b1;\n"
        "    background-color: #323232;\n"
        "    border: 1px solid #b1b1b1;\n"
        "    width: 9px;\n"
        "    height: 9px;\n"
        "}\n"
        "\n"
        "QRadioButton::indicator\n"
        "{\n"
        "    border-radius: 6px;\n"
        "}\n"
        "\n"
        "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
        "{\n"
        "    border: 1px solid #ffaa00;\n"
        "}\n"
        "\n"
        "QCheckBox::indicator:checked\n"
        "{\n"
        "    image:url(:/images/checkbox.png);\n"
        "}\n"
        "\n"
        "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
        "{\n"
        "    border: 1px solid #444;\n"
        "}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emitir Nota"))
        self.Cliente_lb.setText(_translate("MainWindow", "Cliente"))
        self.AmbienteEmissao_Cbx.setItemText(0, _translate("MainWindow", "Homologação"))
        self.AmbienteEmissao_Cbx.setItemText(1, _translate("MainWindow", "Produção"))
        self.TipoPessoa_Lb.setText(_translate("MainWindow", "Tipo Pessoa"))
        self.nome_Lb.setText(_translate("MainWindow", "Nome"))
        self.email_Lb.setText(_translate("MainWindow", "E-mail"))
        self.Telefone_Lb.setText(_translate("MainWindow", "Telefone"))
        self.CPFCNPJ_Lb.setText(_translate("MainWindow", "CPF ou CNPJ"))
        self.Estado_Lb.setText(_translate("MainWindow", "Estado"))
        self.Cidade_Lb.setText(_translate("MainWindow", "Cidade"))
        self.Logradouro_Lb.setText(_translate("MainWindow", "Logradouro"))
        self.Numero_Lb.setText(_translate("MainWindow", "Número"))
        self.Complemento_Lb.setText(_translate("MainWindow", "Complemento"))
        self.Bairro_Lb.setText(_translate("MainWindow", "Bairro"))
        self.CEP_Lb.setText(_translate("MainWindow", "CEP"))
        self.TipoPessoa_Cbx.setItemText(0, _translate("MainWindow", "Pessoa Fisica"))
        self.TipoPessoa_Cbx.setItemText(1, _translate("MainWindow", "Pessoa Juridica"))
        self.AmbienteEmissao_LB.setText(_translate("MainWindow", "Ambiente de Emissão:"))
        self.IDExterno.setText(_translate("MainWindow", "ID Externo:"))
        self.EmiteNota_Bt.setText(_translate("MainWindow", "Emitir a Nota"))
        self.ServicoPrestado_Lb.setText(_translate("MainWindow", "Serviço Prestado"))
        self.ValorTotal_Lb.setText(_translate("MainWindow", "Valor Total da Nota:"))
        self.EnviaEmail_Lb.setText(_translate("MainWindow", "Enviar para email:"))
        self.EnviaEmail_Cbx.setItemText(0, _translate("MainWindow", "Sim"))
        self.EnviaEmail_Cbx.setItemText(1, _translate("MainWindow", "Não"))
        self.ISSRetidoFonte_Cbx.setItemText(0, _translate("MainWindow", "Não"))
        self.ISSRetidoFonte_Cbx.setItemText(1, _translate("MainWindow", "Sim"))
        self.DescricaoServico_Lb.setText(_translate("MainWindow", "Descrição do serviço"))
        self.Aliquota_Lb.setText(_translate("MainWindow", "Aliquota ISS"))
        self.ISSRetidoFonte_Lb.setText(_translate("MainWindow", "ISS Retido na Fonte"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
