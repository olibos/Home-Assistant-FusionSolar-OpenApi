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

# Data attributes
ATTR_TOTAL_CURRENT_DAY_ENERGY = 'day_power'
ATTR_TOTAL_CURRENT_MONTH_ENERGY = 'month_power'
ATTR_TOTAL_LIFETIME_ENERGY = 'total_power'

# Possible ID suffixes
ID_TOTAL_CURRENT_DAY_ENERGY = 'total_current_day_energy'
ID_TOTAL_CURRENT_MONTH_ENERGY = 'total_current_month_energy'
ID_TOTAL_LIFETIME_ENERGY = 'total_lifetime_energy'

# Possible Name suffixes
NAME_TOTAL_CURRENT_DAY_ENERGY = 'Total Current Day Energy'
NAME_TOTAL_CURRENT_MONTH_ENERGY = 'Total Current Month Energy'
NAME_TOTAL_LIFETIME_ENERGY = 'Total Lifetime Energy'
