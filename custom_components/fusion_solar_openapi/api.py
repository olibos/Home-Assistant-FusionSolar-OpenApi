"""API client for FusionSolar OpenAPI."""
import logging
import html
import json
from requests import (post)
from time import (sleep)

from .const import (
    ATTR_DATA,
    ATTR_FAIL_CODE,
    ATTR_SUCCESS,
    ATTR_DATA_REALKPI
)

from requests import get

_LOGGER = logging.getLogger(__name__)

ApiError = {
    ATTR_SUCCESS: False
}
class FusionSolarOpenApi:
    def __init__(self, baseUrl, username, password):
        self._baseUrl = baseUrl
        self._username = username
        self._password = password

    def getRealTimeKpi(self, plantId: str):
        loginJson = { 
            "userName": self._username,
            "systemCode": self._password
        }

        headers = {
            'accept': 'application/json',
        }

        try:
            response = post(self._baseUrl + "login", json=loginJson, headers=headers)
            if ("XSRF-TOKEN" not in response.cookies):
                return ApiError
            token = response.cookies["XSRF-TOKEN"]
            headers = headers | {
                "XSRF-TOKEN": token,
            }

            for attempt in range(10):
                sleep(.5 * attempt)
                response = post(self._baseUrl + "getStationRealKpi", json={"stationCodes":plantId}, headers=headers)
                json = response.json();
                if (ATTR_SUCCESS in json and json[ATTR_SUCCESS]):
                    break

            return json[ATTR_DATA][0][ATTR_DATA_REALKPI]

        except Exception as error:
            _LOGGER.error(error)
            _LOGGER.error(response.text)
    
        return ApiError

class FusionSolarKioskApiError(Exception):
    pass
