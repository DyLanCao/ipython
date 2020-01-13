# minimal QWebEngine example.
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
app = QApplication( [] )
view = QWebEngineView()
view.load( QUrl( "http://www.pyinstaller.org" ) )
view.show()
app.exec_()
