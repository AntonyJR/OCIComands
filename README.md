# Useful Commands for Managing Oracle Integration in OCI
## Setup
Following are pre-requisites to using the commands:
- Python 3 - [Python.org downloads](https://www.python.org/downloads/)
  - Make sure to install Python 3.6+
- argparse - [library used by the commands to parse command line](https://pypi.org/project/argparse/)
  - There are multiple ways to do it, but I recommend using `pip install argparse`
- OCI Python SDK - [Oracle.com installation instructions](https://docs.oracle.com/en-us/iaas/tools/python/2.107.0/installation.html#pypi)
  - There are multiple ways to do it, but I recommend using `pip install oci`
- OCI client config on machine that will run Python - [Oracle.com Required Keys and OCIDs](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm)
- jq - [jq download page](https://jqlang.github.io/jq/download/)
  - Not needed for the commands themselves but used by the test script which verifies your installation is working and is handy for transforming json output into just the format you need.

Note that you can use the [OCI cloud shell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro.htm) which has all the above already configured.

## Running the Commands
The commands are run using the following syntax:

  `python3 main.py <command> <options>`

By default, the commands return json but --param_format can be used to return an array of strings of the most important field.

## Available Commands
| Command | Action                                                                                                                   | Command Specific Parameters |
|---------|--------------------------------------------------------------------------------------------------------------------------|------------|
| subscribed_regions | List subscribed regions                                                                                                  | --param_format |
| searchable_resource_types | List resource types                                                                                                      | --param_format |
| search_resources | List resources of provided types in selected regions, <br/>if no type of resource is provided then all resources are returned | --resource_type |

### Global Parameters
The following parameters are applicable to all commands
| Parameter | Meaning |
|-----------|---------|
| -h, --help | Show help message and exit |
| --config_file CONFIG_FILE | OCI config file - defaults to OCI DEFAULT_LOCATION |
| --profile PROFILE | OCI profile to use - defaults to OCI DEFAULT_PROFILE |
| --all_regions | Operate over all subscribed regions |

### Command Specific Parameters
The following parameters are applicable to a subset of commands
| Parameter | Meaning | Commands |
|-----------|---------|----------|
| --param_format | Return a string array rather than json | subscribed_regions, searchable_resource_types |
| --resource_type RESOURCE_TYPE | Resource type to search for, may be repeated | search_resources |

## Examples

### Get subscribed regions as an array of strings
`python3 main.py  subscribed_regions --param_format`

### Get all searchable resource types as json using a specific OCI profile
`python3 main.py searchable_resource_types --profile MY_PROFILE`

### Get all integration and autonomous database instances across all regions using a different OCI config location
`python main.py search_resources --resource_type IntegrationInstance --resource_type AutonomousDatabase --all_regions --config /home/some/dir/config`

## Verifying your installation
To validate your installation run the command `validate.sh`.

You may also run `test.sh` which performs a test of all the features.
