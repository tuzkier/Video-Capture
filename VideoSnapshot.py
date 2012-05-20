# -*- coding: utf-8 -*-  
from VideoCapture import Device
import time
import sys

cam = Device(1,0)
def SnapShotRealTime():
	now_time = time.localtime()
	cam.saveSnapshot('snapshots/'+time.strftime('%Y-%m-%d %H-%M-%S', now_time) + '-image.png',timestamp=5, boldfont=1, quality=75)
	return now_time