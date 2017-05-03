import requests
import simplejson as json
import os
import time

def lookUp(summoner):
	if 0 == 1:	
		api = open("apikey")
		key = api.read()
		api.close()
	else:
		key = str(os.environ.get('apikey',-1))
	if(key == -1):
		return "No API key found"

	url1 = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner.lower() + "?api_key=" + key

	userReq = requests.get(url1)
	if(userReq.status_code == "404"):
		return "User not found"
	dic = {}
	try:
		print(userReq.text)
		dic = json.loads(userReq.text)
		url2 = "https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + str(dic['id']) + "?&api_key=" + key
		userMatch = requests.get(url2)
		dic = json.loads(userMatch.text)
		data = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ': '))
		print(dic)
		t = (time.time()-float(dic['gameStartTime'])/1000)	
		print(t)

		string = str(	"Ingame for " + str(int(t/60)) + " minutes and " + str(int(t%60)) + " seconds." 	)
		return string
	except:
		return "Not in game"