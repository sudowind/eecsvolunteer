def qset2list(qset):
    fields = qset.model._meta.get_all_field_names()
    result = []
    for q in qset:
        item = dict()
        for f in fields:
            try:
                if f == 'activity':
                    item[f] = getattr(q, f).id
                else:
                    item[f] = getattr(q, f)
            except AttributeError:
                continue
        result.append(item)
    return result
