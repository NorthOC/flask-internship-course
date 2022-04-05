from flask import Flask, redirect, render_template, url_for, request
from city_search import find_city
from get_weather import get_weather_results
from get_coordinates import get_coordinates
from get_meteostat import get_meteostat_data_detailed
app = Flask(__name__)

#redirect root to /welcome
@app.route("/")
def redirect_page():
    return redirect(url_for("welcome"))


@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

#return welcome home or welcome back using same template.
@app.route("/welcome/home")
def welcome_home():
    return render_template("_welcome.html", value = "home")

@app.route("/welcome/back")
def welcome_back():
    return render_template("_welcome.html", value = "back")

#retrieve weather based on search and save state between searches
@app.route("/weather", methods=["POST", "GET"])
def weather():
  #when the weather.html form is submitted
  if request.method == "POST":

    city_search = request.form["city"]

    #for keeping state
    city_id = request.args.get("city_id")
    if city_id != None:
      found_city = get_weather_results(str(city_id))
    else:
      found_city = get_weather_results(str(3489854))
      
    #to stop humans from grabbing all the city.list.json (>200k) results
    if len(city_search) > 1:
      items = find_city(city_search)
    else:
      items = None

    return render_template("weather.html", 
    items = items, search = city_search, city=found_city, city_id = city_id)
  
  else:
    city_id = request.args.get("city_id")
    city_state = request.args.get("state")
    #for keeping state
    if city_id != None:
      found_city = get_weather_results(str(city_id))
    else:
      found_city = get_weather_results(str(3489854))
    found_city['state'] = city_state

    #args: items - cities matching search keyword, city_search - search query
    # found_city - API info about city, city_id - id from weather API
    return render_template("weather.html", 
    items = None, search = None, city=found_city, city_id = city_id)

@app.route("/weather_history")
def get_weather_history():
  city_name = request.args.get("name").replace('_', ' ')
  country = request.args.get("cont")
  state = request.args.get("state")
  #get coordinates
  found_city = get_coordinates(city_name, country, state)
  #meteostat data
  data_in_html = get_meteostat_data_detailed(found_city['city'], float(found_city['lat']), float(found_city['lon']))
  return render_template('weather_history.html', city = data_in_html)

if __name__ == "__main__":
  app.run(debug=True, port=5000)