import csv
import json

data = []

for row in open("corona-2nd.ndjson", encoding="utf-8_sig"):
    obj = json.loads(row.strip())
    for i in obj['objective_keyphrases']:
        for j in i['words']:
            data.append(j + '\n')
print(len(data))
data = list(set(data))
print(len(data))
with open("keyword.csv", 'w' ,newline='', encoding="utf-8") as f:
    f.writelines(data)
