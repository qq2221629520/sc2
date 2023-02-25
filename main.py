# 请输入这个程序的功能
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
# 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxx
import time

import pyautogui
# from main1 import *

import main1
from allmapdescription import *
from sandazhongzu  import *

import json
import subprocess



bool_1 = False
bool_2 = False
bool_3 = False
aibool1 = False
aibool2 = False
aibool3 = False
aibool4 = False
aibool5 = False
aibool6 = False
aibool7 = False
aibool8 = False
aibool9 = False
aibool10 = False
aibool11 = False
aibool12 = False
aibool13 = False
aibool14 = False
aibool15 = False
aibool16 = False
aibool17 = False
aibool18 = False
aibool19 = False
aib00l20 = False
# for i in range(1, 20):
#     globals()['aibool' + str(i)] = False
#     print(globals()['aibool' + str(i)])
#     print(i)

#将上面的布尔值储存到josn文件中，"bool1": bool1,这样的格式
def chushihuajson():
    #判断文件是否存在，如果不存在就创建一个，存在就删除原来的，创建一个新的
    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'w') as f:
        json.dump({"bool_1": bool_1,"bool_2": bool_2,"bool_3": bool_3,"aibool1": aibool1,"aibool2": aibool2,"aibool3": aibool3,"aibool4": aibool4,"aibool5": aibool5,"aibool6": aibool6,"aibool7": aibool7,"aibool8": aibool8,"aibool9": aibool9,"aibool10": aibool10,"aibool11": aibool11,"aibool12": aibool12,"aibool13": aibool13,"aibool14": aibool14,"aibool15": aibool15,"aibool16": aibool16,"aibool17": aibool17,"aibool18": aibool18,"aibool19": aibool19}, f)

    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'r') as f:
        data = json.load(f)
#定义一个修改json文件的函数，最多接收37个参数，最少接收一个参数，分别是37个布尔值
def updatajson(required_arg, *args, **kwargs):
    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'r') as f:
        data = json.load(f)
    data[required_arg] = args[0]
    with open('E:/pythonxiangmu/sc2/resource/tongxin.json', 'w') as f:
        json.dump(data, f)

#定义三个小数，用来存储三个confidence的值
confidence1 = 0.5
confidence2 = 0.8
confidence3 = 0.8
confidence4 = 0.7

typeofaiall =[]
#人族路径
typeofaiall.append('E:/pythonxiangmu/sc2/resource/t/tujituan.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/t/jiushibubingtuan.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/t/anyingkejituan.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/t/zhanzhengjixietuan.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/t/jiushijixietuan.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/t/diguozhandouqun.png')

#神族路径
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/dashijixie.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/buzhanjijia.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/kalaidexiwang.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/aierxianfeng.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/zuzhangzhijun.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/anyingxirao.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/zuzhangzhijun.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/p/fengbaopolin.png')

#虫族路径
typeofaiall.append('E:/pythonxiangmu/sc2/resource/z/baozhaweixie.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/z/zishengfuhua.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/z/zhetianbiri.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/z/sinuekuosan.png')
typeofaiall.append('E:/pythonxiangmu/sc2/resource/z/qinluechongqun.png')

# 定义一个储存15个文件路径的列表,储存了15个地图的图片
map_pictures = []
# 添加地图文件路径
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/heianshaxing.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/jihuimiaomang.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/jingwangxingdong.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/kehaliehen.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/ronghuoweiji.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/shenggezhilian.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/siwangyaolan.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/tianjiefengsuo.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/wangrishenmiao.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/xukongjianglin.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/xukongsilie.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/yanmiekuaiche.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/yingjiukuanggong.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/wangzhezhiye.png')
map_pictures.append('E:/pythonxiangmu/sc2/resource/ditu/jutiechengbing.png')

#github地址：

def dating():
    app = QApplication(sys.argv)
    widget = MyWidget("现在处于大厅界面")
    while True:
        button_location_1 = pyautogui.locateOnScreen('E:/pythonxiangmu/sc2/resource/dating.png', region=(0, 0, 737, 69),
                                                     grayscale=True, confidence=confidence1)
        if button_location_1 is not None:
            widget.show()
            widget.zhiding()
            QTimer.singleShot(2000, widget.close)
            app.exec_()
            break
    app.quit()

def ditushibie():
    while True:
        #如果是与第一个路径匹配的图片，就打开第一个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[0],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            global bool1
            bool1=True
            heianshaxing()
            import main7
            break
        #如果是与第二个路径匹配的图片，就打开第二个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[1],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            global bool2
            bool2 = True
            jihuimiaomang()
            import jihuimiaomangallh
            break
        #如果是与第三个路径匹配的图片，就打开第三个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[2],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            jingwangxingdong()
            global bool3
            bool3=True
            print('jingwangxingdong')
            import main9
            break
        #如果是与第四个路径匹配的图片，就打开第四个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[3],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            kehaliehen()
            global bool4
            bool4=True
            print('kehaliehen')
            import main10
            break
        #如果是与第五个路径匹配的图片，就打开第五个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[4],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            ronghuoweiji()
            global bool5
            bool5=True
            print('ronghuoweiji')
            import main11
            break
        #如果是与第六个路径匹配的图片，就打开第六个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[5],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            shenggezhilian()
            global bool6
            bool6=True
            print('shenggezhilian')
            import main12
            break
        #如果是与第七个路径匹配的图片，就打开第七个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[6],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            siwangyaolan()
            global bool7
            bool7=True
            print('siwangyaolan')
            import main13
            break
        #如果是与第八个路径匹配的图片，就打开第八个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[7],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            tianjiefengsuo()
            global bool8
            bool8=True
            print('tianjiefengsuo')
            import main14
            break
        #如果是与第九个路径匹配的图片，就打开第九个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[8],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            wangrishenmiao()
            global bool9
            bool9=True
            print('wangrishenmiao')
            import main15
            break
        #如果是与第十个路径匹配的图片，就打开第十个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[9],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            xukongjianglin()
            global bool10
            bool10=True
            print('xukongjianglin')
            import main16
            break
        #如果是与第十一个路径匹配的图片，就打开第十一个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[10],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            xukongsilie()
            global bool11
            bool11=True
            print('xukongsilie')
            import main17
            break
        #如果是与第十二个路径匹配的图片，就打开第十二个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[11],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            yanmiekuaiche()
            global bool12
            bool12=True
            print('yanmiekuaiche')
            import main18
            break
        #如果是与第十三个路径匹配的图片，就打开第十三个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[12],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            yingjiukuanggong()
            global bool13
            bool13=True
            print('yingjiukuanggong')
            import main19
            break
        #如果是与第十四个路径匹配的图片，就打开第十四个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[13],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            wangzhezhiye()
            global bool14
            bool14=True
            print('wangzhezhiye')
            import main20
            break
        #如果是与第十五个路径匹配的图片，就打开第十五个窗口
        button_location_2 = pyautogui.locateOnScreen(map_pictures[14],region=(853,47,1067,109),grayscale=True,confidence=confidence2)
        if button_location_2 is not None:
            jutiechengbing()
            global bool15
            bool15=True
            print('jutiechengbing')
            import main21
            break

def find_race():
    terran = 'E:/pythonxiangmu/sc2/resource/terran.png'
    protoss = 'E:/pythonxiangmu/sc2/resource/protoss.png'
    zerg = 'E:/pythonxiangmu/sc2/resource/zerg.png'

    #将图片路径添加到列表中
    race_pictures=[terran,protoss,zerg]

    #在(1837,284,1919,799)区域内轮巡查找图片，是否在race_pictures列表中的图片中，如果找到了，就打开窗口，10s后关闭窗口
    while True:

        button_location_3 = pyautogui.locateOnScreen(race_pictures[0],region=(1837,284,1919,799),grayscale=True,confidence=confidence3)
        if button_location_3 is not None:
            global bool_1
            bool_1=True
            terran_t()
            updatajson('bool_1',bool_1)
            break
        button_location_3 = pyautogui.locateOnScreen(race_pictures[1],region=(1837,284,1919,799),grayscale=True,confidence=confidence3)
        if button_location_3 is not None:
            global bool_2
            bool_2=True
            protoss_p()
            updatajson('bool_2',bool_2)

            break
        button_location_3 = pyautogui.locateOnScreen(race_pictures[2],region=(1837,284,1919,799),grayscale=True,confidence=confidence3)
        if button_location_3 is not None:
            global bool_3
            bool_3=True
            zerg_z()
            updatajson('bool_3',bool_3)
            break
    time.sleep(0.1)

def typeofai():
    while True:
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[0], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool1
            aibool1 = True
            updatajson('aibool1',aibool1)
            subprocess.Popen(["python", "dangqianTai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[1], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool2
            aibool2 = True
            updatajson('aibool2',aibool2)
            subprocess.Popen(["python", "dangqianTai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[2], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool3
            aibool3 = True
            updatajson('aibool3',aibool3)
            subprocess.Popen(["python", "dangqianTai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[3], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool4
            aibool4 = True
            updatajson('aibool4',aibool4)
            subprocess.Popen(["python", "dangqianTai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[4], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool5
            aibool5 = True
            updatajson('aibool5',aibool5)
            subprocess.Popen(["python", "dangqianTai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[5], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool6
            aibool6 = True
            updatajson('aibool6',aibool6)
            subprocess.Popen(["python", "dangqianTai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[6], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool7
            aibool7 = True
            updatajson('aibool7',aibool7)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[7], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool8
            aibool8 = True
            updatajson('aibool8',aibool8)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[8], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool9
            aibool9 = True
            updatajson('aibool9',aibool9)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[9], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool10
            aibool10 = True
            updatajson('aibool10',aibool10)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[10], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool11
            aibool11 = True
            updatajson('aibool11',aibool11)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[11], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool12
            aibool12 = True
            updatajson('aibool12',aibool12)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[12], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool13
            aibool13 = True
            updatajson('aibool13',aibool13)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[13], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool14
            aibool14 = True
            updatajson('aibool14',aibool14)
            subprocess.Popen(["python", "dangqianPai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[14], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool15
            aibool15 = True
            updatajson('aibool15',aibool15)
            subprocess.Popen(["python", "dangqianZai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[15], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool16
            aibool16 = True
            updatajson('aibool16',aibool16)
            subprocess.Popen(["python", "dangqianZai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[16], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool17
            aibool17 = True
            updatajson('aibool17',aibool17)
            subprocess.Popen(["python", "dangqianZai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[17], region=(1447, 96, 1919, 767), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool18
            aibool18 = True
            updatajson('aibool18',aibool18)
            subprocess.Popen(["python", "dangqianZai.py"])
            break
        button_location_4 = pyautogui.locateOnScreen(typeofaiall[18], region=(1451, 476, 1849, 708), grayscale=True, confidence=confidence4)
        if button_location_4 is not None:
            global aibool19
            aibool19 = True
            updatajson('aibool19',aibool19)
            subprocess.Popen(["python", "dangqianZai.py"])
            break

if __name__ == '__main__':
    chushihuajson()
    dating()
    ditushibie()

