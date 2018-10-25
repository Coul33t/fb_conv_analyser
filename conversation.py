from person import Person

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