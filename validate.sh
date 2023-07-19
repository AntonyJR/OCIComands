#!/bin/bash
# Validates that the commands work in your environment.
echo Testing help
echo ============
python3 main.py --help
echo ===================================================================================
echo This verifies that you have correctly installed Python, argparse and OCI Python SDK
echo Verify that you can see the help screen and then press Enter to continue
read -s

echo
echo Testing subscribed_regions array
echo ================================
python3 main.py  subscribed_regions --param_format
echo ===================================================================================
echo This verifies that OCI client is correctly configured on your machine
echo Verify that you can see a list of subscribed regions and then press Enter to continue
read -s

echo
echo Testing jq
echo ================================
echo '{ "str1": "All", "str2": "looks", "str3": "good"}' | jq '[.str1, .str2, .str3]'
echo ===================================================================================
echo This verifies that jq is correctly installed on your machine
echo Verify that you can see an array that says '"All looks good"'
