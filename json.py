# Python program to read
import json

# Opening JSON file
f = open('vishal.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['vishal_details']:
	print(i)

# Closing file
f.close()
