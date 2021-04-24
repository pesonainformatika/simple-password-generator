data_dict = {
    'username': ['pery', 'bayu', 'fajar', 'iqbal']
}


def passMaker(dict_keys):
    password_list = []
    username_list = []
    for username in dict_keys:
        generate_password = sum(ord(c) for c in username)
        password_list.append(f"{username}{generate_password}")
        username_list.append(username)

    # append result
    named_dict = {
        "username": username_list,
        "generate_password": password_list
    }

    return named_dict


print(passMaker(data_dict['username']))
