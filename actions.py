# import requests
# import logging  # Import the logging module
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import webbrowser

# # Configure the logging module
# logging.basicConfig(level=logging.DEBUG)  # You can adjust the log level as needed

# class ActionRedirection(Action):
#     def name(self) -> Text:
#         return "action_redirection"

#     async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         website = tracker.latest_message.get("text")
#         if "google" in website.lower():
#             url = "https://www.google.com"
#             dispatcher.utter_message("Opening Google..")
#         elif "nykaa" in website.lower():
#             url = "https://www.nykaa.com"
#             dispatcher.utter_message("Opening Nykaa..")
#         elif "amazon" in website.lower():
#             url = "https://www.amazon.in"
#             dispatcher.utter_message("Opening Amazon..")
#         elif "myntra" in website.lower():
#             url = "https://www.myntra.com"
#             dispatcher.utter_message("Opening Myntra..")
#         else:
#             url = "https://www.flipkart.com"
#             dispatcher.utter_message("Opening Flipkart")

#         webbrowser.open(url)
#         logging.info(f"Opened website: {url}")  # Log the website URL
#         return []

# class ActionGetWeather(Action):
#     def name(self) -> Text:
#         return "action_get_weather"

#     def kelvin_to_celsius(self, kelvin_temp: float) -> float:
#         celsius_temp = kelvin_temp - 273.15
#         return celsius_temp

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         entities = tracker.latest_message.get("entities")
#         logging.info(f"Extracted entities: {entities}")  # Log extracted entities

#         city = tracker.get_slot('city')
#         logging.info(f"Extracted City: {city}")  # Log extracted city

#         api_key = "4d5df4d5dbd81c9da080c40a865e313d"
#         complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#         logging.info(f"complete_url: {complete_url}")  # Log the complete URL

#         response = requests.get(complete_url)
#         weather_data = response.json()
#         logging.info(f"weather_data: {weather_data}")  # Log weather data

#         conditions = ""
#         temperature = None

#         if "weather" in weather_data and weather_data["weather"]:
#             conditions = weather_data["weather"][0].get("description", "")
#             logging.info(f"conditions: {conditions}")  # Log weather conditions

#         if "main" in weather_data and "temp" in weather_data["main"]:
#             temperature_kelvin = weather_data["main"]["temp"]
#             temperature_celsius = self.kelvin_to_celsius(temperature_kelvin)
#             temperature = f"{int(temperature_celsius)}°C"  # Convert to integer and format as °C
#             logging.info(f"temperature: {temperature}")  # Log temperature

#         if temperature and conditions:
#             message = f"The weather in {city} is {conditions} with a temperature of {temperature}."
#         elif conditions:
#             message = f"The weather in {city} is {conditions}."
#         else:
#             message = f"Sorry, I couldn't fetch the weather information for {city}."

#         dispatcher.utter_message(text=message)
#         return []

import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
import logging

# Configure the logging settings
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG  # Change the logging level to DEBUG
)
logger = logging.getLogger(__name__)

class ActionRedirection(Action):
    def name(self) -> Text:
        return "action_redirection"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        website = tracker.latest_message.get("text")
        if "google" in website.lower():
            url = "https://www.google.com"
            dispatcher.utter_message("Opening Google..")
        elif "nykaa" in website.lower():
            url = "https://www.nykaa.com"
            dispatcher.utter_message("Opening Nykaa..")
        elif "amazon" in website.lower():
            url = "https://www.amazon.in"
            dispatcher.utter_message("Opening Amazon..")
        elif "myntra" in website.lower():
            url = "https://www.myntra.com"
            dispatcher.utter_message("Opening Myntra..")
        else:
            url = "https://www.flipkart.com"
            dispatcher.utter_message("Opening Flipkart")

        webbrowser.open(url)
        logger.info(f"Opened website: {url}")  # Log the website URL
        return []

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"
    
    def kelvin_to_celsius(self, kelvin_temp: float) -> float:
        celsius_temp = kelvin_temp - 273.15
        return celsius_temp

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get("entities")
        logger.debug("Extracted entities: %s", entities)

        city = tracker.get_slot('city')
        logger.debug("Extracted City: %s", city)

        api_key = "4d5df4d5dbd81c9da080c40a865e313d"
        complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        logger.debug("complete_url: %s", complete_url)

        response = requests.get(complete_url)
        weather_data = response.json()
        logger.debug("weather_data: %s", weather_data)

        conditions = ""
        temperature = None

        if "weather" in weather_data and weather_data["weather"]:
            conditions = weather_data["weather"][0].get("description", "")
            logger.debug("conditions: %s", conditions)

        if "main" in weather_data and "temp" in weather_data["main"]:
            temperature_kelvin = weather_data["main"]["temp"]
            temperature_celsius = self.kelvin_to_celsius(temperature_kelvin)
            temperature = f"{int(temperature_celsius)}°C"
            logger.debug("temperature: %s", temperature)

        if temperature and conditions:
            message = f"The weather in {city} is {conditions} with a temperature of {temperature}."
        elif conditions:
            message = f"The weather in {city} is {conditions}."
        else:
            message = f"Sorry, I couldn't fetch the weather information for {city}."

        dispatcher.utter_message(text=message)
        return []
