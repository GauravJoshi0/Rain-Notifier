import requests
import os
from collections import Counter
from twilio.rest import Client

# Fetch Twilio credentials from environment variables
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Define the location key for the forecast and AccuWeather API endpoints
LOCATION_KEY = "244107"
Daily = f"""http://dataservice.accuweather.com/forecasts/v1/daily/1day/{LOCATION_KEY}?apikey={os.environ.get("ACCUWEATHER_API")}"""
Hourly = f"""http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{LOCATION_KEY}?apikey={os.environ.get("ACCUWEATHER_API")}"""

# Make API requests for daily and hourly forecasts
daily_response = requests.get(Daily)
hourly_response = requests.get(Hourly)

hour_count = []
time_count = []

# Check if both requests were successful (HTTP status code 200)
if {daily_response.status_code, hourly_response.status_code} == {200}:
    # Parse the daily forecast data
    data = daily_response.json()
    
    # Check if the forecast indicates rain or thunderstorms
    forecast = data["Headline"].get("Category")
    if forecast in ["rain", "thunderstorm"]:
        try:
            # Loop through hourly forecast to gather precipitation information
            for hour in hourly_response.json():
                check = hour.get("PrecipitationIntensity")
                if check is not None:
                    hour_count.append(check)
                    time = str(hour.get("DateTime")).split("T")[1].split("+")[0].removesuffix(":00")
                    time_count.append(time)

            # Send an SMS with the forecast details via Twilio
            message = client.messages.create(
                messaging_service_sid=os.environ.get("MESSAGING_SERVICE_SID"),
                body=f"""Today, there is a chance of {Counter(hour_count).most_common(1)[0][0]} rain {f"at {time_count[0]}" if len(hour_count) == 1 else f"on {', '.join(time_count)}"}""",
                to='+977XXXXXXXXXX'
            )

            print(message.sid)
        except Exception as e:
            print(e)
