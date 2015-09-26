#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by Watson from BomiBar(http://tieba.baidu.com/f?kw=尹普美)

import urllib2  
import urllib  
import requests
import re
import os
import sys
import datetime
#step1: collect the recent updates of all websites and compare with last_collect
print u"^.^ by Tso from BomiBar ^.^"
print u"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
ToBupdated =open("ToBupdated.txt","w")

jintianriqi=datetime.date.today()
jintianriqi=str(jintianriqi)
print jintianriqi
anyUpdate=0
pattern0=re.compile("http\:\/\/(.+?)\.tistory\.com\/(.+)")
recentestPosts=[]
last_collect=open("last_collect.txt")
for line in last_collect:
	
	m0=re.search(pattern0,line)
	if m0:
		lastpage=m0.group(2)
		foldername=m0.group(1)+u'''站的第'''+m0.group(2)+u'''个post'''
		print m0.group(1)+u'''站:'''
		#print u'''上次收图收到''', foldername
		#find if there's any new update
		lastpage_int=int(lastpage)
		myUrl='http://'+m0.group(1)+'.tistory.com/'
		headers = {  
			'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
		}  
		req = urllib2.Request(  
			url=myUrl,
			headers = headers  
		) 				
		try:
			result = urllib2.urlopen(req, timeout=10)  
			tempt =open("temp","w")
			
			
			print >> tempt, result.read()  
			#print u"临时主站网页文件已生成"		
			tempt.close()
			#analyze the webpage
			f=open('temp','rb')
			lines = f.readlines()
			
			done=0
			for line in lines:
				if done==0:
					pattern1= re.compile("<a href=\"/(\d+)\"")
					m1=re.search(pattern1,line)
					if m1:
						
						recentPost=m1.group(1)
						recentPost_int=int(recentPost)
						myUrl='http://'+m0.group(1)+'.tistory.com/'+recentPost
						recentestPosts.append(myUrl)
						done=1
						
			f.close()
			#print lastpage_int
			if recentPost_int==lastpage_int:
				print u"无更新"
			else:
				anyUpdate=1
				while recentPost_int-lastpage_int>0:
					myUrl='http://'+m0.group(1)+'.tistory.com/'+str(recentPost_int)
					print myUrl
					headers = {  
						'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
					}  
					req = urllib2.Request(  
						url=myUrl,
						# data = postdata,  
						headers = headers  
					) 
					try:			
						result = urllib2.urlopen(req, timeout=10)  
					
						temptt =open("temptt","w")
						print >> temptt, result.read()  
						#print u"临时帖子网页文件已生成"						
						ff=open('temptt','rb')
						lines = ff.readlines()
						for line in lines:
							#find event name
							pattern3= re.compile("title\" content=\"(.*)\" >")
							m3=re.search(pattern3,line)
							if m3:
								title=m3.group(1)
								print >> ToBupdated , title,'['+m0.group(1)+']'
								
						
						print >> ToBupdated ,myUrl
						
						
						ff.close()
						temptt.close()
					except:	
						print u"这个帖子已被原po删除!"   #出现异常的处理方法
						
						#sys.exit()	
					recentPost_int=recentPost_int-1
					# nextpage=nextpage+1
				os.remove('temptt')			# 
		except:	
			print u"这个站子貌似关了!"   #出现异常的处理方法
					
last_collect.close()						
ToBupdated.close()	
os.system('python KR2CN.py')
if(anyUpdate==1):
	# 
	
	last = raw_input('修改准备'.decode('utf-8').encode('gbk'))	
	os.system("\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\" ToBupdated_CN.txt")
	# os.system('ToBupdated_CN.txt')
else:
	last = raw_input('所有收的图都是最新的，那些站子里面没有任何一家更新了。'.decode('utf-8').encode('gbk'))	



	
os.remove('temp')	
tbudd=open('ToBupdated_CN.txt','r')
os.makedirs(jintianriqi) 
os.chdir(jintianriqi)
#step2: save all the new posts from all the websites
for line in tbudd:
	pattern4= re.compile("http")
	m4=re.search(pattern4,line)
	if m4:
		myUrl=line
		headers = {  
			'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
		}  
		req = urllib2.Request(  
			url=myUrl,
			# data = postdata,  
			headers = headers  
		) 

		result = urllib2.urlopen(req)  

		tiezi =open("tiezi.html","w")
		print >> tiezi ,result.read()  
		# print u"临时网页文件已生成"
		count=0
		for line in open("tiezi.html"):
			pattern2= re.compile("__setTitle\(\"(.*)\"")
			m2=re.search(pattern2,line)
			if m2:
				
				folder2=m2.group(1)
				# print folder2.decode('utf8')#.encode('gbk')
				################
			# pattern = re.compile("dir=\"(.+?\/original\/(.+?))\"")
			pattern = re.compile("(http://cfile\d+\.uf\.tistory\.com/original/([A-Za-z0-9]+))")
			# http://cfile1.uf.tistory.com/original/2453B24555C396F927591E
			m1=re.findall(pattern,line)
			if m1:
				for ones in m1:
					count=count+1
					print ones[0]
					pic_url = ones[0]
					# print '\n=====================\n'
					print ones[1]
					filename=ones[1]
					filename = filename+".jpg"
					path=os.path.join(foldername, filename) 
					pic_data = urllib.urlopen(pic_url).read()  
					f = file(path,"wb")  
					f.write(pic_data)  
					f.close() 
		tiezi.close()		
		os.remove('tiezi.html')		
		print u"共保存了",count,u"个图片文件"
	else:
		foldername=line.decode("UTF-8").encode("GBK", 'ignore').rstrip()
		if not os.path.exists(foldername): 
			os.makedirs(foldername)
			# path2=os.path.join(jintianriqi, foldername)
			# 		
			# os.makedirs(foldername) 	
			
#step3: modify the "last_update.txt"
os.chdir('C:\Users\WANG\Desktop\GetPic')
os.remove('last_collect.txt')	
last_collect=open("last_collect.txt","w")
for theurl in recentestPosts:
	print >> last_collect, theurl
last_collect.close()
last = raw_input('按回车键关闭程序并打开本次收图日志'.decode('utf-8').encode('gbk'))	
		
		
