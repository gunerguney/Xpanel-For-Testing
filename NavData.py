__author__ = 'cal02'


airports = []


def readAirports(fileName):

    aptFile = open("apt.dat","r")

    for line in aptFile:
        if line.startswith("1 "):           #get airports start with only 1
            line = " ".join(line.split())   #replace unknown number spaces to one space
            line = line.split(" ",5)        #airport name include spaces so first 5 spaces splitted last one airport name

            airport = {'icao':line[4],'name':line[5], 'elevation':line[1]}

            airports.append(airport)

            line = aptFile.next()

            runways = []                    #contains list of runways
            orderCounter = 0                #counter for using PAPT message it requires order of whole runways

            while line.startswith("100 "):

                line = " ".join(line.split())   #replace unknown number spaces to one space
                line = line.split(" ")


                runway ={'width': line[1], 'name': line[8], 'lat': line[9], 'lon': line[10], 'order': orderCounter, 'backward': 0}
                runways.append(runway)          #first end of runway

                runway ={'width': line[1], 'name': line[17], 'lat': line[18], 'lon': line[19], 'order': orderCounter, 'backward': 1}
                runways.append(runway)          #second end of runway

                airport['runways'] = runways    #add runway list to airport

                line = aptFile.next()

                orderCounter = orderCounter + 1           #increase for each runway which includes 2 ends


    for airport in airports:
        if airport['icao'] == "LTBA":
            print airport['runways']


readAirports('apt.dat')