from os import stat
import requests


class Buienradar:
    def __init__(self, lattitude: str, longitude: str):
        self.lattitude = lattitude
        self.longitude = longitude

    @staticmethod
    def _get_request_data(url: str) -> str:
        """executes the get request against a url and returns only the
        raw data

        Args:
            url (str): url

        Returns:
            str: raw binary string returned from the get requests
        """
        data = requests.get(url=url, timeout=30)
        return data.content

    def get_precipitation_text(self) -> list:
        """wil get the rain data for the provided long and lattitude in
        the following format:

        [
            "000|15:10",
            "000|15:15",
            "000|15:20",
            "077|15:25",
            "077|15:30",
        ]

        Returns:
            list: list of 24 items of rain data
        """
        rain_url = (
            "https://gpsgadget.buienradar.nl/data/raintext?"
            f"lat={self.lattitude}&lon={self.longitude}"
        )
        get_raw_data = self._get_request_data(rain_url)
        return [
            line.split("|")
            for line in get_raw_data.decode().split("\n")
            if line
        ]

    def get_next_rain_moment(self) -> list:
        """Will return the closest rain, time pair

        Returns:
            list: rain in mm, time in cet
        """
        data = self.get_precipitation_text()
        for rain, time in data:
            if int(rain) > 0:
                return [rain, time]
            else:
                continue
        return data[-1]
