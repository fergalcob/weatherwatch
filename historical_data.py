"""
This is a reworking of the openmeteo_py library.
Currently, this library doesn't support querying OpenMeteo's
Historical Weather data API.
The module has been updated to query the archive endpoint and pass
the additional parameters required for historical data
"""
import http.client
import requests
import json
import pandas as pd
from openmeteo_py import ApiCallError, FilepathNotFilled, FileOptionError
from openmeteo_py import Hourly, Daily, Options, OWmanager
from openmeteo_py.constants import *
from openmeteo_py.timezones import *
import re

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except http.client.IncompleteRead as e:
            return e.partial
    return inner


http.client.HTTPResponse.read = patch_http_response_read(
    http.client.HTTPResponse.read)


class OWmanager_historical():

    def __init__(self, options_historical, daily=None):
        """
        Entry point class providing ad-hoc API clients for each OW web API.
        Args:
            options (Options): options for the /v1/forecast endpoint .
            hourly (Hourly): Hourly parameter object.
            daily (Daily) : Daily parameter object.
        """

        self.options_historical = options_historical
        self.daily = daily
        self.url = "https://archive-api.open-meteo.com/v1/era5?"
        self.payload = {
            "latitude": options_historical.latitude,
            "longitude": options_historical.longitude,
            "timezone": options_historical.timezone,
            "windspeed_unit": options_historical.windspeed_unit,
            "precipitation_unit": options_historical.precipitation_unit,
            "timeformat": options_historical.timeformat,
            "start_date": options_historical.start_date,
            "end_date": options_historical.end_date
        }
        if self.daily is not None:
            self.payload['daily'] = ','.join(self.daily.daily_params)
        self.payload = "&".join("%s=%s" % (k, v)
                                for k, v in self.payload.items())

    def Jsonify(self, meteo):
        """Returns a json with each variable having keys as dates,
        result json otherwise
        Args:
            meteo (Dict): JSON input
        Returns:
            dict: response JSON
        """

        daily = {}
        cleaned_data = {}
        if "daily" in meteo:
            for i in meteo['daily']:
                data = {}
                for j in range(len(meteo['daily'][i])-1):
                    data[meteo["daily"]["time"][j]] = meteo['daily'][i][j]
                daily[i] = data
            cleaned_data["daily"] = daily
        else:
            cleaned_data = meteo
        return cleaned_data

    def get_data_historical(self, output=0, file=0, filepath=None):
        """
        Handles the retrieval and processing of the OPEN-METEO data.
        Args:
            output (int, optional): default is the server response JSON,
            1 for a JSON with variable keys as dates,2 for the server
            response parsed as a dataframe and 3 for a dataframe
            where each column is for a variable with rows being
            linked each to a time/date
            file (int, optional): 0 as a default (not saving),
            1 for the server's response JSON or dataframe saved as csv,
            2 for excel file (xlsx)
            filepath (string, optional): filepath of the output file
            to be saved at
        Raises:
            BaseException: HTTP error
            ApiCallError: Api resonse error
            FileOptionError: File option being incorrect (number < 0 or > 3)
            FilepathNotFilled: Filepath not filled in the input options
            ConnectionError: requests connection error
            (internet connection or server having some trouble)
        Returns:
            dict: response JSON
        """

        try:
            r = requests.get(self.url, params=self.payload)
            if r.status_code != 200 and r.status_code != 400:
                raise BaseException(
                    "Failed retrieving open-meteo data,server returned HTTP code: {} on following URL {}.".format(r.status_code, r.url))
            if "reason" in r:
                raise ApiCallError(r)
            if file == 0:
                if output == 0:
                    return json.loads(r.content.decode('utf-8'))
                elif output == 1:
                    return self.Jsonify(json.loads(r.content.decode('utf-8')))
                elif output == 2:
                    return pd.DataFrame(json.loads(r.content.decode('utf-8')))
                elif output == 3:
                    return self.dataframit(json.loads(r.content.decode('utf-8')))
            elif file > 0 and file < 3:
                if filepath is None:
                    raise FilepathNotFilled
                if output == 0:
                    with open(filepath+'.json', 'wb+') as f:
                        f.write(r.content)
                    return json.loads(r.content.decode('utf-8'))
                elif output == 1:
                    with open(filepath+'.json', 'wb+') as f:
                        f.write(r.content)
                    return self.Jsonify(json.loads(r.content.decode('utf-8')))
                elif output == 2:
                    if file == 1:
                        pd.DataFrame(json.loads(r.content.decode(
                            'utf-8'))).to_csv(filepath+".csv")
                        return pd.DataFrame(json.loads(r.content.decode('utf-8')))
                    else:
                        pd.DataFrame(json.loads(r.content.decode(
                            'utf-8'))).to_excel(filepath+".xlsx")
                        return pd.DataFrame(json.loads(r.content.decode('utf-8')))
                elif output == 3:
                    if file == 1:
                        return self.dataframit(json.loads(r.content.decode('utf-8')), file, filepath)
                    else:
                        return self.dataframit(json.loads(r.content.decode('utf-8')), file, filepath)
            else:
                raise FileOptionError
        except requests.ConnectionError as e:
            raise (e)

    def dataframit(self, meteo, format=0, filepath=None):
        """Returns a dataframe with each variable
        having keys as dates,result dataframe otherwise
        Args:
            meteo (Dict): JSON input
        Returns:
            dict: response dataframe
        """

        meteo = self.Jsonify(meteo)
        if format == 0:
            if 'daily' in meteo:
                return pd.DataFrame(meteo['daily'])
            else:
                return pd.DataFrame(meteo)
        elif format == 1:
            if 'daily' in meteo:
                pd.DataFrame(meteo['daily']).to_csv(filepath+"_daily.csv")
                return pd.DataFrame(meteo['daily'])
            else:
                pd.DataFrame(meteo).to_csv(filepath+".csv")
                return pd.DataFrame(meteo)
        elif format == 2:
            if 'daily' in meteo:
                pd.DataFrame(meteo['daily']).to_excel(filepath+"_daily.xlsx")
                return pd.DataFrame(meteo['daily'])
            else:
                pd.DataFrame(meteo).to_excel(filepath+".xlsx")
                return pd.DataFrame(meteo)
        else:
            raise FileOptionError


class Options_Historical():
    """
    The API Options accepts a WGS4 coordinate and other  weather variables .
    Time always starts at 0:00 today and contains 168 hours.
    """

    def __init__(self, latitude, longitude, start_date, end_date, timeformat=iso8601, timezone=UTC, windspeed_unit=kmh,  precipitation_unit=mm):
        """
        Args:
            latitude (float): Latitude (Geographical WGS84 coordiante of the location).
            longitude (float): Longitude (Geographical WGS84 coordiante of the location).
            windspeed_unit (string, optional): Other wind speed speed units: ms, mph and kn.
            precipitation_unit (string, optional): Other precipitation amount units: inch.
            timeformat (string, optional): If format unixtime is selected, all time values are returned in UNIX epoch time in seconds.
                                            Please note that all time is then in UTC! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date.
            timezone (string, optional): If timezone is set, all timestamps are returned as local-time and data is returned starting at 0:00 local-time.
                                        Any time zone name from the time zone database is available under timezones.py .
            start_date(string): Start date for historical weather search, specified in YYYY-MM-DD
            end_date(string): End date for historical weather search, specified in YYYY-MM-DD
            ValueError: Raises when latitude is not between -90 and 90 degrees.
            ValueError: Raises when longitude is not between -180 and 180 degrees.
        """
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude should be between -90 and 90 degrees.")
        if longitude < -180 or longitude > 180:
            raise ValueError(
                "Longitude should be between -180 and 180 degrees.")
        self.latitude = latitude
        self.longitude = longitude
        self.windspeed_unit = windspeed_unit
        self.precipitation_unit = precipitation_unit
        self.timeformat = timeformat
        self.timezone = timezone
        self.start_date = start_date
        self.end_date = end_date
