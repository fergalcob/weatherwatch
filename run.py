# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import googlemaps
from openmeteo_py import Hourly, Daily, Options, OWmanager
from historical_data import *
import re
import datetime
from art import *
import readchar
import os
from openmeteo_py.constants import *
from openmeteo_py.timezones import *

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich.style import Style
from rich.align import Align

current_time = datetime.datetime.now()
hourly = Hourly()
daily = Daily()
daily.daily_params.append("rain_sum")
daily.daily_params.append("snowfall_sum")
current_weather = True
console = Console()

"""
The following converts the weathercodes provided by the API query
to their text values
"""


def weather_converter(weathercode):
    if weathercode >= 0 and weathercode < 50:
        if weathercode <= 40:
            if weathercode == 0:
                weather = 'Clear Sky'

            elif weathercode == 1:
                weather = 'Mainly Clear'

            elif weathercode == 2:
                weather = 'Partly Cloudy'

            elif weathercode == 3:
                weather = 'Overcast'

        else:
            if weathercode == 45:
                weather = 'Fog'

            elif weathercode == 48:
                weather = 'Heavy Fog'

    elif weathercode >= 50 and weathercode < 70:
        if weathercode <= 60:
            if weathercode == 51:
                weather = 'Light Drizzle'

            elif weathercode == 53:
                weather = 'Moderate Drizzle'

            elif weathercode == 55:
                weather = 'Heavy Drizzle'

            elif weathercode == 56:
                weather = 'Light Freezing Drizzle'

            elif weathercode == 57:
                weather = 'Heavy Freezing Drizzle'

        else:
            if weathercode == 61:
                weather = 'Light Rain'

            elif weathercode == 63:
                weather = 'Moderate Rain'

            elif weathercode == 65:
                weather = 'Heavy Rain'

            elif weathercode == 66:
                weather = 'Light Freezing Rain'

            elif weathercode == 67:
                weather = 'Heavy Freezing Rain'

    elif weathercode >= 70 and weathercode < 90:
        if weathercode < 80:
            if weathercode == 71:
                weather = 'Light Snowfall'

            elif weathercode == 73:
                weather = 'Moderate Snowfall'

            elif weathercode == 75:
                weather = 'Heavy Snowfall'

            elif weathercode == 77:
                weather = 'Snow Grains'

        else:
            if weathercode == 80:
                weather = 'Light Showers'

            elif weathercode == 81:
                weather = 'Moderate Showers'

            elif weathercode == 82:
                weather = 'Heavy Showers'

            elif weathercode == 85:
                weather = 'Light Snow Showers'

            elif weathercode == 86:
                weather = 'Heavy Snow Showers'

    else:
        if weathercode == 95:
            weather = 'Thunderstorm'
        elif weathercode == 96:
            weather = 'Thunderstorm w/ Light Hail'
        elif weathercode == 99:
            weather = 'Thunderstorm w/ Heavy Hail'
    return weather


"""
Create the table for the 7-day weather forecast and iterate through the results
to present the data in a visually consistent style
"""


def weather_table(meteo_today):
    table = Table(title=f"7 Day Forecast - {location}")
    table.add_column("Date", justify="center", style="cyan", no_wrap=True)
    table.add_column("Temperature", justify="center",
                     style="cyan", no_wrap=True)
    table.add_column("Weather", justify="center", style="cyan", no_wrap=True)
    table.add_column("Precipitation", justify="center",
                     style="cyan", no_wrap=True)
    """
    Create and add rows to the forecast table
    """
    for w, x, y, z in zip(meteo_today['daily']['precipitation_sum'],
                          meteo_today['daily']['temperature_2m_max'],
                          meteo_today['daily']['time'],
                          meteo_today['daily']['weathercode']):
        table.add_row(y,
                      f"{str(x)}"
                      f"{meteo_today['daily_units']['temperature_2m_max']}",
                      weather_converter(z),
                      f"{str(w)}"
                      f"{meteo_today['daily_units']['precipitation_sum']}")
    os.system('cls||clear')
    table = Align(table, align="center")
    print()
    console.print(table)
    """
    Monitor keystrokes to return to landing page
    """
    print("\n Press enter to return home")
    returnHome = readchar.readkey()
    while returnHome is not readchar.key.ENTER:
        returnHome = readchar.readkey()
    if returnHome == readchar.key.ENTER:
        home()


"""
Create the table for the 24 hour weather forecast
and iterate through the results
to present the data in a visually consistent style
"""


def weather_table_hourly(meteo_today):
    table = Table(title=f"24 Hour Forecast - {location}")
    table.add_column("Time", justify="center", style="cyan", no_wrap=True)
    table.add_column("Temperature", justify="center",
                     style="cyan", no_wrap=True)
    table.add_column("Weather", justify="center", style="cyan", no_wrap=True)
    table.add_column("Precipitation", justify="center",
                     style="cyan", no_wrap=True)

        for counter, (w, x, y, z) in \
            enumerate(list(zip(meteo_today['hourly']['precipitation'],
                               meteo_today['hourly']['apparent_temperature'],
                               meteo_today['hourly']['time'],
                               meteo_today['hourly']['weathercode']))):
        """
        As the 7-day forecast provides data from midnight of the current day,
        the data is iterated through so that only the 24 hours from the current
        time are output
        """
        if counter == current_time.hour + 24:
            break
        elif counter < current_time.hour:
            continue
        else:
            table.add_row(y,
                          f"{str(x)}" +
                          meteo_today['hourly_units']
                          ['apparent_temperature'],
                          weather_converter(z),
                          f"{str(w)}"
                          f"{meteo_today['hourly_units']['precipitation']}")
    os.system('cls||clear')
    table = Align(table, align="center")
    print()
    console.print(table)
    print("\n Press enter to return home")
    returnHome = readchar.readkey()
    while returnHome is not readchar.key.ENTER:
        returnHome = readchar.readkey()
    if returnHome == readchar.key.ENTER:
        home()
