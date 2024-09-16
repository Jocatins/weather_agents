import asyncio
from weather_api import get_real_time_weather
from conversable_agent import get_general_response

async def get_forecast_or_chat(query, location=None):
    """Decide whether to fetch weather data or ask a general query."""
    
    # Check if the query is related to weather by looking for keywords or the presence of location
    if "weather" in query.lower() or location:
        # Call the weather API if the query is weather-related
        weather_report = get_real_time_weather(location)
        print(weather_report)
    else:
        # Otherwise, use the general agent to handle the query
        general_response = await get_general_response(query)
        print(general_response)

# Function to interact with the user
async def interact_with_user():
    # Get user input
    location = input("Enter the location for the weather forecast: ")
    period = input("Enter the time period (e.g., 'next 24 hours', 'next week'): ")
    
    # Construct the query
    query = f"Provide a weather forecast for {location} for the {period}."
    
    # Decide whether to call the weather API or the general agent
    await get_forecast_or_chat(query, location)

if __name__ == "__main__":
    # Run the user interaction asynchronously
    asyncio.run(interact_with_user())
