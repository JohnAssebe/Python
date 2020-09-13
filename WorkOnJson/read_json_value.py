import json
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
json_data=json.loads(stringOfJsonData)
print(json_data)
