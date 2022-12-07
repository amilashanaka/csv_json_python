import csv
import json
import pandas as pd



#function convert to csv file to json file 
def make_json(csvFilePath, jsonFilePath):
     
    # create a data dictionary
    data = {}
     
    # Open a csv reader called DictReader

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'ID' to
            # be the primary key
            key = rows['Product_Code']
            data[key] = rows
            
    
    # Open a json writer, and use the json.dumps()
    # function to dump data
    
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


#call function convert csv file to json file format

make_json('product__demnd.csv','input_data.json')


