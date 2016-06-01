# Landgraf_final_project

# Concept and documentation


## App name: California Board and Care Mapper


## Elevator pitch

Historically in California, disabled homeless people have been housed in residential care facilities, or board and cares, as they are more commonly known. But board and cares have been closing at a high rate, and few new ones are being licensed.

As a result, hospitals and social workers have fewer facilities to send homeless individuals to.

A look at the big picture would be helpful: what is the number of board and cares and available beds in each county, compared with the homeless population?

## Inspirations and Prior Work

- [Map the Homeless](https://theawl.com/the-homeless-wall-of-shame-755f98b50b01#.4ys2k5bfo)
  + The construction of the app doesn't match what I want to do, but it does indicate 
- [Chicago Crime Mapper](http://spotcrime.com/il/chicago)
  + Much closer to what I want to do: overlay board and cares and a map of California


# Data

## Data sources

1. The California Department of Social Services maintains a downloadable .csv file of all adult residential care facilities in the state: [https://secure.dss.ca.gov/CareFacilitySearch/home/getstatedata/HomeCare](https://secure.dss.ca.gov/CareFacilitySearch/home/getstatedata/HomeCare)
2. HUD maintains point-in-time counts of homeless individuals in counties. Would be very easy to make a quick spreadsheet with county names and the number of homeless individuals in each county: [https://www.hudexchange.info/manage-a-program/coc-homeless-populations-and-subpopulations-reports/?filter_Year=2015&filter_Scope=CoC&filter_State=CA&filter_CoC=&program=CoC&group=PopSub](https://www.hudexchange.info/manage-a-program/coc-homeless-populations-and-subpopulations-reports/?filter_Year=2015&filter_Scope=CoC&filter_State=CA&filter_CoC=&program=CoC&group=PopSub)
2. California county shapefiles from Arcgis. [http://www.arcgis.com/home/item.html?id=2f227372477d4cddadc0cd0b002ec657](http://www.arcgis.com/home/item.html?id=2f227372477d4cddadc0cd0b002ec657)


## Categorical variable

The column named "Facility Status" in the database of residential care facilities contains three categories: Licensed, Closed, and Unlicensed

The residential care facilities easily fall into each of these three broad categories

## Creating a continuous variable

With the HUD data, we can get an estimate of the homeless population in each county, so we can calculate the rate of how many board and care beds are available for every 100 homeless people.

## Joining two datasets

The Social Services data includes addresses for each of the board and cares, so it can be joined to the HUD data and the California county shapefiles using PostGIS queries. 

# Filtering options

## Attributes to search/find by

-Allow the user to select a county by a dropdown menu
-Allow the user to view board and cares by status: licensed, closed, and unlicensed.

# Deployment

Use Heroku
