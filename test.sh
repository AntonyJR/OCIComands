#!/bin/bash

echo help
echo ==========================================================
python3 main.py --help

echo
echo subscribed_regions json
echo ==========================================================
python3 main.py subscribed_regions | wc -l

echo
echo subscribed_regions array
echo ==========================================================
python3 main.py  subscribed_regions --param_format

echo
echo searchable_resource_types json
echo ==========================================================
python3 main.py searchable_resource_types | wc -l

echo
echo searchable_resource_types array
echo ==========================================================
python3 main.py searchable_resource_types --param_format

echo
echo search_resources json
echo ==========================================================
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase | wc -l

echo
echo search_resources json across all regions
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase --all_regions |
 wc -l

echo
echo search_resources json across all regions with jq
echo ==========================================================
python3 main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase --all_regions |
jq '.[] | {"display_name":.display_name, "identifier":.identifier, "compartment_id":.compartment_id}'
