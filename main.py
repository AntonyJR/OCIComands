import oci
import argparse

import iam
import resource_search

# Commands are registered in this dictionary
# Command string is used by command parameter
# Command string is used to identify correct function to execute
# To add a command, add a new key of the command string passed on command line
# and the value is a reference to the function to execute
commands = {
    'subscribed_regions':
        (iam.subscribed_regions, iam.subscribed_regions_field,
         'List subscribed regions'),
    'searchable_resource_types':
        (resource_search.searchable_resource_types, resource_search.searchable_resource_types_field,
         'List resource types'),
    'search_resources':
        (resource_search.search_resources, None,
         'List resources of provided types in selected regions')
}

# Command line arguments are documented as part of the add_argument
epilog = f'Following commands are supported\n'
for cmd in commands:
    cmdtuple = commands[cmd]
    epilog += '  '+cmd+': '+cmdtuple[2]+'\n'
parser = argparse.ArgumentParser(prog='OCICommands',
                                 description="Helpful OCI scripts",
                                 epilog=epilog,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('command')
parser.add_argument('--config_file', default=oci.config.DEFAULT_LOCATION,
                    help='OCI config file - defaults to OCI DEFAULT_LOCATION')
parser.add_argument('--profile', default=oci.config.DEFAULT_PROFILE,
                    help='OCI profile to use - defaults to OCI DEFAULT_PROFILE')
parser.add_argument('--resource_type', action='append',
                    help='Resource type to search for, may be repeated')
parser.add_argument('--param_format', action='store_true',
                    help='Return a string array rather than json')
parser.add_argument('--all_regions', action='store_true',
                    help='Operate over all regions')


def main():
    args = parser.parse_args()

    config = oci.config.from_file(args.config_file, args.profile)
    oci.config.validate_config(config)

    if args.all_regions:
        regions = iam.region_array(config)
    else:
        regions = [config[oci.config.REGION_KEY_NAME]]
    result = []

    for region in regions:
        config = oci.config.from_file(args.config_file, args.profile)
        config[oci.config.REGION_KEY_NAME] = region

        if args.command not in commands:
            print("Invalid command : " + args.command)
            exit()

        result += commands[args.command][0](config, args)

    print(result)

if __name__ == '__main__':
    main()
