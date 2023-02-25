# 请输入要实现的功能
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
# 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxx

# 这个程序是Terran的AI分类
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
# 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxx
import json
import sys
import time
from main1 import *

#加载json文件
def load_json():
    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'r') as f:
        data = json.load(f)
#将json文件转换为字典，返回字典
def json_to_dict():
    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'r') as f:
        data = json.load(f)
        return data










def jiushibubingtuan():
    app = QApplication(sys.argv)
    widget = MyWidget('经典生化T','旧式步兵团','纯地面兵种','','提防鬼子进村！！')
    widget.show()
    widget.zhiding()
    QTimer.singleShot(3500, widget.close)
    app.exec_()
    app.quit()

def tujituan():
    app = QApplication(sys.argv)
    widget = MyWidget('生化T','突击团','','提防鬼子进村！！')
    widget.show()
    widget.zhiding()
    QTimer.singleShot(3500, widget.close)
    app.exec_()
    app.quit()

def anyingkejituan():
    app = QApplication(sys.argv)
    widget = MyWidget('科技T','暗影科技团','','无隐形单位！')
    widget.show()
    widget.zhiding()
    QTimer.singleShot(3500, widget.close)
    app.exec_()
    app.quit()

def zhanzhengjixietuan():
    app = QApplication(sys.argv)
    widget = MyWidget('机械T','战争机械团','','隐形寡妇雷')
    widget.show()
    widget.zhiding()
    QTimer.singleShot(3500, widget.close)
    app.exec_()
    app.quit()

def jiushijixietuan():
    app = QApplication(sys.argv)
    widget = MyWidget('经典机械T','旧式机械团','','隐形怨灵战机！！')
    widget.show()
    widget.zhiding()
    QTimer.singleShot(3500, widget.close)
    app.exec_()
    app.quit()

def diguozhandouqun():
    app = QApplication(sys.argv)
    widget = MyWidget('空军T','帝国战斗群','','隐形女妖！！')
    widget.show()
    widget.zhiding()
    QTimer.singleShot(3500, widget.close)
    app.exec_()
    app.quit()


def shibieAI_T():
    #判断字典中的键值对，"aibool1"-"aibool6"d的值是否为True，如果为True，则执行对应的函数
    while True:
        load_json()
        aiandrace = json_to_dict()
        if aiandrace["aibool1"] == True:
            tujituan()
            break
        elif aiandrace["aibool2"] == True:
            jiushibubingtuan()
            break
        elif aiandrace["aibool3"] == True:
            anyingkejituan()
            break
        elif aiandrace["aibool4"] == True:
            zhanzhengjixietuan()
            break
        elif aiandrace["aibool5"] == True:
            jiushijixietuan()
            break
        elif aiandrace["aibool6"] == True:
            diguozhandouqun()
            break
        time.sleep(1)

shibieAI_T()








