from person import Person
from tools import convert_timestamp_to_date, normalise_length
from datetime import datetime

import pdb

class Conversation:
    def __init__(self):
        self.persons = {}
        self.messages = []
        self.extremum_dates = [0, 0]

    def add_name(self, name):
        self.persons[name] = Person(name)

    def add_message(self, message):
        """ Adds a message to the Conversation list, and to the Person object. """
        self.messages.append(message)

        # In case one of the people isn't in the list (shouldn't be, but eh)
        if message['sender_name'] not in self.persons.keys():
            self.persons[message['sender_name']] = Person(message['sender_name'])

        self.persons[message['sender_name']].add_message(message)

        if self.extremum_dates[0] == 0 and self.extremum_dates[1] == 0:
            self.extremum_dates[0] = message['timestamp_ms']
            self.extremum_dates[1] = message['timestamp_ms']
        else:
            if message['timestamp_ms'] < self.extremum_dates[0]:
                self.extremum_dates[0] = message['timestamp_ms']
            if message['timestamp_ms'] > self.extremum_dates[1]:
                self.extremum_dates[1] = message['timestamp_ms']


    def convert_persons_timestamp_to_date(self):
        """ Adds a new key to each messages dict, being the date in a readable format."""
        for person in self.persons.values():
            convert_timestamp_to_date(person)


    def get_all_messages(self, frequency='Weekly'):
        all_mess = {}

        if frequency == 'Weekly':
            for person in data.keys():
                all_mess[person] = self.persons[person].number_of_messages_per_week()

        elif frequency == 'Daily':
            for person in data.keys():
                all_mess[person] = self.persons[person].number_of_messages_per_day()

        return all_mess


    def get_basic_stats(self):
        string = ""
        string += f'Number of persons: {len(self.persons)}\n'
        for person in self.persons.keys():
            string += f'- {person}\n'
        duration = self.messages[0]['datetime'] - self.messages[-1]['datetime']
        hours = int(duration.seconds / 60 / 60)
        minutes = int(duration.seconds / 60) - 60*int(duration.seconds / 60 / 60)
        seconds = duration.seconds - minutes * 60 - hours * 60 * 60
        string += f'Conversation going from {self.messages[-1]["date"]} to {self.messages[0]["date"]}, for a total of {duration.days} days, {hours} hours, {minutes} minutes and {seconds} seconds\n'
        string += f'Total number of messages: {len(self.messages)}\n'
        for person, v in self.persons.items():
            string += f'- {person}: {v.number_of_messages}\n'
        return string