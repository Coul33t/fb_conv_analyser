# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta

import numpy as np

import sys

import os

from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)

import matplotlib.pyplot as plt

import json
import locale
import pdb

class Person:
    def __init__(self, name):
        self.name = name
        self.number_of_messages = 0
        self.messages = []
        self.extremum_dates = [0,0]

    def add_message(self, message):
        self.messages.append(message)
        self.number_of_messages += 1
        if message['timestamp_ms'] < self.extremum_dates[0]:
            self.extremum_dates[0] = message['timestamp_ms']
        if message['timestamp_ms'] > self.extremum_dates[1]:
            self.extremum_dates[1] = message['timestamp_ms']

    def get_messages_date(self, begin=datetime(2000, 1, 1), end=datetime.now()):
        list_of_messages = []

        if type(begin) == datetime:
            begin = int(begin.timestamp())
        if type(end) == datetime:
            end = int(end.timestamp())

        if not (begin > self.extremum_dates[1] or end < self.extremum_dates[0]):
            for mess in self.messages:
                if int(mess['timestamp_ms'] / 1000) > begin and int(mess['timestamp_ms'] / 1000) < end:
                    list_of_messages.append(mess)

        return list_of_messages

    def number_of_words_per_message(self):
        messages_length = []
        for mess in self.messages:
            messages_length.append(len(mess['content'].split()))
        return messages_length

    def total_number_of_words(self):
        sum(number_of_words_per_message)

    def mean_number_of_words(self):
        messages_length = self.number_of_words_per_message()
        return sum(messages_length)/len(messages_length)

    def number_of_messages_per_day(self):
        number_of_messages = {}

        beginning = self.messages[-1]['datetime'].date()
        end = self.messages[0]['datetime'].date()
        current_day = beginning

        while current_day <= end:
            number_of_messages[current_day.isoformat()] = 0
            current_day += timedelta(days=1)

        for mess in self.messages:
            number_of_messages[mess['datetime'].date().isoformat()] += 1

        return number_of_messages

    def number_of_messages_per_week(self):
        number_of_messages = {}

        beginning = self.messages[-1]['datetime'].date()
        end = self.messages[0]['datetime'].date()

        if beginning.isoweekday() != 1:
            beginning = beginning - timedelta(days=beginning.isoweekday() - 1)

        if end.isoweekday() != 1:
            end = end - timedelta(days= end.isoweekday() - 1)

        current_week = beginning

        while current_week <= end:
            number_of_messages[current_week.isoformat()] = 0
            current_week += timedelta(days=7)

        for mess in self.messages:
            if mess['datetime'].date().isoweekday() != 1:
                number_of_messages[(mess['datetime'].date() - timedelta(days=mess['datetime'].date().isoweekday() - 1)).isoformat()] += 1
            else:
                number_of_messages[mess['datetime'].date().isoformat()] += 1

        return number_of_messages

    def get_basic_stats(self):
        print(f'Total number of messages: {self.number_of_messages}')


class Conversation:
    def __init__(self):
        self.persons = {}
        self.messages = []

    def add_name(self, name):
        self.persons[name] = Person(name)

    def add_message(self, message):
        """ Adds a message to the Conversation list, and to the Person object. """
        self.messages.append(message)

        # In case one of the people isn't in the list (shouldn't be, but eh)
        if message['sender_name'] not in self.persons.keys():
            self.persons[message['sender_name']] = Person(message['sender_name'])

        self.persons[message['sender_name']].add_message(message)

    def convert_persons_timestamp_to_date(self):
        """ Adds a new key to each messages dict, being the date in a readable format."""
        for person in self.persons.values():
            convert_timestamp_to_date(person)


    def get_basic_stats(self):
        print(f'Number of persons: {len(self.persons)}')
        for person in self.persons.keys():
            print(f'- {person}')
        duration = self.messages[0]['datetime'] - self.messages[-1]['datetime']
        hours = int(duration.seconds / 60 / 60)
        minutes = int(duration.seconds / 60) - 60*int(duration.seconds / 60 / 60)
        seconds = duration.seconds - minutes * 60 - hours * 60 * 60
        print(f'Conversation going from {self.messages[-1]["date"]} to {self.messages[0]["date"]}, for a total of {duration.days} days, {hours} hours, {minutes} minutes and {seconds} seconds')
        print(f'Total number of messages: {len(self.messages)}')
        for person, v in self.persons.items():
            print(f'- {person}: {v.number_of_messages}')


def convert_timestamp_to_date(obj):
    """ Adds a new key to each messages dict, being the date in a readable format."""
    for mess in obj.messages:
        mess['date'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000).strftime('%d-%m-%Y (%H:%M:%S)')
        mess['datetime'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000)


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

def plot_dual_data(data, dates=False):
    new_data = []
    #FIX FOR CHARLENE DO NOT KEEP
    # I keep it here so I'll remember to correct this
    # (different length because one didn't send message the last week)
    data[0]['2018-10-08'] = 0
    for person in data:
        new_data.append(np.asarray(list(person.values())))


    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    x = np.asarray([i for i in range(len(new_data[0]))])

    ax.bar(x, new_data[0], width=0.5, color='b', align='center')
    ax.bar(x, new_data[1], bottom=new_data[0], width=0.5, color='r', align='center')
    plt.show()


def main():
    path = r'C:\Users\quentin\Desktop\fb_json\messages\CharleneLemarchand_5e165fd540'

    peoples = ()

    conv = Conversation()

    with open(path + r'\message.json', 'r', encoding=locale.getpreferredencoding()) as f:
        jsonf = json.load(f)

        for k, v in jsonf.items():
            if k == 'participants':
                for names in v:
                    conv.add_name(names['name'])

            if k == 'messages':
                for single_message in v:
                    conv.add_message(single_message)

    convert_timestamp_to_date(conv)
    conv.convert_persons_timestamp_to_date()
    print(len(conv.persons['Charl\u00c3\u00a8ne Lemarchand'].get_messages_date(begin=datetime(2018,10,1))))
    print(len(conv.persons['Quentin Cld'].get_messages_date(begin=datetime(2018,10,1))))
    conv.get_basic_stats()
    # plot_single_data(conv.persons['Juliette Rbe'].number_of_messages_per_day())
    # plot_dual_data([conv.persons['Juliette Rbe'].number_of_messages_per_day(),
    #                 conv.persons['Quentin Cld'].number_of_messages_per_day()])
    plot_dual_data([conv.persons['Charl\u00c3\u00a8ne Lemarchand'].number_of_messages_per_week(),
                    conv.persons['Quentin Cld'].number_of_messages_per_week()])

if __name__ == '__main__':
    main()

