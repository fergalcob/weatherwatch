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