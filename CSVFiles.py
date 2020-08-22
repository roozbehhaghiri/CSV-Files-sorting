import urllib.parse
import operator
import csv
#Find the most 10 popular pages of each language
def firstten (listofdatas, language):
    resultlist=[language]
    count = 0
    for row in listofdatas:
        if row[0] == language:
            resultlist.append(urllib.parse.unquote(row[1]))
            count += 1
        if count == 10:
            break
    return(resultlist)
#Put all the usefull datas in a list
def lisofusefulldata(data):
    listofdata=[]
    for row in data:
        if len(row[0]) < 3 and not (":" in row[1]):
            if '%' in row[1]:
                row[1] = urllib.parse.unquote(row[1])

            listofdata.append(row)
    return (listofdata)
#Openning the csv file
with open(r"pagecounts-20120101-000000","r", encoding="latin1") as csvfile:
    #creating a csv file for the number of views and total byte transformed of each language
    with open("ViewsAndTransferredBytes.csv","w", encoding="latin1", newline='')as newcsvfile:
        #creating a csv file for the 10 most popular pages of each language
        with open("TopPages.csv","w", encoding="utf8", newline='') as newcsv:
            VATD = csv.writer(newcsvfile)
            TP = csv.writer(newcsv)
            data = csv.reader(csvfile, delimiter=' ')
            listofdata = lisofusefulldata(data)
            countviews = 0
            countbytes = 0
            language = listofdata[0][0]
            #sorting datas by number of views
            sortedlist = sorted(listofdata, key=operator.itemgetter(2), reverse=True)
            #Creating headers for both csv files as a separate row
            VATD.writerow(["Language", "Total_bytes_transferred", "View_count"])
            TP.writerow(["Language", "Page_1", "Page_2", "Page_3", "Page_4", "Page_5", "Page_6", "Page_7", "Page_8", "Page_9", "Page_10"])
            for row in listofdata:
                #cheking for data with the same languages
                if row[0] == language:
                    #counting the views and the transferred bytes for each language
                    countviews += int(row[2])
                    countbytes += int(row[3])
                else:
                    #coping the datas to csv files
                    VATD.writerow([language, countbytes, countviews])
                    TP.writerow(firstten(sortedlist, language))
                    countbytes = int(row[3])
                    countviews = int(row[2])
                    language = row[0]
            #coping the data of the last language to the csc files
            VATD.writerow([language, countviews, countbytes])
            TP.writerow(firstten(sortedlist, language))

            








