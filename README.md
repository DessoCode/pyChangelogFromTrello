# pyExportTrelloList

## What it does
This python script exports a Trello list from a PRIVATE Trello board list through the API. And it gets saved to your clipboard, ready to paste into an e-mail! Just enter your list name, et voila! 
You should install pyperclip (pip install pyperclip) to have the changelog automatically pasted in your clipboard.

## How to use it
Just edit the TrelloKeys.json with your own Trello Key, Token and board ID, and you're good to go.
Trello Key: https://trello.com/app-key
Trello Token: Click the Token link in the previously linked web page
Trello Board id: Go to your Trello board you want to export & add .json to the end of your URL. Your board id is the first thing in the list.
Run the script and enter the EXACT same list name as the one on Trello that you want to export.
The script now asks if you want to export the ticket names with the tag, type Y for yes or N for no.
That's it! 

***No error handling yet. So make sure you enter the exact list name correctly***
