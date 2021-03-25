import json, requests

with open("config/online.json") as f:
    config = json.load(f)

def getCookie(name):
    request = requests.post(config[name] + "/getCookie").text
    splitedcookie = request.split("~")
    decryptedcookie = dict()
    for thing in splitedcookie:
        thingsplitted = thing.split("=")
        decryptedcookie.update({thingsplitted[0]:thingsplitted[1]})
    response = {
        "encryptedcookie": request,
        "decryptedcookie": decryptedcookie
    }
    return decryptedcookie

def removeCookie(name, cookie):
    requests.post(config[name] + "/removeCookie?cookie=" + cookie)

def getServerTime(name, cookie):
    request = requests.get(config[name] + "/getServerTime?cookie=" + cookie)
    return int(request.text)

class Custom:
    def getCustomShop(name, cookie):
        request = requests.get(config[name] + "/Custom/getCustomShop?cookie=" + cookie)
        return json.loads(request.text)
    def getMapJson(name, id, cookie):
        request = requests.get(config[name] + "/Custom/getMapJson?id=" + str(id) + "&cookie=" + cookie)
        return json.loads(request.text)
    def downloadLinksMap(name, id, cookie):
        request = requests.get(config[name] + "/Custom/downloadLinksMap?id=" + str(id) + "&cookie=" + cookie)
        return json.loads(request.text)
    def downloadZipFile(path, url):
        filename = url.split("/")[-1]
        with open(path + filename, "wb") as f:
            f.write(requests.get(url).content)

class OnlineMultiPlayer:
    def connectToRoom(name, id, cookie):
        request = requests.get(config[name] + "/OnlineMultiPlayer/connectToRoom?room=" + str(id) + "&cookie=" + cookie)
        return json.loads(request.text)
    def checkChat(name, id, cookie):
        request = requests.get(config[name] + "/OnlineMultiPlayer/checkChat?room=" + str(id) + "&cookie=" + cookie)
        return json.loads(request.text)
    def sendMessage(name, message, id, cookie):
        request = requests.get(config[name] + "/OnlineMultiPlayer/sendMessage?msg=" + message + "&room=" + str(id) + "&cookie=" + cookie)
        return json.loads(request.text)
    def getOnlineJSON(name, id, cookie):
        request = requests.get(config[name] + "/OnlineMultiPlayer/getGlobalOnlineJSON?room=" + str(id) + "&cookie=" + cookie)
        return json.loads(request.text)
    def updateScores(name, id, score, cookie):
        request = requests.get(config[name] + "/OnlineMultiPlayer/updateScores?room=" + str(id) + "&score=" + str(score) + "&cookie=" + cookie)
        return json.loads(request.text)