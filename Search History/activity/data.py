import json

config = json.loads(open('C:/Users/DELL.india/Desktop/activity/data2.json').read())

print(config[0]['content'][0])