# -*- coding: utf-8 -*-
import os
import webbrowser
from weibopy.auth import OAuthHandler
from weibopy.api import API 
import time  


app_key = '3697114952'
app_secret = '616611de12d73ba6769e7967e03356b6'
#vmonit
#access_token_key = '4263fa4f1ab9c655ff2adaf53efb4a15'
#acces_token_secret = '7b3994d665882c6fe16bc2453217867a'

#videomonit
access_token_key = '0d51053f97027a7f4651e36071120615'
acces_token_secret = '614a6ec600bfdcb6d29728e120ebda73'

auth = OAuthHandler(app_key, app_secret)
#url = auth.get_authorization_url()
#webbrowser.open(url)
#verifier  = raw_input("PIN:").strip()
#token = auth.get_access_token(verifier)
#print token.key, " ", token.secret
auth.setToken(access_token_key, acces_token_secret)
api = API(auth)

text_list = [" 我家的摄像头正在摄像"," 看看我家楼下的车，我家的摄像头正在拍摄"," 测试中，我家的摄像头正在拍摄", " 过段时间把它移到室内，出门开始监控，我家的摄像头正在拍摄","..，我家的摄像头正在摄像", " 共享摄像头，我家的摄像头正在拍摄"," 我是一个摄像头，我没有在偷拍哦！", "难道我会告诉你我在偷看吗？"]
def ShareSnapToWeibo(now_time):
	try:
		second = int(time.strftime('%S', now_time))
		file_name = 'snapshots/'+time.strftime('%Y-%m-%d %H-%M-%S', now_time) + '-image.png'
		status_text = time.strftime('%Y年%m月%d日 %H点%M分%S秒', now_time)+ text_list[second % 7]
		status = api.upload(file_name, status_text,  lat='12.3', long='45.6')#text_list[second % 6])
		print "Share Success"
	except Exception as e:
		print "Share Error:%s" % e
		return
if __name__ == '__main__':
	api.update_status("test")