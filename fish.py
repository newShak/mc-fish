# ! python 3
import pyautogui as pa
import pynput.keyboard as pu
import keyboard as kb
import time
import sys


startFish= pu.Key.f9
stopFish= 'f10'
exitProcess='f8'
exitProcessKey=pu.Key.f8
getFishPng = "getFish.png"
mouseDown=pu.Key.f7
mouseUp=pu.Key.f8
#print(pressButton == releaseButton)
def on_press(button):
      #print(pressButton == button)
      x, y=pa.position()
      print("按下了{}".format(button))
      #print("按下了{}".format(button))
      if(button==mouseDown):
          print("按下左键")
          pa.mouseDown(x,y,'left')
      if(button==mouseUp):
          print("松开左键")
          pa.mouseUp(x,y,'left')
      if (button ==startFish) :
          print("开始钓鱼")
          while(True):
            #检测是否停止循环
            if kb.is_pressed(stopFish):
              break
            if kb.is_pressed(exitProcess):
              sys.exit()
            #x, y=pa.position()
            loca=pa.locateOnScreen(getFishPng, confidence=0.8, grayscale=True)
            #loca=pa.locateOnScreen(getFishPng)
            if loca !=None:
              print("捕获到收杆标识")
              #获取到浮漂下沉的标识，收回并再次抛出
              pa.rightClick()
              #睡眠0.5s防止抛竿过快使得鱼漂没有在正常位置
              time.sleep(0.5)
              pa.rightClick()
              #随眠3s防止检测过快
              time.sleep(3)
            else:
              print("没有捕获到收杆标识")
            #time.sleep(0.2)

def p_thread():
  while(1):
     with pu.Listener(on_press=on_press) as puListener:
           puListener.join()

p_thread()
    