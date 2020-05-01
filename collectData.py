import urllib.request, urllib.parse, urllib.error
import json
import re
import time



def CollectDataManager(year):
	

	page=pageOpt(year)
	curryear=2020
	file=str(year)+".json"
	
	while True:
		#dont remove time.sleep(), else risk ip-ban
		time.sleep(1)
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
	with urllib.request.urlopen(URL) as html:
		print("\rStarting..",end="")
		
		data=html.read().decode()
		jsdata=json.loads(data)
			
		with open(filename,"w",encoding="utf-8") as f:
			json.dump(jsdata,f,ensure_ascii=False,indent=4)
			print("\r--done--",end="")


def pageOpt(year):
	if 2019-year<1:
		rerurn(0)
	else:
		return((2019-year)*4)




year=int(input("Collection Year: "))

CollectDataManager(year)
	
	