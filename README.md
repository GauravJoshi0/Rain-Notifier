# Rain-Notifier using Python
This project is a Python script that fetches real-time weather data from the AccuWeather API and sends SMS alerts using Twilio. It checks for specific weather conditions (like rain or thunderstorms) and sends a notification if detected.

Here are the screenshots of the code and the output:

<img src="Screenshots/weather_script_1.png" alt="Code Screenshot 1" width="600"/>
<i>First part of the script that handles API requests and data processing.</i>
<br><br>
<img src="Screenshots/weather_script_2.png" alt="Code Screenshot 2" width="600"/>
<i>Second part of the script that sends SMS notifications based on the weather data.</i>
<br><br>
<img src="Screenshots/output.jpg" alt="Output Screenshot" width="600"/>
<i>Example output showing the notification sent for weather alerts.</i>
<br><br>
The `weather.json` file is intended for testing purposes. Since AccuWeather has daily request limits, you can use this file to test and modify your app without exceeding those limits.
<br><br>
This script is designed to run continuously on a server. It uses Twilio to send messages, and additional phone numbers can be added directly through the Twilio website. It has various use cases, such as serving as an add-on for a fully featured weather app.
<br><br>
Links:

https://www.twilio.com/docs<br>
https://developer.accuweather.com/accuweather-forecast-api/apis

Feel free to give Feedback!
