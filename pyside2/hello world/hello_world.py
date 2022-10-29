from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox,QWidget

from ui_main import Ui_MainWindow
# app=QApplication([])#提供app,最底层功能

# window = QMainWindow()#创建窗口
# window.resize(500, 400)
# window.move(300, 310)#相对屏幕左上角
# window.setWindowTitle('薪资统计')

# textEdit = QPlainTextEdit(window)
# textEdit.setPlaceholderText("请输入薪资表")
# textEdit.move(10,25)#相对位置
# textEdit.resize(300,350)




# button = QPushButton('统计', window)#对象的实例化
# button.move(380,80)
# button.clicked.connect(handleCalc)#类似js的click()
# window.show()

# app.exec_()

#使用外部样式表
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问
        self.ui.pushButton.clicked.connect(self.handleCalc)
        
    def handleCalc(self):
        QMessageBox.about(self,"Notice","be click")

app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()