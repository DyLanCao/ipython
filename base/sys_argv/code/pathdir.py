import sys,os
try:
    import parameters,helpAbout,autoUpdate
    from Combobox import ComboBox
except ImportError:
    from COMTool import parameters,helpAbout,autoUpdate
    from COMTool.Combobox import ComboBox

from PyQt5.QtGui import QIcon,QFont,QTextCursor,QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget,QMainWindow,
                             QVBoxLayout,QHBoxLayout,QGridLayout,QTextEdit,QLabel,QRadioButton,QCheckBox,
                             QLineEdit,QGroupBox,QSplitter,QFileDialog)

class MainWindow(QMainWindow):
	DataPath = "./"
	def __init__(self,app):
		pathDirList = sys.argv[0].replace("\\", "/").split("/")
		self.DataPath = os.path.abspath("/".join(str(i) for i in pathDirList))
		pathDirList.pop()
		if not os.path.exists(self.DataPath + "/" + parameters.strDataDirName):
		    pathDirList.pop()
		    self.DataPath = os.path.abspath("/".join(str(i) for i in pathDirList))
		self.DataPath = (self.DataPath + "/" + parameters.strDataDirName).replace("\\", "/")

def main():
	app = QApplication(sys.argv)
	mainWindow = MainWindow(app)
	print("pathdir:",mainWindow.DataPath)

if __name__ == "__main__":
	main()
