# 这个程序是Protoss的AI分类# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx# 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxximport jsonimport sysimport threadingimport timefrom main1 import *#加载json文件def load_json():    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'r') as f:        data = json.load(f)#将json文件转换为字典，返回字典def json_to_dict():    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'r') as f:        data = json.load(f)        return datadef dashijixie():    app = QApplication(sys.argv)    widget=MyWidget('经典机械P','大师机械',)    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def buzhanjijia():    app = QApplication(sys.argv)    widget=MyWidget('巨像P','步战机甲',)    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def kalaidexiwang():    app = QApplication(sys.argv)    widget=MyWidget('航母P','卡莱的希望',)    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def aierxianfeng():    app = QApplication(sys.argv)    widget=MyWidget('经典地面P','艾尔先锋','又称主教P','金甲虫对地强力AOE','隐身仲裁机')    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def zuzhangzhijun():    app = QApplication(sys.argv)    widget=MyWidget('经典空军P','族长之军','与沃拉尊的兵种基本相同','隐身仲裁机')    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def anyingxirao():    app = QApplication(sys.argv)    widget=MyWidget('隐刀P','暗影袭扰','注意隐刀！！','空军只有凤凰')    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def xiraopaoji():    app = QApplication(sys.argv)    widget=MyWidget('金甲P','袭扰炮击','金甲虫对地强力AOE')    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def fengbaopolin():    app = QApplication(sys.argv)    widget=MyWidget('风暴P','风暴迫临',)    widget.show()    widget.zhiding()    QTimer.singleShot(5000, widget.close)    app.exec_()    app.quit()def shibieAI_P():    #判断字典中的键值对，"aibool7"-"aibool4"d的值是否为True，如果为True，则执行对应的函数    while True:        load_json()        aiandrace = json_to_dict()        if aiandrace["aibool7"] == True:            dashijixie()            break        elif aiandrace["aibool8"] == True:            buzhanjijia()            break        elif aiandrace["aibool9"] == True:            kalaidexiwang()            break        elif aiandrace["aibool10"] == True:            aierxianfeng()            break        elif aiandrace["aibool11"] == True:            zuzhangzhijun()            break        elif aiandrace["aibool12"] == True:            anyingxirao()            break        elif aiandrace["aibool13"] == True:            xiraopaoji()            break        elif aiandrace["aibool14"] == True:            fengbaopolin()            break        time.sleep(1)shibieAI_P()