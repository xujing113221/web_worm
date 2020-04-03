#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import mysql.connector
import socket

def connectdb():
	db = mysql.connector.connect(user='root', passwd='xuJING3119',
                              # host='localhost',
                              # port='3306',
                              database='xujing',
                              use_unicode=True
                              )
	print ('Database is connected.')
	return db

def closedb(db):
	db.close()

def createTable(db,tbl):
	cursor = db.cursor()
	# stmt_drop = "DROP TABLE IF EXISTS {0}".format(tbl)		#delete table
	# cursor.execute(stmt_drop)
	t_create = ("CREATE TABLE IF NOT EXISTS {0} "
		"(id INT UNSIGNED AUTO_INCREMENT, "
		"likes FLOAT ,"
		"watch_times INT UNSIGNED,"
		"title VARCHAR(100) NOT NULL, "
		"html_url VARCHAR(150) NOT NULL,"
		"video_url VARCHAR(150) NOT NULL ,"
		"PRIMARY KEY (id))DEFAULT CHARSET=utf8;".format(tbl))
	cursor.execute(t_create)
	print('table is crated.')

def insertData(db,tbl,url):
	cursor = db.cursor()

	html = getHtml(url)
	[name,https] = getInfo(html)
	video_http = []
	global x
	for i in range(len(name)):
		hm = getHtml(https[i].encode('utf-8'))
		video_http.append(getVideo(hm))
		[rat,ts] = getLikeandTimes(hm)
		print ("%s is writing..." %x)
		stmt_insert = ("INSERT INTO {table} (likes, watch_times,title,html_url,video_url) VALUES "
                   "('{likes}','{times}','{title}','{html}','{video}')".format(table=tbl,\
                   	likes = rat, times = ts,\
                   	title=name[i].encode('utf-8'),\
                   	html=https[i].encode('utf-8'),\
                   	video=video_http[i]))
		cursor.execute(stmt_insert)
		db.commit()
		x += 1

def getHtml(url):
	for j in range(10):
		try:
			# page=urllib.request.urlopen(url,timeout = 5)
			page=urllib.urlopen(url)
			html=page.read()
			return html
		except:
			if j < 9:
				continue
			else :
				print 'URLError: <urlopen error timed out> All times is failed '
	

def getInfo(html):
	soup = BeautifulSoup(html,'lxml')
	name = []
	http = []
	for tag in soup.find_all("div","video"):
		name.append(tag.a['title'])
		http.append("http://www.avtbm.com%s" %tag.a['href'])
	return name,http

def getVideo(html):
	soup = BeautifulSoup(html,'lxml')
	tag = soup.find("source",type="video/mp4",label="360p")
	return tag['src']

def getLikeandTimes(html):
	soup = BeautifulSoup(html,'lxml')
	tag = soup.find("source",type="video/mp4",label="360p")
	like = soup.find("button",id = "rating",type = "button")
	times = soup.find_all("div", class_= "col-xs-12 col-sm-6 col-md-6",limit = 2)
	rat = float(like.text.strip()[0:2])/100
	ts = int(times[1].strong.text.strip())
	return rat,ts
	

def main():
	tb = 'avtb'
	db = connectdb()
	createTable(db,tb)
	socket.setdefaulttimeout(3) 		# set timeout 3s
	for page in range(500,540):
		url = 'http://www.avtbm.com/recent/%s/' %page
		print("=================Page%s is searching....=============" %(page-1))
		insertData(db,tb,url)
	print("write done!")
	closedb(db)

if __name__ == '__main__':
	x = 1
	main()
	
	



