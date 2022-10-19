"""
Custom integration to integrate FusionSolar OpenAPI with Home Assistant.
"""
from homeassistant.core import Config, HomeAssistant
from homeassistant.components.sensor import STATE_CLASS_TOTAL_INCREASING, SensorEntity
from homeassistant.const import (
    ENERGY_KILO_WATT_HOUR,
    POWER_KILO_WATT
)
from homeassistant.components.sensor import (
    SensorDeviceClass
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import (
    ATTR_DATA_REALKPI,
    ATTR_TOTAL_LIFETIME_ENERGY,
    DOMAIN,
)

async def async_setup(hass: HomeAssistant, config: Config) -> bool:
    """Set up the FusionSolar OpenAPI component."""
    return True

class FusionSolarOpenApiEnergyEntity(CoordinatorEntity, SensorEntity):
    """Base class for all FusionSolarOpenApiEnergy energy entities."""
    def __init__(
        self,
        coordinator,
        plantId,
        plantName,
        idSuffix,
        nameSuffix,
        attribute,
    ):
        """Initialize the entity"""
        super().__init__(coordinator)
        self._plantId = plantId
        self._plantName = plantName
        self._idSuffix = idSuffix
        self._nameSuffix = nameSuffix
        self._attribute = attribute

    @property
    def device_class(self) -> str:
        return SensorDeviceClass.ENERGY

    @property
    def name(self) -> str:
        return f'{self._plantName} ({self._plantId}) - {self._nameSuffix}'

    @property
    def state(self) -> float:
        return float(self.coordinator.data[self._plantId][ATTR_DATA_REALKPI][self._attribute]) if self.coordinator.data[self._plantId][ATTR_DATA_REALKPI] else None

    @property
    def unique_id(self) -> str:
        return f'{DOMAIN}-{self._plantId}-{self._idSuffix}'

    @property
    def unit_of_measurement(self) -> str:
        return ENERGY_KILO_WATT_HOUR

    @property
    def state_class(self) -> str:
        return STATE_CLASS_TOTAL_INCREASING

    @property
    def native_value(self) -> str:
        return self.state if self.state else ''

    @property
    def native_unit_of_measurement(self) -> str:
        return self.unit_of_measurement

class FusionSolarOpenApiPowerEntity(CoordinatorEntity, SensorEntity):
    """Base class for all FusionSolarOpenApiEnergy power entities."""
    def __init__(
        self,
        coordinator,
        plantId,
        plantName,
        idSuffix,
        nameSuffix,
        attribute,
    ):
        """Initialize the entity"""
        super().__init__(coordinator)
        self._plantId = plantId
        self._plantName = plantName
        self._idSuffix = idSuffix
        self._nameSuffix = nameSuffix
        self._attribute = attribute

    @property
    def device_class(self) -> str:
        return SensorDeviceClass.POWER

    @property
    def name(self) -> str:
        return f'{self._plantName} ({self._plantId}) - {self._nameSuffix}'

    @property
    def state(self) -> float:
        return float(self.coordinator.data[self._plantId][ATTR_DATA_REALKPI][self._attribute]) if self.coordinator.data[self._plantId][ATTR_DATA_REALKPI] else None

    @property
    def unique_id(self) -> str:
        return f'{DOMAIN}-{self._plantId}-{self._idSuffix}'

    @property
    def unit_of_measurement(self) -> str:
        return POWER_KILO_WATT
