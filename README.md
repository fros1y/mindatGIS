# MindatGIS

*TLDR;* 
* I've created a GeoPackage of [Mindat.org](http://Mindat.org) data available for download in the Releases section.
* There is a second version that merges Mindat data with USGS information on public lands.

* The files are too big for Google Maps, but here is an small chunk as an example:

<iframe src="https://www.google.com/maps/d/embed?mid=1GZtmYG1Iqn-nVRIDGEa4JFt6lIVqvt0&ehbc=2E312F&noprof=1" width="640" height="480"></iframe>

## Mindat Opens Up
Mindat is an amazing resource for learning about minerals and, for the rock collector, an awesome way to check out possible locations where those minerals might be found.  

As amazing as it may be, the data has historically been stuck in Mindat, with aggressive anti-scraping and "keep out" signs attached.  Luckily, this seems to be changing! 

With the publication of the [OpenMindat paper](https://rmets.onlinelibrary.wiley.com/doi/10.1002/gdj3.204) last May, new resources were invested into integrating Mindat information into the wider community. There is even an early start of a Python [API library](https://github.com/ChuBL/OpenMindat) and [some example code](https://github.com/ChuBL/How-to-Use-Mindat-API?tab=readme-ov-file) available!

## GIS, Meet Mineral Data

One of my goals for Mindat information has always been to put it on the map, literally.  Although there are small map embeds on the Mindat website, I really wanted to be able to load all of the localitiy information into QGIS or some other GIS package to develop the information.  

To get there, I've put together some interface code, worked around bugs in the current API, and coded up a script to take in Mindat location and geomaterial information and prepare a GeoPackage for use in GIS software! (I use QGIS, but should work in anything OGC standards compliant.) 

## Mineral Data, Meet Public Access

The great thing about open data is combining it in unexpected ways (without having to ask anyone for permission). The USGS is clearly a big believer in open data and makes tons of different products.  

One (newer) offering includes GIS data for [conserved and public lands all over the United States](https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-download).  This dataset is itself a compilation, apparently, of many different sources that describe Federal, State, and municipal lands.  While **it does not tell you if mineral collecting is allowed**, it does have information on whether the public is allowed onto the land in the first place!

Along with `geopandas` and data from Mindat, that means that we can generate maps that not only show mineral localities from Mindat, but also that indicate whether you **might** be able to go to the location and check it out for youself! 

>Of course, this information might be wrong in any number of ways and doesn't even try to cover local rules about mineral, so do your own checking and mind any posted signs. 
But it is a great step towards figuring out new places to look for minerals to collect!

## Pain Points

Things aren't entirely awesome yet, but I have hope!

* Despite [several](https://github.com/ChuBL/OpenMindat/issues/4) [queries](https://www.mindat.org/mesg-652986.html), there is still no actual license specified for the data. 
  * Open and FAIR are repeated frequently, but sadly that seems to mean non-commercial and non-standard restrictions. 
  * See, e.g., "We are creating a forked copy of the CC-BY-NC-SA 4.0 licence tailored specifically for these needs." from the [OpenMindat paper](https://rmets.onlinelibrary.wiley.com/doi/10.1002/gdj3.204)
  
* The API itself is limited and buggy.  
  * There is no way, for example, to retrieve localities by geographic region. 
  * Indeed, trying country-based filtering for the United States [doesn't work](https://www.mindat.org/mesg-650453.html).  
  * It cannot (currently)[https://github.com/ChuBL/OpenMindat/issues/3] provide the minerals (geomaterials) available for a specific locality, despite documentation suggesting so. 
    * I've "worked around" this by downloading *all* of the geomaterial information (which does include locality IDs) and joined that to the locality information.
* Data hygeine is questionable. 
  * There may be better quality GeoJSON artifacts [eventually](https://github.com/ChuBL/OpenMindat/issues/7), but the current information has some sloppy [NA markers](https://github.com/ChuBL/OpenMindat/issues/6)
  * It also lacks any sort of [coordinate reference system](https://datacarpentry.org/organization-geospatial/03-crs.html) to accompany the raw floating point latitude and longitude data.  
    * I'm just assuming EPSG:4326/WGS84.
  * This may just be unavoidable, given the venerable and non-GIS based data collection history, but who knows.
* The "official" Python package for accessing the API is probably best skipped for now.  It doesn't do anything for throttling or sanity checking the data and is (currently)[https://github.com/ChuBL/OpenMindat/issues/5] limited to extracting to files for some reason.


# Additional Requirements

If you want to run this code, you will need to provide your own MinDat API Key. Instructions on getting one are [here](https://www.mindat.org/a/how_to_get_my_mindat_api_key).

When you have it, make a `.env` file with an entry for
`MINDAT_API_KEY=xxxxx`