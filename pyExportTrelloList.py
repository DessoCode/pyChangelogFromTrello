
import urllib
import json
import time
import sys
from urllib.request import urlopen


#Check for py plugins
import subprocess

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

#Open the json file where the api keys are stored. 
#check if file exists
try:
	with open('TrelloKeys.json', encoding="utf8") as f:
		keys = json.load(f)
except FileNotFoundError:
	print('TrelloKeys.json was not found.')
	input('Press ENTER to exit')


#get API keys out of the TrelloKeys.json
api_key = keys['key']
api_token = keys['token']
api_boardId = keys['boardId']

boardURL = 'https://api.trello.com/1/boards/' + api_boardId + '?key=' + \
            api_key + '&token=' + api_token + '&fields=all&cards=all&card_fields=all&pluginData=true&card_pluginData=true&lists=all'
response = urllib.request.urlopen(boardURL)
jsonFile=response.read()
data = json.loads(jsonFile)
boardName = data['name']
print('***********************')
print(boardName)
print('***********************')

print("What is the name of the list you want to export?")
listName = input()
#print(data['lists'])
for lists in data['lists']:
    #print(lists['name'])
    if(listName == lists['name']):
        print('***List has been found***')
        listId = lists['id']
    # else:
    #     sys.exit("ERROR: Done 13-02-2019COULD NOT FIND LIST....")
    #     break
time.sleep(0.5)
print('list id is:' + listId)
time.sleep(0.5)
toPasteTxt = listName + ':\n'
print('-------------------The Changelog Is---------------------')
for cards in data['cards']:
    if(listId == cards['idList']):
        changeTxt = '* '+ cards['name']
        toPasteTxt += changeTxt + '\n'
        print(changeTxt)
        time.sleep(0.1)
print('--------------------------------------------------------')


#see if pyperclip is in installed_packages
if 'pyperclip' in installed_packages:
    import pyperclip
    pyperclip.copy(toPasteTxt)
    print('Your changelog is now under your clipboard. CTRL+V to paste it somewhere!')



input('Press ENTER to exit')
