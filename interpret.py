import json
import datetime
import re



years=2015,2016,2017,2018,2019

def identifyDRMs(years):
	DRMs=[]
	for year in years:
		fname=str(year)+".json"
		with open(fname,"r") as f:
			fdata=f.read()
			jsdata=json.loads(fdata)
			
			for item in jsdata:
				drm=item["protections"][0]
				
				if drm.lower() not in DRMs:
					DRMs.append(drm.lower())
	return(DRMs)


def crackedWithIn(rd,cd):
	if cd!="Uncracked":
		
		rdt=re.findall("([0-9]+)-([0-9]+)-([0-9]+)T\S",rd)[0]
		cdt=re.findall("([0-9]+)-([0-9]+)-([0-9]+)T\S",cd)[0]
		
		crackedwithin=datetime.datetime(int(cdt[0]),int(cdt[1]),int(cdt[2]))-datetime.datetime(int(rdt[0]),int(rdt[1]),int(rdt[2]))
		try:
			crackedwithin=int(re.findall("([0-9]+) days",str(crackedwithin))[0])
		except IndexError:
			crackedwithin=0
		
		return(crackedwithin)
		
	
	return("Uncracked")     


def rateDRM(drm):
	ratedrm={"DRM":drm,"Total":0,"7":0,"14":0,"21":0,"28":0,"56":0,"cracked in 56+ days":0,"Uncracked":0}
	uncrackedTitles=[]
	for year in years:
		fname=str(year)+".json"
		with open(fname,"r") as f:
			fdata=f.read()
			jsdata=json.loads(fdata)
			
			for item in jsdata:
				if item["protections"][0].lower()==drm:
					ratedrm["Total"]+=1
					try:
						rd=item["releaseDate"]
						cd=item["crackDate"]
					
					except KeyError:
						cd="Uncracked"
					
					cwi=crackedWithIn(rd,cd)
					
					
					if cwi=="Uncracked":
						ratedrm["Uncracked"]+=1
						uncrackedTitles.append(item["title"])
					elif cwi>56:
						i="cracked in 56+ days"
						ratedrm[i]+=1
					else:
						for k,v in ratedrm.items():
							try:
								if cwi<=int(k):
									ratedrm[k]+=1
									break
							except ValueError:
								pass					
					
					
	for k,v in ratedrm.items():
		try:
			kk="cracked in "+str(int(k))+" days: "
			print(kk,v)
		
		except ValueError:
			print(k+": ",v)
	
	
	print("uncracked titles:\n")
	for i in uncrackedTitles:
		print(i)
							

DRMs=identifyDRMs(years)

for drm in DRMs:
	rateDRM(drm)
	print("--"*10,"\n")
						
						
					
						
					
					
			
	
					
			
			
			
			
			
			
			
			
			