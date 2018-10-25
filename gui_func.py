import os

def set_conversation_list(combobox):
        fb_user_ignored = 0

        if os.path.isdir(os.getcwd() + r'\cache') and os.path.exists(os.getcwd() + r'\cache\name_list_cache.txt'):
            print("Loading names from cached file...")
            with open(r'cache\name_list_cache.txt', 'r') as list_file:
                data = list_file.read().split('\n')
                for name in data:
                    combobox.addItem(name)

        else:
            print("Creating name list from conversation folder...")
            yo = [name.encode('latin1').decode('utf8') for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
            name_list_to_cache = []

            for name in yo:
                if name.split("_")[0].lower() == "facebookuser":
                    fb_user_ignored += 1
                else:
                    try:
                        with open(path + r'\\' + name + r'\message.json', 'r', encoding=locale.getpreferredencoding()) as f:
                            jsonf = json.load(f)

                            for k, v in jsonf.items():
                                if k == 'participants':
                                    if len(v) > 1:
                                        name_list_to_cache.append(", ".join([x['name'].encode('latin1').decode('utf8') for x in v]))
                                        combobox.addItem(", ".join([x['name'].encode('latin1').decode('utf8') for x in v]))
                                break

                    except FileNotFoundError:
                        print(f'WARNING: {name} does not have a message.json file')

            print(f'WARNING: \'facebookuser\' ignored: {fb_user_ignored}')

            if not os.path.isdir(os.getcwd() + r'\cache'):
                os.mkdir('cache')

            with open(r'cache\name_list_cache.txt', 'w') as list_file:
                print('Caching name list...')
                for name in name_list_to_cache:
                    try:
                        list_file.write(f'{name}\n')
                    except:
                        name = name.encode('utf8')
                        list_file.write(f'{name}\n')