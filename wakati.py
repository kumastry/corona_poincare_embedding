import json
import spacy
import csv

nlp = spacy.load("ja_ginza")
documents = []
sentents_word = []

cnt = 0
for row in open("corona-2nd.ndjson", encoding="utf-8_sig"):
    obj = json.loads(row.strip())
    print(cnt)
    if(cnt == 150):
        break
    cnt += 1
    word = []
    for key in ['name', 'objective']:
        if obj[key]:
            doc = nlp(obj[key])
            for sent in doc.sents:
                for t in sent:
                    if(len(t.text) > 1 and t.pos_ == 'NOUN'
                    ):
                        word.append(t.text)
    sentents_word.append(word)

#print(sentents_word)
print(sentents_word) 
#print("##########")
#a = 0
#b = 0
#c = 0
#d = 0
#for i in sentents_word:
#    for j in i:
#        if(j == "新型コロナウイルス"):
#            a += 1
        
#        if(j == "新型コロナウイルス感染症"):
#            b  += 1
        
#        if(j == "コロナ"):
#            c += 1

#        if(j == "感染症"):
#            d += 1
data = []
cnt = 0
for word in sentents_word:
    cnt += 1
    print(cnt)
    n = len(word)
    for i in range(n):
        for j in range(i+1, n):
            data.append([word[i], word[j]])
            data.append([word[j], word[i]])
#print(data)
with open("corona3.tsv", 'w' ,newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(data)
