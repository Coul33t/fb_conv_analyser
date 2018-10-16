from datetime import datetime

import sys
from PyQt5.QtWidgets import QApplication, QWidget

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


def plot_single_data(data):
    pdb.set_trace()
    pass

def main():
    path = r'C:\Users\quentin\Desktop\fb_json\messages\JulietteRbe_d46ca96a16'

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
    print(len(conv.persons['Juliette Rbe'].get_messages_date(begin=datetime(2018,10,1))))
    print(len(conv.persons['Quentin Cld'].get_messages_date(begin=datetime(2018,10,1))))
    conv.get_basic_stats()
    plot_single_data(conv.persons['Juliette Rbe'].number_of_words_per_message())
    pdb.set_trace()


if __name__ == '__main__':
    # app = QApplication(sys.argv)

    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()

    # sys.exit(app.exec_())
    main()

