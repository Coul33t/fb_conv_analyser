from datetime import datetime
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
        print(f'Total number of messages: {len(self.messages)}')
        for person, v in self.persons.items():
            print(f'- {person}: {v.number_of_messages}')


def convert_timestamp_to_date(obj):
    """ Adds a new key to each messages dict, being the date in a readable format."""
    for mess in obj.messages:
            mess['date'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000).strftime('%Y-%m-%d %H:%M:%S')


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
    conv.persons['Juliette Rbe'].get_messages_date()
    conv.get_basic_stats()
    pdb.set_trace()


if __name__ == '__main__':
    main()