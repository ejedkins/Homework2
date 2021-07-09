#Elijah Jedkins PSID: 1786452
import csv

fileName = input()

wordsFrequency = {}

with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for i in csvreader:
        for j in i:
            if j not in wordsFrequency.keys():
                wordsFrequency[j] = 1
            else:
                wordsFrequency[j] += 1

for key in wordsFrequency.keys():
    print(key + " " + str(wordsFrequency[key])) 