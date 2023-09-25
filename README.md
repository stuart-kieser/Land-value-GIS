The following project is WIP. 

The program is used to demonstrate a heat map showing the average landvalue per SQM. 
By webcrawling publically available property data pertaining to a certain area we are able to exptrapolate that value into and average land value per region. where we can develop a valuation map to visually depict economic data that we would want.

Property consists of attributes; location Street address --> (co-ordinates), price, area.
these attriutes need to be revalued to the heat map intensity scales, this can be done with maximum land value and minimum land value per SQM. 
[longatude, latitude, intensity]

Market consists of attributes; average land price, average land area, value per SQM. 

Property attributes and market attributes define characteristics of the valuation map. 

Converting street address into co-ordinates is done with the Bing Maps api. 

The csv file has the property data: location and price, the location is plugged into the the address tab and the price into the price catagory. 
The intensity should be auto calculated, maybe set to the standard deviation of the data set. 

NOTES:
Web crawl for property data, format data
Depict data visual using any python modules (to be researched)
- dasymetric
- heatmap
- space time cubes
- voronoi diagram
Modules:
ipyleaflet

DATA COLLECTION:
Data is collected for every area in gauteng, and sorted into their general area per csv

by looking at p24 when under gauteng all the prop listings for the area are shown to a rough total of 50000

DATA CLEANING:
Data is grouped by area and the values are used to create and area value 

DATA VISUALIZATION:
Region average is collected and plotted on a per m2 and per average building price. 
