"""FusionSolar OpenAPI sensor."""
from .api import *
import homeassistant.helpers.config_validation as cv
import logging
import voluptuous as vol

from . import FusionSolarOpenApiEnergyEntity, FusionSolarOpenApiPowerEntity

from datetime import timedelta
from homeassistant.components.sensor import SensorEntity, PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_ID,
    CONF_NAME,
    CONF_PASSWORD,
    CONF_USERNAME
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator, UpdateFailed

from .const import *

CREDENTIALS_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string
    }
)

PLANT_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ID): cv.string,
        vol.Required(CONF_NAME): cv.string
    }
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_CREDENTIALS): CREDENTIALS_SCHEMA,
        vol.Required(CONF_PLANTS): vol.All(cv.ensure_list, [PLANT_SCHEMA]),
    }
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async def async_update_data():
        """Fetch data"""
        try:
            data = {}
            credentials = config[CONF_CREDENTIALS];
            api = FusionSolarOpenApi("https://eu5.fusionsolar.huawei.com/thirdData/", credentials[CONF_USERNAME], credentials[CONF_PASSWORD])
            for plantConfig in config[CONF_PLANTS]:
                plantId = str(plantConfig[CONF_ID])
                data[plantId] = {
                    ATTR_DATA_REALKPI: await hass.async_add_executor_job(api.getRealTimeKpi, plantId)
                }
            return data
        except FusionSolarKioskApiError as error:
            raise UpdateFailed(str(error)) from error

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name='FusionSolarOpenAPI',
        update_method=async_update_data,
        update_interval=timedelta(minutes=5),
    )

    # Fetch initial data so we have data when entities subscribe
    await coordinator.async_refresh()

    for plantConfig in config[CONF_PLANTS]:
        plantId = plantConfig[CONF_ID]
        plantName = plantConfig[CONF_NAME]

        async_add_entities([
            FusionSolarOpenApiSensorState(
                coordinator,
                plantId,
                plantName,
            ),
            FusionSolarOpenApiSensorRealtimePower(
                coordinator,
                plantId,
                plantName,
                ID_REALTIME_POWER,
                NAME_REALTIME_POWER,
                ATTR_ACTIVE_POWER,
            ),
            FusionSolarOpenApiSensorTotalCurrentDayEnergy(
                coordinator,
                plantId,
                plantName,
                ID_TOTAL_CURRENT_DAY_ENERGY,
                NAME_TOTAL_CURRENT_DAY_ENERGY,
                ATTR_TOTAL_CURRENT_DAY_ENERGY,
            ),
            FusionSolarOpenApiSensorTotalCurrentMonthEnergy(
                coordinator,
                plantId,
                plantName,
                ID_TOTAL_CURRENT_MONTH_ENERGY,
                NAME_TOTAL_CURRENT_MONTH_ENERGY,
                ATTR_TOTAL_CURRENT_MONTH_ENERGY,
            ),
            FusionSolarOpenApiSensorTotalLifetimeEnergy(
                coordinator,
                plantId,
                plantName,
                ID_TOTAL_LIFETIME_ENERGY,
                NAME_TOTAL_LIFETIME_ENERGY,
                ATTR_TOTAL_LIFETIME_ENERGY,
            )
        ])

class FusionSolarOpenApiSensorTotalCurrentDayEnergy(FusionSolarOpenApiEnergyEntity):
    pass

class FusionSolarOpenApiSensorTotalCurrentMonthEnergy(FusionSolarOpenApiEnergyEntity):
    pass

class FusionSolarOpenApiSensorTotalLifetimeEnergy(FusionSolarOpenApiEnergyEntity):
    pass

class FusionSolarOpenApiSensorRealtimePower(FusionSolarOpenApiPowerEntity):
    pass

class FusionSolarOpenApiSensorState(CoordinatorEntity, SensorEntity):
    def __init__(
        self,
        coordinator,
        plantId,
        plantName
    ):
        """Initialize the entity"""
        super().__init__(coordinator)
        self._plantId = plantId
        self._plantName = plantName
        self._idSuffix = ID_STATE
        self._nameSuffix = NAME_STATE
        self._attribute = ATTR_INVERTER_STATE

    @property
    def name(self) -> str:
        return f'{self._plantName} ({self._plantId}) - {self._nameSuffix}'

    @property
    def state(self) -> str:
        return InverterState.get(int(self.coordinator.data[self._plantId][ATTR_DATA_REALKPI][self._attribute]), 'Unknown') if self.coordinator.data[self._plantId][ATTR_DATA_REALKPI] else None

    @property
    def unique_id(self) -> str:
        return f'{DOMAIN}-{self._plantId}-{self._idSuffix}'
