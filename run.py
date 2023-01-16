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
