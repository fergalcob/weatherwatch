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


"""
Takes the time range from user's input and retrieve
the weather for the timeframe provided then
display in table format.
"""


def weather_table_historical(lat, lon):
    os.system('cls||clear')
    print()
    historical_weather_intro = Text("Historical Weather Data", justify="left")
    historical_weather_intro.style = Style(underline=True, bold=True)
    console.print(historical_weather_intro,
                  "\n \nLooking for weather data from a specific"
                  " time? Here you can search through 60 years of past weather"
                  " data  beginning with 2022 and see how the weather"
                  " was on the dates of your choice! Just enter in your"
                  " start date and end dates in the YYYY-MM-DD format"
                  "(i.e. 2022-10-12) and we'll retrieve"
                  " that data for you! \n")
    while True:
        try:
            start_date = (Prompt.ask
                          ("Enter the starting date"
                           " of your search(YYYY-MM-DD)"))
            end_date = (Prompt.ask
                        ("Enter the end date of your search(YYYY-MM-DD)"))
            options_historical = \
                Options_Historical(lat, lon, start_date, end_date)
            mgr = OWmanager_historical(options_historical,
                                       daily.all())
            meteo = mgr.get_data_historical()
            table = Table(title=f"Average Weather for {start_date}"
                          f" - {end_date} - {location}")
            table.add_column("Date Range", justify="center",
                             style="cyan", no_wrap=True)
            table.add_column("Temperature", justify="center",
                             style="cyan", no_wrap=True)
            table.add_column("Weather", justify="center",
                             style="cyan", no_wrap=True)
            table.add_column("Precipitation \n(Rain/Snowfall)",
                             justify="center", style="cyan", no_wrap=True)
            for w, x, y, z in zip(meteo['daily']['precipitation_sum'],
                                  meteo['daily']['temperature_2m_max'],
                                  meteo['daily']['time'],
                                  meteo['daily']['weathercode']):
                table.add_row(y,
                              f"{str(x)}"
                              f"{meteo['daily_units']['temperature_2m_max']}",
                              weather_converter(z),
                              f"{str(w)}"
                              f"{meteo['daily_units']['precipitation_sum']}")
            break
        except KeyError:
            print(f"Invalid date range entered, please ensure the dates"
                  f" are in the format YYYY-MM-DD,"
                  f" you have entered {start_date} & {end_date}")
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


sorted_days = []

"""
Creates a list of all values for specific year and adds to their own list
"""


def total_temps(lat, lon):
    os.system('cls||clear')
    print()
    hot_and_cold = Text("Hottest & Coldest Days", justify="left")
    hot_and_cold.style = Style(underline=True, bold=True)
    console.print(hot_and_cold,
                  "\n \nLooking for the hottest and coldest days in years."
                  " Enter the number of years you wish to search over"
                  " and you'll be shown the 5 hottest and coldest days"
                  " on average for the year range you've selected giving you"
                  " an idea of the most commonly warm"
                  " and cold times of year. \n")
    while True:
        try:
            number_years = \
                Prompt.ask("How many years would you like to cover?")
            start_date = f"{2022 - int(number_years)}-01-01"
            end_date = "2022-12-31"
            options_historical = \
                Options_Historical(lat, lon, start_date, end_date)
            mgr = OWmanager_historical(options_historical,
                                       daily.all())
            meteo = mgr.get_data_historical()

            """
            As the data will always be returned in YYYY-MM-DD format,
            slices the first five characters from the time key values
            leaving the MM-DD values in place and creates new list
            using the MM-DD as key
            """
            temp_days = {}
            for value1 in meteo['daily']['time']:
                temp_days.update({f'{value1[5:]}': []})
            for value1, value2 in zip(meteo['daily']['time'],
                                      meteo['daily']['temperature_2m_max']):
                temp_days[f'{value1[5:]}'].append(value2)
            average_and_sort(temp_days)
            break
        except (ValueError, KeyError):
            print("Please enter a valid number of years to search(0-60)")


"""
Sum up the values of each MM-DD list and averages out the data,
the data is then sorted to get highest and lowest values in order
"""


def average_and_sort(all_days):
    for value in all_days:
        all_days[value] = round(sum(all_days[value]) / len(all_days[value]), 2)
    global sorted_days
    sorted_days = sorted(all_days.items(), key=lambda x: x[1])
    new_weather_table(sorted_days)


"""
Present the highest and lowest values calculated by
average_and_sort() function in the weather table
"""


def new_weather_table(sorting):
    os.system('cls||clear')
    print()
    table = Table(title=f"Hottest & Coldest Days On Average - {location}")
    table.add_column("Date", justify="center", style="cyan", no_wrap=True)
    table.add_column("Coldest Temperatures",
                     justify="center", style="cyan", no_wrap=True)
    table.add_column("Date", justify="center", style="cyan", no_wrap=True)
    table.add_column("Hottest Temperatures",
                     justify="center", style="cyan", no_wrap=True)
    for value in range(0, 5):
        table.add_row(f"{sorted_days[value][0]}",
                      f"{str(sorted_days[value][1])}\N{DEGREE SIGN}C",
                      f"{sorted_days[-value-1][0]}",
                      f"{str(sorted_days[-value-1][1])}\N{DEGREE SIGN}C")
    table = Align(table, align="center")
    console.print(table)
    print("\n Press enter to return home")
    returnHome = readchar.readkey()
    while returnHome is not readchar.key.ENTER:
        returnHome = readchar.readkey()
    if returnHome == readchar.key.ENTER:
        home()

def weather_trends(lat, lon):
    os.system('cls||clear')
    print()
    weather_trends_menu = Text("Changes In Weather", justify="left")
    weather_trends_menu.style = Style(underline=True, bold=True)
    console.print(weather_trends_menu,
                  "\n \nLooking to see how weather patterns have changed over"
                  " years, enter the month you wish to explore and the number"
                  " of years(up to 60 years of data available). You can then"
                  " choose to see how temperature or precipitation has changed"
                  " for your selection has changed over time, including"
                  " changes in the highs and lows of the scale. \n")
