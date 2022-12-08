from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
#https://www.agame.com/game/magic-piano-tiles

# X:  245 Y:  450 RGB: ( 89,  91, 117)

# X:  326 Y:  450 RGB: (  0,   0,   0)


# X:  407 Y:  450 RGB: ( 92,  94, 118)

# X:  489 Y:  450 RGB: ( 91,  93, 118)
print('Start! ')
print('If you want to end, press q')
def click(x,y):
    win32api.SetCursorPos((x,y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #tốc độ click của chuột
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
	#khi thấy màu đen thì code đi vào hàm click() ở các vị trí
	if pyautogui.pixel(245,450)[0] == 0:
		click(245,450)
	if pyautogui.pixel(326,450)[0] == 0:
		click(326,450)
	if pyautogui.pixel(407,450)[0] == 0:
		click(407,450)
	if pyautogui.pixel(489,450)[0] == 0:
		click(489,450)