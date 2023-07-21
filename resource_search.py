from oci import resource_search

import iam
import util
import json

searchable_resource_types_field = 'name'


def searchable_resource_types(config, args):
    """
    Return list of searchable resource types
    :param config:
    :param args:
    :return: Array of Resource Types
        --param_format: returns array of name
    """
    search = resource_search.ResourceSearchClient(config)
    return util.oci_page_iterator(search.list_resource_types, args, param_field=searchable_resource_types_field)


def search_resources(config, args):
    compartments = iam.compartment_dictionary(config)
    search = resource_search.ResourceSearchClient(config)
    rt = ', '.join(args.resource_type) if args.resource_type is not None else 'all'
    query = 'query ' + rt + ' resources'
    resources = util.oci_page_iterator(search.search_resources, args,
                                       resource_search.models.StructuredSearchDetails(query=query),
                                       nested_array_field='items')
    resources_json = []
    for resource in resources:
        resource_json = json.loads(str(resource))
        resource_json['compartment_name'] = compartments[resource.compartment_id]
        resources_json.append(resource_json)
    return resources_json
