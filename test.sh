#!/bin/bash

echo help
python3 main.py --help
echo subscribed_regions json
python3 main.py subscribed_regions | wc -l
echo subscribed_regions array
python3 main.py  subscribed_regions --param_format
echo searchable_resource_types json
python3 main.py searchable_resource_types | wc -l
echo searchable_resource_types array
python3 main.py searchable_resource_types --param_format
echo search_resources json
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase | wc -l
echo search_resources with jq
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase |
jq '.[] | {"display_name":.display_name, "identifier":.identifier, "compartment_id":.compartment_id}'
echo search_resources across al regions with jq
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase --all_regions |
jq '.[] | {"display_name":.display_name, "identifier":.identifier, "compartment_id":.compartment_id}'
echo search_resources with jq
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase |
jq '.[] | {"display_name":.display_name, "identifier":.identifier, "compartment_id":.compartment_id}' | wc -l
echo search_resources across al regions with jq
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase --all_regions |
jq '.[] | {"display_name":.display_name, "identifier":.identifier, "compartment_id":.compartment_id}' | wc -l