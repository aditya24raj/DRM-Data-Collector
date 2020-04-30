import urllib.request, urllib.parse, urllib.error
import json
import re
import time
import sys
import random


def CollectDataManager(year):
	

	page=pageOpt(year)
	curryear=2020
	file=str(year)+".json"
	
	while True:
		time.sleep(random.randint(1,4))
		servUrl="https://api.crackwatch.com/api/games?page={}&is_aaa=true&is_released=true".format(page)
		
		
		with urllib.request.urlopen(servUrl) as html:
			data=html.read().decode()
			jsdata=json.loads(data)
			
			rd=jsdata[0]["releaseDate"]
			curryear=int(re.findall("([0-9]+)-\S",rd)[0])
			
			if curryear!=year:
				if curryear>year:
					pass
				elif curryear<year:
					break
				print("\rskipping:",curryear,end="")
			
			else:
				CollectData(servUrl,file)
				collectedtill=re.findall("([0-9]+-[0-9]+-[0-9]+)T\S",jsdata[-1]["releaseDate"])
				print(collectedtill)
			
			page+=1

		

def CollectData(URL,filename):
	
	while True:
		with urllib.request.urlopen(URL) as html:
			print("\rStarting..",end="")
			
			data=html.read().decode()
			jsdata=json.loads(data)
			
			with open(filename,"w",encoding="utf-8") as f:
				json.dump(jsdata,f,ensure_ascii=False,indent=4)
				print("\r--done--",end="")
				break

def pageOpt(year):
	if 2019-year<1:
		rerurn(0)
	else:
		return((2019-year)*4)




year=2015

CollectDataManager(year)
	
	