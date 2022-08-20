const { app, BrowserWindow } = require('electron')
//导入两个模块app控制生命周期
//BrowserWindow创建窗口

const path = require('path')//导入node.js的path模块

//利用函数表达式来创建窗口
const createWindow = () => {
    const win = new BrowserWindow({
      width: 1200,
      height: 600,
      webPreferences: {
         preload: path.join(__dirname, 'preload.js')
         }//加载js
    })
  
    win.loadFile('index.html')//载入html文件
  }

    

  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
  })

  //若closed则判断不为macOS后执行quit函数

  app.whenReady().then(() => {
    createWindow()//常规(windows和linux)
  
    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })//未成功打开window适配macOS
  })