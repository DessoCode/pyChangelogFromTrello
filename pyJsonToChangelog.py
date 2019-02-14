import json
import time
import sys

print("What is the json filename?")
file = input()
file_directory = file +'.json'
time.sleep(0.5)
print(file_directory + " was loaded...")
json_data=open(file_directory, encoding="utf8").read()
data = json.loads(json_data)
time.sleep(0.5)
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
print('-------------------The Changelog Is---------------------')
for cards in data['cards']:
    if(listId == cards['idList']):
        changeTxt = '* '+ cards['name']
        print(changeTxt)
        time.sleep(0.1)



print('--------------------------------------------------------')
print('Press a key to close')
key = input()
