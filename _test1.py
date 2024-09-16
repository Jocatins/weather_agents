import requests

# Define the API URL and payload
API_URL = "http://localhost:1234/v1/completions"
payload = {
    "prompt": "Provide a weather forecast for Togo for the next week.",
    "max_tokens": 100,
}

# Make the POST request to the LM Studio server
response = requests.post(API_URL, json=payload)

# Check if the request was successful
if response.status_code == 200:
    forecast = response.json().get("choices", [{}])[0].get("text", "").strip()
    print(f"Weather Forecast: {forecast}")
else:
    print(f"Error: {response.status_code} - {response.text}")
