# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary_popup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(539, 595)
        
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lbl_companyName = QtGui.QLabel(Dialog)
        self.lbl_companyName.setObjectName(_fromUtf8("lbl_companyName"))
        self.gridLayout.addWidget(self.lbl_companyName, 0, 0, 1, 1)
        self.lineEdit_companyName = QtGui.QLineEdit(Dialog)
        self.lineEdit_companyName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_companyName.setObjectName(_fromUtf8("lineEdit_companyName"))
        self.gridLayout.addWidget(self.lineEdit_companyName, 0, 1, 1, 1)
        self.lbl_comapnyLogo = QtGui.QLabel(Dialog)
        self.lbl_comapnyLogo.setObjectName(_fromUtf8("lbl_comapnyLogo"))
        self.gridLayout.addWidget(self.lbl_comapnyLogo, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_browse = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy)
        self.btn_browse.setObjectName(_fromUtf8("btn_browse"))
        self.horizontalLayout.addWidget(self.btn_browse)
        self.lbl_browse = QtGui.QLabel(Dialog)
        self.lbl_browse.setMouseTracking(True)
        self.lbl_browse.setAcceptDrops(True)
        self.lbl_browse.setText(_fromUtf8(""))
        self.lbl_browse.setObjectName(_fromUtf8("lbl_browse"))
        self.horizontalLayout.addWidget(self.lbl_browse)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.lbl_groupName = QtGui.QLabel(Dialog)
        self.lbl_groupName.setObjectName(_fromUtf8("lbl_groupName"))
        self.gridLayout.addWidget(self.lbl_groupName, 2, 0, 1, 1)
        self.lineEdit_groupName = QtGui.QLineEdit(Dialog)
        self.lineEdit_groupName.setCursorPosition(0)
        self.lineEdit_groupName.setObjectName(_fromUtf8("lineEdit_groupName"))
        self.gridLayout.addWidget(self.lineEdit_groupName, 2, 1, 1, 1)
        self.lbl_designer = QtGui.QLabel(Dialog)
        self.lbl_designer.setObjectName(_fromUtf8("lbl_designer"))
        self.gridLayout.addWidget(self.lbl_designer, 3, 0, 1, 1)
        self.lineEdit_designer = QtGui.QLineEdit(Dialog)
        self.lineEdit_designer.setObjectName(_fromUtf8("lineEdit_designer"))
        self.gridLayout.addWidget(self.lineEdit_designer, 3, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.btn_useProfile = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_useProfile.sizePolicy().hasHeightForWidth())
        self.btn_useProfile.setSizePolicy(sizePolicy)
        self.btn_useProfile.setObjectName(_fromUtf8("btn_useProfile"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.btn_useProfile)
        self.btn_saveProfile = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_saveProfile.sizePolicy().hasHeightForWidth())
        self.btn_saveProfile.setSizePolicy(sizePolicy)
        self.btn_saveProfile.setObjectName(_fromUtf8("btn_saveProfile"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.btn_saveProfile)
        self.gridLayout.addLayout(self.formLayout, 4, 1, 1, 1)
        self.lbl_projectTitle = QtGui.QLabel(Dialog)
        self.lbl_projectTitle.setObjectName(_fromUtf8("lbl_projectTitle"))
        self.gridLayout.addWidget(self.lbl_projectTitle, 5, 0, 1, 1)
        self.lineEdit_projectTitle = QtGui.QLineEdit(Dialog)
        self.lineEdit_projectTitle.setObjectName(_fromUtf8("lineEdit_projectTitle"))
        self.gridLayout.addWidget(self.lineEdit_projectTitle, 5, 1, 1, 1)
        self.lbl_subtitle = QtGui.QLabel(Dialog)
        self.lbl_subtitle.setObjectName(_fromUtf8("lbl_subtitle"))
        self.gridLayout.addWidget(self.lbl_subtitle, 6, 0, 1, 1)
        self.lineEdit_subtitle = QtGui.QLineEdit(Dialog)
        self.lineEdit_subtitle.setText(_fromUtf8(""))
        self.lineEdit_subtitle.setObjectName(_fromUtf8("lineEdit_subtitle"))
        self.gridLayout.addWidget(self.lineEdit_subtitle, 6, 1, 1, 1)
        self.lbl_jobNumber = QtGui.QLabel(Dialog)
        self.lbl_jobNumber.setObjectName(_fromUtf8("lbl_jobNumber"))
        self.gridLayout.addWidget(self.lbl_jobNumber, 7, 0, 1, 1)
        self.lineEdit_jobNumber = QtGui.QLineEdit(Dialog)
        self.lineEdit_jobNumber.setObjectName(_fromUtf8("lineEdit_jobNumber"))
        self.gridLayout.addWidget(self.lineEdit_jobNumber, 7, 1, 1, 1)
        self.lbl_method = QtGui.QLabel(Dialog)
        self.lbl_method.setObjectName(_fromUtf8("lbl_method"))
        self.gridLayout.addWidget(self.lbl_method, 8, 0, 1, 1)
        self.comboBox_method = QtGui.QComboBox(Dialog)
        self.comboBox_method.setObjectName(_fromUtf8("comboBox_method"))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.comboBox_method.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_method, 8, 1, 1, 1)
        self.lbl_addComment = QtGui.QLabel(Dialog)
        self.lbl_addComment.setObjectName(_fromUtf8("lbl_addComment"))
        self.gridLayout.addWidget(self.lbl_addComment, 9, 0, 1, 1)
        self.txt_additionalComments = QtGui.QTextEdit(Dialog)
        self.txt_additionalComments.setStyleSheet(_fromUtf8("  QTextCursor textCursor;\n"
"  textCursor.setPosistion(0, QTextCursor::MoveAnchor); \n"
"  textedit->setTextCursor( textCursor );"))
        self.txt_additionalComments.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_additionalComments.setFrameShape(QtGui.QFrame.WinPanel)
        self.txt_additionalComments.setFrameShadow(QtGui.QFrame.Sunken)
        self.txt_additionalComments.setTabChangesFocus(False)
        self.txt_additionalComments.setReadOnly(False)
        self.txt_additionalComments.setObjectName(_fromUtf8("txt_additionalComments"))
        self.gridLayout.addWidget(self.txt_additionalComments, 9, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 10, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.btn_browse, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lbl_browse.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_companyName.setText(_translate("Dialog", "Company Name :", None))
        self.lbl_comapnyLogo.setText(_translate("Dialog", "Company Logo :", None))
        self.btn_browse.setText(_translate("Dialog", "Browse...", None))
        self.lbl_groupName.setText(_translate("Dialog", "Group/Team Name :", None))
        self.lbl_designer.setText(_translate("Dialog", "Designer :", None))
        self.btn_useProfile.setText(_translate("Dialog", "Use Profile", None))
        self.btn_saveProfile.setText(_translate("Dialog", "Save Profile", None))
        self.lbl_projectTitle.setText(_translate("Dialog", "Project Title :", None))
        self.lbl_subtitle.setText(_translate("Dialog", "Subtitle :", None))
        self.lineEdit_subtitle.setPlaceholderText(_translate("Dialog", "(Optional)", None))
        self.lbl_jobNumber.setText(_translate("Dialog", "Job Number :", None))
        self.lbl_method.setText(_translate("Dialog", "Method :", None))
        self.comboBox_method.setItemText(0, _translate("Dialog", "Limit State Design (No Earthquake Load)", None))
        self.comboBox_method.setItemText(1, _translate("Dialog", "Limit State (Capacity Based) Design", None))
        self.comboBox_method.setItemText(2, _translate("Dialog", "Working Stress Design", None))
        self.lbl_addComment.setText(_translate("Dialog", "Additional Comments :", None))
        self.txt_additionalComments.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

