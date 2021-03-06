# Flask course - Baltic internships

Weekly tasks of the course will be uploaded here. If I upload the weeks challenge, it means that I am done with that week!

## First week (deadline: Mar 25):

> For this assigment you will be creating a ver small flask application. Your application should:
>
>> have a route for /welcome, which responds with the string "welcome"
>>
>> have a route for /welcome/home, which responds with the string "welcome home"
>>
>> have a route for /welcome/back, which responds with the string "welcome back"


## Week 2 (deadline: Apr 1):

>You will continue to evolve previously created flask app:
>
>>1. Get weather report for a city of your liking via API call.
>>
>>2. Create a route /weather which responds with received data (city name and current temperature in Celsius). Consider using a template to render and display data.
>>
>>3. Optional task – let user pick a city.
>>
>>API doc: https://openweathermap.org/current#name
>>
>>API Key: [REDACTED]

## Week 3 (deadline: Apr 8):

>1. Get geographic coordinates for a city of your liking via API call
>>
>>API doc: https://openweathermap.org/api/geocoding-api
>
>2. Get historical data from dev.meteostat.net via one of these methods:
>>
>>JSON API
>>Python library
>>Bulk data
>
>3. Display one year of temperature history - min., max., average
>>Use graphical form of representation – matplotlib module
>
>4. Create a route /weather_history to display data
>>Show city name and chart with temperature data, including legend (names of axis, description of data)
>>In addition, separately display value for min., max., average temperature and date when it was recorded
>>Provide a download link for an Excel document with temperature data (raw data)
>>Provide a download link for an PDF document with temperature chart (graphical data)

## Final Week (deadline: Apr 15):
>1. Record each weather search to logfile
>>
>>Log: Date, Time, City, Temperature
>>
>2. Create a route /log to display data for last 5 searches
>>
>>Think about persistent data. Last 5 searches must be displayed even after flask is restarted
>>
>3.Create a route /cities
>>
>>Display current list of cities of interest and their current temperature (updates on list change)
>>Let user add city to the list
>>Let user change list entry (change city name)
>>Let user delete city from the list
>>Record add/change/delete events to logfile
>>Let user manually refresh currently listed cities temperature data
>>Current list and temperature must persist after flask is restarted
>>
>Optional advanced task: implement this for multiple users (identified by login)


*Well, it was a good run while it lasted. In these four weeks I learned how to use Flask, Jinja, SQLAlchemy and three different weather APIs. Thanks to Ints Meijers, our coordinator, for these fun challenges*

*(PS. the hardest one was definitely the third week, plotting data with matplotlib, converting images and pdf and csv files to base64, loading them into memory using buffers and generating a download link for the user)*