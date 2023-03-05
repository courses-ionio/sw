import requests
import ntfy

# Define the OpenWeatherMap API URL and API key as variables
api_key = "a730bc3728298979f7d6893764d848cb"
api_url = "https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric"

# Define your Telegram bot token as a variable
bot_token = " "
# Define a function that retrieves the weather information for a given city and country
def get_weather():
    city = "Kozani"
    country = "Greece"
    # Build the API URL for the specified city and country
    url = api_url.format(city, country, api_key)
    # Send a GET request to the API
    response = requests.get(url)
    # If the response status code is not 200 (OK), raise an exception
    response.raise_for_status()
    # Parse the JSON response into a Python dictionary
    data = response.json()
    # Extract the relevant weather information from the dictionary
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    cloud_cover = data["clouds"]["all"]
    # Return the weather information as a formatted string
    return f"Temperature in {city}, {country}: {temperature}°C\nDescription: {description}\nWind speed: {wind_speed} m/s\nHumidity: {humidity}%\nCloud cover: {cloud_cover}%"

# Call the get_weather function to retrieve the weather information
weather_info = get_weather()

# Set up the ntfy notification and send it using the Telegram bot API
ntfy.notify(title="Weather Update", message=weather_info, backend="telegram")

