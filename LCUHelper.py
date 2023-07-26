import subprocess, re, requests, base64, json, time
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def encodeBase64Token(rawAuthToken: str):
    auth_token_bytes = rawAuthToken.encode("ascii")    
    base64_bytes = base64.b64encode(auth_token_bytes)
    return str(base64_bytes)[2:-1]

def getPortPassLCU():
    infoLCU = []
    outputCMD = subprocess.getoutput('wmic PROCESS WHERE name="LeagueClientUx.exe" GET commandline')
    if outputCMD.__len__() > 1000:
        port = re.search(r"(--app-port=([0-9]*))", outputCMD).group(2)
        password = re.search(r"(--remoting-auth-token=([\w-]*))", outputCMD).group(2)
        infoLCU.append(port)
        infoLCU.append(password)

        #index "0" -> port, "1" -> password
        return infoLCU

class LCUHelper:

    def __init__(self, port: str, password: str, isStopThreading = False):
        self.port = port
        self.password = password
        self.isStopThreading = isStopThreading

    def getDataSummoner(self):
        dataSummoner = []
        if self.port != None and self.password != None:

            urlLCU = f"https://127.0.0.1:{self.port}/lol-summoner/v1/current-summoner"
            authTokenLCU = "Basic " + encodeBase64Token(f"riot:{self.password}")
            headers = {
                "Authorization": authTokenLCU
            }

            resultData = requests.get(urlLCU, headers=headers, verify=False)
            dataSummoner.append(resultData.json()['displayName']) #--> index 0
            dataSummoner.append(str(resultData.json()['summonerLevel'])) #--> index 1
            dataSummoner.append(str(resultData.json()['summonerId'])) #--> index 2

        return dataSummoner
    
    def getAvailableChamps(self):
        dataChamps = []
        if self.port != None and self.password != None:

            urlLCU = f"https://127.0.0.1:{self.port}/lol-champions/v1/owned-champions-minimal"
            authTokenLCU = "Basic " + encodeBase64Token(f"riot:{self.password}")
            headers = {
                "Authorization": authTokenLCU
            }

            resultData = requests.get(urlLCU, headers=headers, verify=False).json()
            for champ in resultData:
                dataChamps.append({
                    "id": str(champ['id']),
                    "name": champ['name']
                })

        return dataChamps

    def quickPickChamp(self, summonerId: str, ChampionId: str, flagsLockChamp):
        while True:
            if self.isStopThreading:
                break
            urlLCU = f"https://127.0.0.1:{self.port}/lol-champ-select/v1/session"
            authTokenLCU = "Basic " + encodeBase64Token(f"riot:{self.password}")
            headers = {
                "Authorization": authTokenLCU
            }
            while True:
                if self.isStopThreading:
                    break          
                resultData = requests.get(urlLCU, headers=headers, verify=False)
                cellID = 0
                if resultData.status_code == 200:
                    resultData =resultData.json()
                    for test1 in resultData['myTeam']:
                        if test1['summonerId'] == summonerId:
                            cellID = test1['cellId']
                    for test1 in resultData['actions'][0]:
                        if test1['actorCellId'] == cellID:
                            actionID = test1['id']

                    if flagsLockChamp:
                        data = json.dumps({
                                "championId": re.search(r"(.*?) -", ChampionId).group(1),
                                "completed": True
                        })
                    else:
                        data = json.dumps({
                                "championId": re.search(r"(.*?) -", ChampionId).group(1),
                                "completed": False
                        })

                    urlLCU = f"https://127.0.0.1:{self.port}/lol-champ-select/v1/session/actions/{actionID}"
                    requests.patch(urlLCU, headers=headers, data=data, verify=False).status_code
                    break
                else:
                    time.sleep(0.5)




