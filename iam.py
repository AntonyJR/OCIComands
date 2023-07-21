from oci import identity
import util

subscribed_regions_field = 'region_name'


def subscribed_regions(config, args):
    """
    Return list of subscribed regions
    :param config: OCI config dictionary
    :param args:
        --param_format: returns array of region_name
    :return: Array of subscribed regions
    """
    iam = identity.IdentityClient(config)
    return util.oci_page_iterator(iam.list_region_subscriptions, args, config['tenancy'],
                                  param_field=subscribed_regions_field, paged=False)


def region_array(config):
    regions = identity.IdentityClient(config).list_region_subscriptions(config['tenancy']).data
    return [region.region_name for region in regions]


def compartment_dictionary(config):
    identity_client = identity.IdentityClient(config)
    compartments = util.oci_page_iterator(identity_client.list_compartments, None, config['tenancy'],
                                          use_args=False, compartment_id_in_subtree=True)
    compartments_dict = {compartment.id: compartment.name for compartment in compartments}
    compartments_dict[config['tenancy']] = identity_client.get_tenancy(config['tenancy']).data.name
    return compartments_dict
