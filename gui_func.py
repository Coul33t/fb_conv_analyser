import os
import locale
import json
import operator

from datetime import datetime, date, timedelta

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from conversation import Conversation
from tools import convert_timestamp_to_date, normalise_length

import pdb


def set_conversation_list(path):
        fb_user_ignored = 0
        print("Creating name list from conversation folder...")
        yo = [name.encode('latin1').decode('utf8') for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        list_of_conv = []

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
                                    list_of_conv.append([", ".join([x['name'].encode('latin1').decode('utf8') for x in v]), name])
                            break

                except FileNotFoundError:
                    print(f'WARNING: {name} does not have a message.json file')

        print(f'WARNING: \'facebookuser\' ignored: {fb_user_ignored}')

        return list_of_conv

def set_conversation_list_cached(combobox):
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

def load_conv_data(path):
    conv = Conversation()

    with open(path + r'\message.json', 'r', encoding=locale.getpreferredencoding()) as f:
        jsonf = json.load(f)

        for k, v in jsonf.items():
            if k == 'participants':
                for names in v:
                    conv.add_name(names['name'].encode('latin1').decode('utf8'))

            if k == 'messages':
                for single_message in v:
                    single_message['sender_name'] = single_message['sender_name'].encode('latin1').decode('utf8')
                    conv.add_message(single_message)

    convert_timestamp_to_date(conv)
    conv.convert_persons_timestamp_to_date()

    return conv

def append_conv_data(path, conv):
    with open(path + r'\message.json', 'r', encoding=locale.getpreferredencoding()) as f:
        jsonf = json.load(f)

        for k, v in jsonf.items():
            if k == 'messages':
                for single_message in v:
                    single_message['sender_name'] = single_message['sender_name'].encode('latin1').decode('utf8')
                    conv.add_message(single_message)

    convert_timestamp_to_date(conv)
    conv.convert_persons_timestamp_to_date()
    return conv


def plot_single_data(data, dates=False):
    data = np.asarray(list(data.values()))
    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    x = np.asarray([i for i in range(len(data))])
    ax.bar(x, data)
    plt.show()

def plot_dual_data(data, dates=False, visualisation='Stacked bar'):

    data = normalise_length(data)
    new_data = []

    for k in data.keys():
        # Since the normalise_length() method insert keys at the end,
        # we have to make sure that the obtained data is in the correct
        # order.
        tmp_data = sorted(data[k].items(), key=operator.itemgetter(0))
        new_data.append(np.asarray([x[1] for x in tmp_data]))

    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    x = np.asarray([i for i in range(len(new_data[0]))])

    if visualisation == 'Stacked bar':
        ax.bar(x, new_data[0], width=0.5, color='b', align='center')
        ax.bar(x, new_data[1], bottom=new_data[0], width=0.5, color='r', align='center')

    elif visualisation == 'Stacked area':
        ax.stackplot(x, new_data)

    elif visualisation == 'Stacked areas (percentage)':
        pass

    plt.show()

def plot_multiple_data(data, names, data_type, dates, visualisation='Stacked bar'):
    data = normalise_length(data)
    new_data = []

    for k in data.keys():
        # Since the normalise_length() method insert keys at the end,
        # we have to make sure that the obtained data is in the correct
        # order.
        tmp_data = sorted(data[k].items(), key=operator.itemgetter(0))
        new_data.append(np.asarray([x[1] for x in tmp_data]))

    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    x = np.asarray([i for i in range(len(new_data[0]))], dtype=np.float64)

    beg = dates[0].strftime('%d-%m-%Y')
    end = dates[1].strftime('%d-%m-%Y')

    if visualisation == 'Stacked bar':
        color=iter(cm.rainbow(np.linspace(0,1,len(new_data))))
        for i, single_data in enumerate(new_data):
            c = next(color)
            if i == 0:
                ax.bar(x, single_data, width=0.5, color=c, align='center', label=names[i])
            else:
                ax.bar(x, single_data, bottom=new_data[i-1], width=0.5, color=c, align='center', label=names[i])

    if visualisation == 'Stacked bar (percentage)':
        total = sum(new_data)
        new_data = new_data / total
        new_data[np.isnan(new_data)] = 0
        color=iter(cm.rainbow(np.linspace(0,1,len(new_data))))
        for i, single_data in enumerate(new_data):
            c = next(color)
            if i == 0:
                ax.bar(x, single_data, width=0.5, color=c, align='center', label=names[i])
            else:
                ax.bar(x, single_data, bottom=new_data[i-1], width=0.5, color=c, align='center', label=names[i])

    if visualisation == 'Stacked bar (cumulative)':
        new_data = np.cumsum(new_data, axis=1)
        color=iter(cm.rainbow(np.linspace(0,1,len(new_data))))
        for i, single_data in enumerate(new_data):
            c = next(color)
            if i == 0:
                ax.bar(x, single_data, width=0.5, color=c, align='center', label=names[i])
            else:
                ax.bar(x, single_data, bottom=new_data[i-1], width=0.5, color=c, align='center' , label=names[i])

    elif visualisation == 'Stacked area':
        ax.stackplot(x, new_data, labels=names)

    elif visualisation == 'Stacked area (percentage)':
        total = sum(new_data)
        new_data = new_data / total
        new_data[np.isnan(new_data)] = 0
        ax.stackplot(x, new_data, labels=names)

    elif visualisation == 'Stacked area (cumulative)':
        new_data = np.cumsum(new_data, axis=1)
        ax.stackplot(x, new_data, labels=names)

    if visualisation != 'Pie chart':
        ax.set_ylabel(f'Number of {data_type[0]}')
        ax.set_xlabel(f'{data_type[1]}')

    plt.title(f'Number of {data_type[0].lower()} sent per {data_type[1].lower()} between {beg} and {end}')
    plt.legend()
    plt.show()

def plot_pie_chart(data, names, data_type, dates, visualisation='Pie chart'):
    new_data = []

    for k in data.keys():
        new_data.append(np.asarray(data[k]))

    fig = plt.figure(figsize=(9,9))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    beg = dates[0].strftime('%d-%m-%Y')
    end = dates[1].strftime('%d-%m-%Y')

    ax.pie(new_data, labels=names)

    plt.title(f'Number of {data_type[0].lower()} sent between {beg} and {end}')
    plt.legend()
    plt.show()
