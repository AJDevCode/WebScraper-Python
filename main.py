import requests

from bs4 import BeautifulSoup
#Abhayjit Sodhi
### Design
cloud =("""   

                        ▓▓▓▓▓▓▓▓
          ░░  ▓▓▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒
        ░░░░▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓
        ░░▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
      ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      ░░▒▒    ░░░░░░░░░░░░░░  ░░░░░░░░░░
              ░░  ░░░░    ░░  ░░░░
              ░░    ░░    ░░    ░░
              ░░
            ░░    ░░    ░░    ░░
            ░░    ░░    ░░    ░░

        ░░░░    ░░    ░░    ░░
          ░░    ░░    ░░    ░░

      ░░                      ░░             """)





#Using beautiful Soup
#URL and setup
URL = "https://weather.com/weather/today/l/b1d7089dcff056d6907ce58c458f2a32932387f1854af523080c6c79e2678e66"
page = requests.get(URL)
beautifulSoup = BeautifulSoup(page.content, "html.parser")

### list elements to be printed.
results = beautifulSoup.find(id="WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a")
tempDisplay = results.find("span", class_="CurrentConditions--tempValue--MHmYY")
descript = results.find("div", class_="CurrentConditions--phraseValue--mZC_p")
loc = results.find("h1", class_="CurrentConditions--location--1YWj_")
currentTime = results.find("span", class_="CurrentConditions--timestamp--1ybTk")

### tommorw

resultTmr =results.find("span", class_="Ellipsis--ellipsis--3ADai")



### Print results to user

print (cloud)
print("---------------------------------")
print("| WEATHER INFORMATION")
print("| Location:", loc.text)

print("| Current temperature:", tempDisplay.text)

print("| Weather description:", descript.text)

print("| Local time:", currentTime.text)
print("---------------------------------")



