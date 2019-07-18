from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, Qt
from views.mainWindowUi import Ui_MainWindow
from views.formViewerWidget import FormViewWidget
from views.loginView import LoginDialog
from forms.FormController import FormController
from forms.formModel import FormModel


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, model, controller):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.model = model
        self.controller = controller

        self.actionInventory.triggered.connect(self.show_actionInventory)
        self.actionPickList.triggered.connect(self.show_actionPickList)
        self.actionSign_In.triggered.connect(self.showLoginDialog)


    def showLoginDialog(self):
        self.loginDialog = LoginDialog(self.model, self.controller)
        self.loginDialog.s_dialogBoxClose.connect(self.enableMainWindow)
        self.setEnabled(False)
        self.loginDialog.show()

    def enableMainWindow(self):
        self.setEnabled(True)

    def show_actionInventory(self):
        self.formModel = FormModel()
        self.formController = FormController(self.formModel)
        self.formViewer = FormViewWidget(self.formController, self.formModel)
        self.setCentralWidget(self.formViewer)

    def show_actionPickList(self):
        self.temporary = QLabel()
        self.temporary.setText("LOL")
        self.formViewer = FormViewWidget(self.controller, self.model)
        self.setCentralWidget(self.temporary)

