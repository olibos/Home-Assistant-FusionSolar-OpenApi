# Home Assistant FusionSolar OpenAPI Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Integrate FusionSolar into you Home Assistant.

FusionSolar allows you to query your plants through an [OpenAPI](https://forum.huawei.com/enterprise/en/communicate-with-fusionsolar-through-an-openapi-account/thread/591478-100027).

## Installation
At this point the integration is not part of the default HACS repositories, so
you will need to add this repository as a custom repository in HACS.

When this is done, just install the repository.

## Requirements
### Create an OpenAPI account.
1. Contact service team at eu_inverter_support@huawei.com to create an openAPI account for your plant.
2. Get credentials
3. Find your PlantID (aka station code)\
Follow the documentation and especially the [Step 5: Interface of Plant List](https://forum.huawei.com/enterprise/en/communicate-with-fusionsolar-through-an-openapi-account/thread/591478-100027#:~:text=Interface%20of%20Plant%20List)
![image](https://forum.huawei.com/enterprise/en/data/attachment/forum/201912/26/231051iegoqemvx5eeo3a5.png?9.png)
Copy the stationCode.

## Configuration
### configuration.yaml
Add the code below:
```yml
sensor:
  - platform: fusion_solar_openapi
    credentials:
      username: !secret fusion_solar_username
      password: !secret fusion_solar_password
    plants:
      - id: "REPLACE THIS WITH YOUR STATION CODE"
        name: "A readable name for the plant"
```
### Use secrets
I strongly advise to store your crendials as a secret. 

More information on secrets: [Storing secrets](https://www.home-assistant.io/docs/configuration/secrets/).

### Multiple plants
You can configure multiple plants:
```yml
sensor:
  - platform: fusion_solar_openapi
    credentials:
      username: !secret fusion_solar_username
      password: !secret fusion_solar_password
    plants:
      - id: "REPLACE THIS WITH YOUR STATION CODE XXXXX"
        name: "A readable name for plant XXXXX"
      - id: "REPLACE THIS WITH YOUR STATION CODE YYYYY"
        name: "A readable name for plant YYYYY"
```

### Credits
This integration is based on the awsome work of @tijsverkoyen on https://github.com/tijsverkoyen/Home-Assistant-FusionSolar-Kiosk/