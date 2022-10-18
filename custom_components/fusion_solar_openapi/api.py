"""API client for FusionSolar OpenAPI."""
import html
import json
import logging
from homeassistant.const import ATTR_ID
from .const import *

from requests import Session
from time import (sleep)

from .const import (
    ATTR_DATA,
    ATTR_FAIL_CODE,
    ATTR_SUCCESS,
    ATTR_DATA_REALKPI
)

_LOGGER = logging.getLogger(__name__)

class FusionSolarOpenApi:
    def __init__(self, baseUrl, username, password):
        self._baseUrl = baseUrl
        self._username = username
        self._password = password
        self._session = Session()
        self._session.headers.update({'Content-Type': 'application/json'});

    def post(self, method: str, data):
        session = self._session
        for attempt in range(10):
            sleep(.5 * attempt)
            response = session.post(self._baseUrl + method, json=data)
            json = response.json();
            if (ATTR_SUCCESS in json and json[ATTR_SUCCESS]):
                token= response.cookies.get(name='XSRF-TOKEN')
                if (token):
                    session.headers.update({ 'XSRF-TOKEN': token })
                _LOGGER.debug(f'Request: {method}\nResponse: {json}')
                return json
        
        raise FusionSolarKioskApiError(f'Unable to get data from {method}')

    def getRealTimeKpi(self, plantId: str):
        try:
            self.post("login", { "userName": self._username, "systemCode": self._password });
            if ("XSRF-TOKEN" not in self._session.headers):
                raise FusionSolarKioskApiError("Unable to get token.")

            kpi = self.post('getStationRealKpi', {"stationCodes":plantId})[ATTR_DATA][0][ATTR_DATA_REALKPI]
            if (ATTR_TOTAL_CURRENT_DAY_ENERGY not in kpi):
                raise FusionSolarKioskApiError(f"Invalid response from API (missing {ATTR_TOTAL_CURRENT_DAY_ENERGY})")

            devInfo = next(filter(lambda d: d.get("devTypeId") in [1, 38], self.post('getDevList', {"stationCodes":plantId})[ATTR_DATA]), None)
            _LOGGER.debug(f'Selected device: {devInfo}')
            devKpi = self.post('getDevRealKpi', {"stationCodes":plantId, "devIds": str(devInfo[ATTR_ID]), "devTypeId": devInfo[ATTR_DATA_DEVTYPEID]})[ATTR_DATA][0][ATTR_DATA_REALKPI]
            if (ATTR_ACTIVE_POWER not in devKpi):
                raise FusionSolarKioskApiError(f"Invalid response from API (missing {ATTR_ACTIVE_POWER})")
            if (ATTR_INVERTER_STATE not in devKpi):
                raise FusionSolarKioskApiError(f"Invalid response from API (missing {ATTR_INVERTER_STATE})")

            kpi[ATTR_ACTIVE_POWER] = devKpi[ATTR_ACTIVE_POWER]
            kpi[ATTR_INVERTER_STATE] = devKpi[ATTR_INVERTER_STATE]
            return kpi

        except FusionSolarKioskApiError as error:
            raise error

        except Exception as error:
            raise FusionSolarKioskApiError(f"Unknown error {error}") from error

class FusionSolarKioskApiError(Exception):
    pass
