# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import *
from PyQt4 import QtGui, uic

import sqlite3


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.a=[]
        self.b=[]
        self.pushButton.clicked.connect(self.nextPage)
        self.pushButton_2.clicked.connect(self.searchPage)
    def toHome(self):
        self.a=[]
        self.b=[]
        super(MyWindow, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.nextPage)
        self.pushButton_2.clicked.connect(self.searchPage)
        
    def doSearch(self):
        self.comboBox.clear() 
        w=unicode(self.lineEdit_25.text())
        conn = sqlite3.connect('test.db')
        sql="select * from data WHERE `1` LIKE '%"+w+"%'"
        print sql
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        r=map(lambda x:x[0],rows)
        self.comboBox.addItems(r)
        self.comboBox.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.sel = unicode(self.comboBox.currentText())
        for i in rows:
            if i[0]==self.sel:
                self.d=i
                break
        
        print i
        
    def showData(self):
        self.close()
        super(MyWindow, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()
        self.pushButton_2.deleteLater()
        self.pushButton.clicked.connect(self.showData2)
        p1=[self.lineEdit, self.lineEdit_2,self.lineEdit_3,self.lineEdit_8,self.lineEdit_10,self.lineEdit_6, self.lineEdit_11,self.lineEdit_12,self.lineEdit_13,self.textEdit, self.lineEdit_17, self.lineEdit_18,self.lineEdit_19,self.lineEdit_20,self.textEdit_2, self.lineEdit_21, self.lineEdit_22,self.lineEdit_23,self.lineEdit_24,self.textEdit_3]
        for i in range(len(p1)):
            p1[i].setText(self.d[i])
            p1[i].setEnabled(False)
            
    def showData2(self):
        self.e=self.d[20:]
        self.close()
        super(MyWindow, self).__init__()
        uic.loadUi('2ndpage.ui', self)
        self.show()
        self.pushButton.deleteLater()

        self.pushButton_3.clicked.connect(self.showData)
        self.pushButton_2.clicked.connect(self.toHome)

        p2=[self.lineEdit_25, self.lineEdit_26,self.lineEdit_27,self.lineEdit_28,self.textEdit_4,self.textEdit_5,self.lineEdit_29,self.lineEdit_30, self.lineEdit_31,self.lineEdit_32,self.lineEdit_6, self.lineEdit_11,self.lineEdit_12,self.lineEdit_13,self.textEdit, self.lineEdit_7, self.lineEdit_16,self.lineEdit_15,self.lineEdit_14,self.textEdit_2]
        for i in range(len(p2)):
            p2[i].setText(self.e[i])
            p2[i].setEnabled(False)

            
    def searchPage(self):
        self.close()
        super(MyWindow, self).__init__()
        uic.loadUi('searchpage1.ui', self)
        self.show()
        self.pushButton_2.clicked.connect(self.showData)
        self.pushButton.clicked.connect(self.doSearch)

        self.comboBox.setEnabled(False)
        self.pushButton_2.setEnabled(False)

    def nextPage(self):
        self.a=[self.lineEdit.text(), self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_8.text(),self.lineEdit_10.text(),self.lineEdit_6.text(), self.lineEdit_11.text(),self.lineEdit_12.text(),self.lineEdit_13.text(),self.textEdit.toPlainText(), self.lineEdit_17.text(), self.lineEdit_18.text(),self.lineEdit_19.text(),self.lineEdit_20.text(),self.textEdit_2.toPlainText(), self.lineEdit_21.text(), self.lineEdit_22.text(),self.lineEdit_23.text(),self.lineEdit_24.text(),self.textEdit_3.toPlainText(),]
        self.a=map(lambda x:"'"+unicode(x)+"'",self.a)
        print len(self.a)
        self.close()
        super(MyWindow, self).__init__()
        uic.loadUi('2ndpage.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.addData)
        self.pushButton_2.deleteLater()
        self.pushButton_3.deleteLater()
    

    def addData(self):
        self.b=[self.lineEdit_25.text(), self.lineEdit_26.text(),self.lineEdit_27.text(),self.lineEdit_28.text(),self.textEdit_4.toPlainText(),self.textEdit_5.toPlainText(),self.lineEdit_29.text(),self.lineEdit_30.text(), self.lineEdit_31.text(),self.lineEdit_32.text(),self.lineEdit_6.text(), self.lineEdit_11.text(),self.lineEdit_12.text(),self.lineEdit_13.text(),self.textEdit.toPlainText(), self.lineEdit_7.text(), self.lineEdit_16.text(),self.lineEdit_15.text(),self.lineEdit_14.text(),self.textEdit_2.toPlainText()]
        self.b=map(lambda x:"'"+unicode(x)+"'",self.b)
        #print self.b,len(self.b)
        self.a=self.a+self.b
        
        print self.a
        print self.b
        conn = sqlite3.connect('test.db')
        sql="CREATE TABLE IF NOT EXISTS data ('1' varchar(500) primary key ,'2' varchar(500), '3' varchar(500), '4' varchar(500), '5' varchar(500), '6' varchar(500), '7' varchar(500), '8' varchar(500), '9' varchar(500), '10' varchar(500), '11' varchar(500), '12' varchar(500), '13' varchar(500), '14' varchar(500), '15' varchar(500), '16' varchar(500), '17' varchar(500), '18' varchar(500), '19' varchar(500), '20' varchar(500), '21' varchar(500), '22' varchar(500), '23' varchar(500), '24' varchar(500), '25' varchar(500), '26' varchar(500), '27' varchar(500), '28' varchar(500), '29' varchar(500), '30' varchar(500), '31' varchar(500), '32' varchar(500), '33' varchar(500), '34' varchar(500), '35' varchar(500), '36' varchar(500), '37' varchar(500), '38' varchar(500), '39' varchar(500), '40' varchar(500))"
        conn.execute(sql)
        sql="insert into data values (%s)"%','.join(self.a)
        conn.execute(sql)
        conn.commit()
        #print 1
        self.toHome()

    
        


            

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
