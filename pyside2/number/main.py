from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox,QWidget,QLabel,QFileDialog
from PIL import Image
import os
import numpy as np
from ui_main import Ui_MainWindow
import torch
from torch import nn
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        
        # 使用界面定义的控件，也是从ui里面访问
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.pushButton.clicked.connect(self.predict)

        
    def handleCalc(self):
        FileDialog = QFileDialog(self.ui.pushButton)
        FileDialog.setFileMode(QFileDialog.AnyFile)#调用读取文件的操作
        image_file, _ = FileDialog.getOpenFileName(self.ui.pushButton,'open file','./','Image files (*.jpg *.png *.jpeg)')  # 选择目录，返回选中的路径 'Image files (*.jpg *.gif *.png *.jpeg)'
        im = Image.open(image_file)
        self.out = im.resize((28, 28), Image.Resampling.LANCZOS)#真实图片
        disp = im.resize((280, 280), Image.Resampling.LANCZOS).convert('L')#用于展示的图片
        disp_path=os.path.join('pyside2','number','temp','disp.png')
        disp.save(disp_path)
        self.out=np.array(self.out)#将图片数组化
        self.proc = np.array(im.resize((28, 28), Image.Resampling.LANCZOS))[:,:,:3]
        if(self.proc[0,0,0]>250):
            self.proc=255-np.array(Image.fromarray(self.proc).convert('L'))#背景转黑色
        else:
            self.proc=np.array(Image.fromarray(self.proc).convert('L'))#本来就为黑
        proc_disp = Image.fromarray(self.proc).resize((280, 280), Image.Resampling.LANCZOS)#显示灰度图片
        # plt.imshow(self.proc)
        # plt.show()
        proc_path=os.path.join('pyside2','number','temp','proc.png')
        proc_disp.save(proc_path)
        self.ui.input.setPixmap(disp_path)
        self.ui.proc.setPixmap(proc_path)
        
    def predict(self):
        net = nn.Sequential(
    nn.Conv2d(1, 6, kernel_size=5, padding=2), nn.Sigmoid(),#6个输出通道32*32
    #32-5+1=28
    nn.AvgPool2d(kernel_size=2, stride=2),#和核的大小一样
    nn.Conv2d(6, 16, kernel_size=5), nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),
    nn.Flatten(),
    nn.Linear(16 * 5 * 5, 120), nn.Sigmoid(),
    nn.Linear(120, 84), nn.Sigmoid(),
    nn.Linear(84, 10))
        net.load_state_dict(torch.load(os.path.join('pyside2','number','data','mnist.params')))
        ans=net(torch.tensor(self.proc/255).to(torch.float32).reshape(-1,1,28,28)).argmax().item()
        self.ui.output.setText(f'预测结果为 {ans}')

app = QApplication([])

mainw = MainWindow()
mainw.show()
app.exec_()