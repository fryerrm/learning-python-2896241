# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request 
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name  
    if "count" in theJSON["metadata"]:
        count = theJSON["metadata"]["count"]
        print("Number of events recorded", count)
    
    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        print(i["properties"]["place"], "with a magnitude of", i["properties"]["mag"])
    print("-----------------\n")

    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"], "with a magnitude of", i["properties"]["mag"])

    # print only the events where at least 1 person reported feeling something
    print("-----------------\n")
    
    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["felt"] != None:
            if i["properties"]["felt"] > 0:
                print(i["properties"]["place"], "with a magnitude of", i["properties"]["mag"], "felt by", i["properties"]["felt"], "people.")

  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    resultcode = str(webUrl.getcode())
    if (resultcode == '200') :
        printResults(webUrl.read())
    else:
        print("Could not print results due to error:", resultcode)

if __name__ == "__main__":
    main()
