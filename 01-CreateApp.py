import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from flask import g

def window():
    # sys.argv => gönderilen komutlar
    
    # app
    # Application() -> uygulama oluşturur..
    app = QApplication(sys.argv) 
    
    
    # uygulamanın Ana Ekranı 
    # QMainWindow -> Ana Ekran
    win = QMainWindow()
    
    win.setGeometry(80,60,500,500)
    win.setWindowTitle("First Application")
    
    # Show() -> pencereyi gösteriri
    win.show()
    # system tarafından EXIT komutu gönderildiğinde 
    # app işler
    sys.exit(app.exec_())
    
    
window()