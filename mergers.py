# python 3.9

def dict_merge(*dicts):
    data_dict = {}
    for args in dicts:
        data_dict.update(args)
    return data_dict

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict3 = {'Status': 'single', 'Age': 27}
dict4 = {'Occupation':'nurse', 'Wage': 3000}

print(dict_merge(dict1, dict2, dict3, dict4))