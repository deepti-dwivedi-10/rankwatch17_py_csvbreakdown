import os #for using operating system dependent functionality
import csv #For dealing with the CSV files and data
for file_ in os.listdir("raw"): #os.listdir returns a list of the entries in the directory given by path
    with open('raw/'+ file_, 'rb') as csvfile: #opening files from raw folder one by one
        spamreader = csv.reader(csvfile, delimiter=',') #reading the data
        for row in spamreader: #getting each row one by one fromspamreader
            if os.path.isfile("processed/" + row[0] +"-processed.csv"): #checking if it already exists then continue
                with open("processed/" + row[0] +"-processed.csv", 'a') as csvfile1: #opening the already created file of the particular date
                    spamwriter = csv.writer(csvfile1, delimiter=',') #writing the information in that processed file
                    spamwriter.writerow(row)
            else: #if file does not exists in processed folder
                with open("processed/" + row[0] +"-processed.csv", 'wb') as csvfile1: #creating and opening the processed file
                    spamwriter = csv.writer(csvfile1, delimiter=',') #writing the information into it
                    spamwriter.writerow(row)