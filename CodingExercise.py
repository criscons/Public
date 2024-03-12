import csv
import json
import requests


#Remove any duplicates by name. For each name just keep a single row....
def deleteDuplicates(filecsv):
    items={}
    with open(filecsv, 'r') as file:
        records_r = csv.DictReader(file)
        for item in records_r:
            name = item['NAME']
            items[name]=item
    with open(filecsv, 'w', newline='') as file:
        records_w = csv.DictWriter(file, fieldnames=records_r.fieldnames)
        records_w.writeheader()
        for item in items.values():
            records_w.writerow(item)


#Print the data ordered by name desc
def printOrdDesc(filecsv):
    with open(filecsv, 'r') as file:
        records_r = csv.DictReader(file)
        sortedItems= sorted(records_r,key=lambda x: x['NAME'], reverse=True)
        for item in sortedItems:
            print(item)

#Convert the data in json format
def convertToJson(filecsv,filejson):
    with open(filecsv, 'r') as file:
        records_r = csv.DictReader(file)
        items = [row for row in records_r]
    with open(filejson, 'w') as json_file:
        json.dump(items,json_file,indent=4)

#Execute an HTTP POST request passing the json data
#to https://httpbin.org/post and collect output.
def executePostRequest(json_items):
    url= 'https://httpbin.org/post'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=json_items)
    return response


if __name__ == '__main__':
    
    #Path input file csv
    filecsv = "/home/sirio/Scrivania/CodingExercise/filecsv.csv"
    deleteDuplicates(filecsv)
    
    printOrdDesc(filecsv)

    #Path output file json
    filejson = "/home/sirio/Scrivania/CodingExercise/filejson.json"
    convertToJson(filecsv,filejson)
    
    
    with open(filejson, 'r') as file:
        json_items= json.load(file)
    output = executePostRequest(json_items)
    print(output.text)
        


