import json
import time
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
        print('MATCH!!!')
        listId = lists['id']
time.sleep(0.5)
print('list id is:' + listId)
time.sleep(0.5)
for cards in data['cards']:
    if(listId == cards['idList']):
        print(cards['name'])
#print(data['lists'][0]['id'])
#print(data['cards'][2]['name'])
