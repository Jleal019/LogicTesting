import requests, json, dateutil.parser, pytz
# function converts 24-Hour formatted UTC time to 12-Hour formatted ET
def format_time(mod):
    fmt = '%I:%M%p %m-%d-%Y'# format to be followed when printing time
    utc = dateutil.parser.parse(mod) # parses UTC datetime
    formed_date = utc.astimezone(pytz.timezone("US/Eastern")) # converts to ET time
    formed_date = formed_date.strftime(fmt) # formats string for printing
    return formed_date

# extracts United States statistics
url = 'https://covidtracking.com/api/v1/us/current.json'
req = requests.get(url)

#since alist is returned in this instance, this part converts the list into a dictionary object
js_obj = req.json()

# the above response is returned as a list
# that is why these variables are set with a list position and then dictionary position
US_test_pos = str(js_obj[0]["positive"])
US_deaths = str(js_obj[0]["death"])
US_last_mod = str(format_time(js_obj[0]["lastModified"]))

print("United States statistics: \nTotal Cases: " + US_test_pos
+ "\nTotal Deaths: "+ US_deaths + "\nLast Modified: " + US_last_mod)

# extracts Florida statistics
url = 'https://covidtracking.com/api/states?state=FL'
req = requests.get(url)

js_obj = req.json() # loads page contents into json module
# print(req) # prints server reply

state_test_pos = js_obj["positive"]
state_deaths = js_obj["death"]
state_lastMod = format_time(js_obj["dateModified"])

print("Florida state statistics: \nTotal Cases: " + str(state_test_pos)
+ "\nTotal Deaths: " + str(state_deaths) + "\nLast Modified: " + state_lastMod) # prints json object
