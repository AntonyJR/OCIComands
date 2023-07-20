from oci import resource_search
import util

searchable_resource_types_field = 'name'


def searchable_resource_types(config, args):
    """
    Return list of searchable resource types
    :param config:
    :param args:
    :param regions:
    :return: Array of Resource Types
        --param_format: returns array of name
    """
    search = resource_search.ResourceSearchClient(config)
    return util.oci_page_iterator(search.list_resource_types, args, param_field=searchable_resource_types_field)


def search_resources(config, args):
    search = resource_search.ResourceSearchClient(config)
    rt = ', '.join(args.resource_type) if args.resource_type is not None else 'all'
    query = 'query ' + rt + ' resources'
    return util.oci_page_iterator(search.search_resources, args,
                                  resource_search.models.StructuredSearchDetails(query=query),
                                  nested_array_field='items')
