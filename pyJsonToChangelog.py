import json
import time
import sys

#Check for py plugins
import subprocess

#Check for py plugins
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

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



print('Press a key to close')
key = input()
