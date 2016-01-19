import sys
import urllib
import urllib3
import certifi
from bs4 import BeautifulSoup
import re
from ast import literal_eval
from joblib import Parallel, delayed
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
import multiprocessing
import json

key = "X5dHK6yyg_oBzywCz82z"

#I need to become  a data scientist.
def getDataToFrontEnd():
	print("IN GET DATA FRONT END")
	list = ["http://biz.yahoo.com/p/6conameu.html", "http://biz.yahoo.com/p/1conameu.html", "http://biz.yahoo.com/p/2conameu.html", 
	"http://biz.yahoo.com/p/3conameu.html", "http://biz.yahoo.com/p/5conameu.html", "http://biz.yahoo.com/p/7conameu.html", "http://biz.yahoo.com/p/8conameu.html", 
	 "http://biz.yahoo.com/p/9conameu.html"]
	

	jsonStr= "{  \"children\" : ["
	for url in list:
		html = urllib.urlopen(url).read()
		print(html) #then you want to parse ht edata into the data visualization. 
		print("Finding items")
		pattern =  re.compile("(.*)More Info<\/a><\/font><\/td><\/tr><tr><td\nnowrap\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)")
	#regex (.*)More Info<\/a><\/font><\/td><\/tr><tr><td\nnowrap\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)
		title_pattern = re.compile("Industry\nBrowser - (.*)- Industry List", re.S)
		title = title_pattern.findall(html)
		print(title[0])
		if title[0].replace(" ", "") != "ConglomeratesSector":
			print("NOT CONGLOMERATES")
			jsonStr+="{ \"name\": \""+ title[0]+"\" , \"children\" :{"
			print(title)
			print jsonStr
			html = pattern.findall(html)
			print(html) 
			if html is not None:
				try:
					print(type(html))
					for item in html: 

						for part in item: 
							if "</font></a></td><td" in part: 
								part = part.replace("/font></a></td><td", "")
								part= part.replace("-","")
								part = part.replace("&", "")
								part = part.replace("<", "")
								part = part.replace("size=-1>", "")
								part = part.replace("size=1>", "")

								jsonStr+=" \""+part +"\" : "

							if "</font></td><td" in part:
								part = part.replace("</font></td><td", "")
								part = part.replace("size=-1>", "") 
								part = part.replace("size=1>", "")
								print(part)
								jsonStr += part+", "


				except: 
					print("This is the url")
			jsonStr  = jsonStr[:-2]
			jsonStr +="}}, "

	print("NOW")
	print(jsonStr)
	jsonStr = jsonStr[:-2]
	print("After trimming")
	print(jsonStr)
	jsonStr +="]}"
	print(jsonStr)
	jsonStr = json.loads(jsonStr)
	return jsonStr



getDataToFrontEnd()
			
			#prune out the numbers that matter the most. 
		#and then now you want to entire this data into a way for D3.js will understand. 










