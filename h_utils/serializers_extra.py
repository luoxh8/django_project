foreign_key_set = ('goods', 'category', 'user', 'balance', 'category_id')


def serializer_list_data(data, serializer, request=None):
    return_data = serializer(data, many=True, context={'request': request}).data
    for value in return_data:
        for k, v in value.items():
            if value[k] is None:
                if k in foreign_key_set:
                    value[k] = 0
                else:
                    value[k] = ''
    return return_data


def serializer_data(data, serializer, request=None):
    return_data = serializer(data, context={'request': request}).data
    for key, value in return_data.items():
        if return_data[key] is None:
            if key in foreign_key_set:
                return_data[key] = 0
            else:
                return_data[key] = ''
    return return_data
