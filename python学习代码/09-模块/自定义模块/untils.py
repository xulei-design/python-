def str_to_int(str_data):
    '''
    :param str_data:
    :return:
    '''
    if str_data.isdecimal():
        return int(str_data)
    return None