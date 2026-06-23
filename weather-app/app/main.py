import os
import requests

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is required")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q=Paris&appid={API_KEY}&units=metric"
)

response = requests.get(url)
response.raise_for_status()

data = response.json()

print(f"City: {data['name']}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Weather: {data['weather'][0]['description']}")
