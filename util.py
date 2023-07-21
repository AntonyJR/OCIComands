def oci_page_iterator(ocifunc, args, *ociargs, param_field=None, paged=True, nested_array_field=None, use_args=True,
                      **ocikwargs):
    retval = []
    page = None
    if paged:
        ocikwargs['limit'] = 1000
    while True:
        if paged:
            ocikwargs['page'] = page
        resp = ocifunc(*ociargs, **ocikwargs)
        resp_data = lambda: resp.data if nested_array_field is None else getattr(resp.data, nested_array_field)
        if use_args and args.param_format:
            retval += [getattr(obj, param_field) for obj in resp_data()]
        else:
            retval += resp_data()
        if paged and resp.has_next_page:
            page = resp.next_page
            continue
        else:
            break
    return retval
