import os
import random
import time
import win32api, win32con, win32gui


def ProcessRecievedData():
	file1 = open(os.path.realpath(r'.\SENSOR_DATA\Sensor1.txt'),"r") 
	Sensor1_Data=int(file1.read())
	file1.close()
	file1 = open(os.path.realpath(r'.\SENSOR_DATA\Sensor2.txt'),"r") 
	Sensor2_Data=int(file1.read())
	file1.close()
	if(Sensor1_Data==Sensor2_Data and Sensor1_Data==1):
		print("green")
		path = os.path.realpath(r'.\green.jpg')
		setWallpaper(path)
	elif(Sensor1_Data==Sensor2_Data and Sensor1_Data==0):
		print("red")
		path = os.path.realpath(r'.\red.jpg')
		setWallpaper(path)
	else:
		print("Normal")
		path = os.path.realpath(r'.\normal.png')
		setWallpaper(path)

def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

while (1):
	file1 = open(os.path.realpath(r'.\SENSOR_DATA\Sensor1.txt'),"w") 
	file1.write(str(random.randint(0,1))) 

	file1.close()

	file1 = open(os.path.realpath(r'.\SENSOR_DATA\Sensor2.txt'),"w") 
	file1.write(str(random.randint(0,1))) 

	file1.close()
	ProcessRecievedData()
	time.sleep(2)



