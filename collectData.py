import urllib.request,urllib.parse,urllib.error
import re
import json
import time


collectYear=int(input("Year: "))

collectDataTemp={"title":"", "protections":"", "releaseDate":"", "crackDate":""}
collectData=[]
fileName=str(collectYear)+".json"

try:
	with open(str(collectYear+1)+".page","r") as p:
		page=int(p.read())
except FileNotFoundError:
	page=0
	
	
	
while True:
	time.sleep(1)
	
	servUrl="https://api.crackwatch.com/api/games?page={}&is_aaa=true&is_released=true".format(page)
	with urllib.request.urlopen(servUrl) as html:
		data=html.read().decode()
		jsdata=json.loads(data)
		
		for item in jsdata:
			releaseDate=item["releaseDate"]
			releaseYear=int(re.findall("([0-9]+)-\S",releaseDate)[0])
			date=(re.findall("([0-9]+)-([0-9]+)-([0-9]+)\S",releaseDate)[0])
				
			
			if releaseYear==collectYear:
			
				for k in collectDataTemp:
					try:
						if type(item[k])==list:
							collectDataTemp[k]=str(item[k][0])
						else:
							collectDataTemp[k]=item[k]
					except KeyError as e:
						collectDataTemp[k]="uncracked"
					
				collectData.append(collectDataTemp.copy())
				print("Collecting: page({}) Date({}/{}/{})".format(page,date[2],date[1],date[0]))
				
			
			elif releaseYear>collectYear:
				break
			
			elif releaseYear<collectYear:
				print("Ending: page({}) Date({}/{}/{})".format(page,date[2],date[1],date[0]))
				
				with open(fileName,"w") as f:
					json.dump(collectData,f,ensure_ascii=False,indent=4)
				
				with open(str(collectYear)+".page","w") as p:
					p.write(str(page))
								
				exit()
	
	page+=1





