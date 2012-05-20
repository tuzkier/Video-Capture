# -*- coding: utf-8 -*-
import weibo
import VideoSnapshot
import time

if __name__ == '__main__':
	end = raw_input("结束时间(小时)：")
	while True:
		hour = int(time.strftime('%H', time.localtime()))
		if hour > end:
			break
		now_time = VideoSnapshot.SnapShotRealTime()
		weibo.ShareSnapToWeibo(now_time)
		print str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())) + " 发送"
		time.sleep(120)