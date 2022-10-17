"""Constants for FusionSolar OpenAPI."""
# Base constants
DOMAIN = 'fusion_solar_openapi'

# Configuration
CONF_PLANTS = 'plants'
CONF_CREDENTIALS = 'credentials'

# Fusion Solar OpenAPI response attributes
ATTR_DATA = 'data'
ATTR_FAIL_CODE = 'failCode'
ATTR_SUCCESS = 'success'
ATTR_DATA_REALKPI = 'dataItemMap'
ATTR_DATA_STATIONCODE = 'stationCode'
ATTR_DATA_DEVID = 'devId'
ATTR_DATA_DEVTYPEID = 'devTypeId'

# Data attributes
ATTR_TOTAL_CURRENT_DAY_ENERGY = 'day_power'
ATTR_TOTAL_CURRENT_MONTH_ENERGY = 'month_power'
ATTR_TOTAL_LIFETIME_ENERGY = 'total_power'
ATTR_INVERTER_STATE = 'inverter_state';
ATTR_ACTIVE_POWER = 'active_power';

# Possible ID suffixes
ID_REALTIME_POWER = 'realtime_power'
ID_STATE = 'state'
ID_TOTAL_CURRENT_DAY_ENERGY = 'total_current_day_energy'
ID_TOTAL_CURRENT_MONTH_ENERGY = 'total_current_month_energy'
ID_TOTAL_LIFETIME_ENERGY = 'total_lifetime_energy'

# Possible Name suffixes
NAME_REALTIME_POWER = 'Realtime Power'
NAME_STATE = 'State'
NAME_TOTAL_CURRENT_DAY_ENERGY = 'Total Current Day Energy'
NAME_TOTAL_CURRENT_MONTH_ENERGY = 'Total Current Month Energy'
NAME_TOTAL_LIFETIME_ENERGY = 'Total Lifetime Energy'

InverterState = {
    0: 'Standby: initializing',
    1: 'Standby: insulation resistance detection',
    2: 'Standby: sunlight detection',
    3: 'Standby: power grid detection',
    256: 'Start',
    512: 'Grid connection',
    513: 'Grid connection: limited power',
    514: 'Grid connection: self-derating',
    768: 'Shutdown: unexpected shutdown',
    769: 'Shutdown: commanded shutdown',
    770: 'Shutdown: OVGR',
    771: 'Shutdown: communication disconnection',
    772: 'Shutdown: limited power',
    773: 'Shutdown: manual startup is required',
    774: 'Shutdown: DC switch disconnected',
    1025: 'Grid scheduling: cosψ-P curve',
    1026: 'Grid scheduling: Q-U curve',
    1280: 'Spot-check ready',
    1281: 'Spot-checking',
    1536: 'Inspecting',
    1792: 'AFCI self-check',
    2048: 'I-V scanning',
    2304: 'DC input detection',
    40960: 'Standby: no sunlight',
    45056: 'Communication disconnection (written by the SmartLogger)',
    49152: 'Loading (written by the SmartLogger)'
}