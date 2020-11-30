def ini_to_dict(data):
    elements = filter(lambda x: False if not x or x[0] == ';' or x[0] == '#' else True, map(lambda x: x.strip(), data.split('\n')))
    section = None
    result = {}

    for element in elements:
        if element[0] == '[' and element[-1] == ']':
            section = element[1:-1].strip()
            result[section] = {}
        else:
            element_split = element.split('=')
            result[section][element_split[0].strip()] = element_split[1].strip().split(';')[0].split('#')[0].split(',') if len(element_split[1].strip().split(',')) > 1 else element_split[1].strip().split(';')[0].split('#')[0]

    return result

def dict_to_ini(data):
    result = ''

    for i, j in data.items():
        result += '[{}]\n'.format(i)

        for k, l in j.items():
            result += '{} = {}\n'.format(k, ', '.join(l)) if isinstance(l, list) else '{} = {}\n'.format(k, l)

    return result
