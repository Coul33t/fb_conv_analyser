from datetime import datetime, date, timedelta

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
        words = self.number_of_words_per_message()
        return sum(words)

    def mean_number_of_words(self):
        messages_length = self.number_of_words_per_message()
        return sum(messages_length)/len(messages_length)

    def number_of_words_per_day(self):
        if not self.messages:
            return {}

        number_of_words = {}

        beginning = self.messages[-1]['datetime'].date()
        end = self.messages[0]['datetime'].date()
        current_day = beginning

        while current_day <= end:
            number_of_words[current_day] = 0
            current_day += timedelta(days=1)

        for mess in self.messages:
            number_of_words[mess['datetime'].date()] += len(mess['content'].split(' '))

        return number_of_words

    def number_of_words_per_week(self):
        if not self.messages:
            return {}

        number_of_words = {}

        beginning = self.messages[-1]['datetime'].date()
        end = self.messages[0]['datetime'].date()

        if beginning.isoweekday() != 1:
            beginning = beginning - timedelta(days=beginning.isoweekday() - 1)

        if end.isoweekday() != 1:
            end = end - timedelta(days= end.isoweekday() - 1)

        current_week = beginning

        while current_week <= end:
            number_of_words[current_week] = 0
            current_week += timedelta(days=7)

        for mess in self.messages:
            if mess['datetime'].date().isoweekday() != 1:
                number_of_words[(mess['datetime'].date() - timedelta(days=mess['datetime'].date().isoweekday() - 1))] += len(mess['content'].split(' '))
            else:
                number_of_words[mess['datetime'].date()] += len(mess['content'].split(' '))

        return number_of_words

    def number_of_messages_per_day(self):
        if not self.messages:
            return {}

        number_of_messages = {}

        beginning = self.messages[-1]['datetime'].date()
        end = self.messages[0]['datetime'].date()
        current_day = beginning

        while current_day <= end:
            number_of_messages[current_day] = 0
            current_day += timedelta(days=1)

        for mess in self.messages:
            number_of_messages[mess['datetime'].date()] += 1

        return number_of_messages

    def number_of_messages_per_week(self):
        if not self.messages:
            return {}

        number_of_messages = {}

        beginning = self.messages[-1]['datetime'].date()
        end = self.messages[0]['datetime'].date()

        if beginning.isoweekday() != 1:
            beginning = beginning - timedelta(days=beginning.isoweekday() - 1)

        if end.isoweekday() != 1:
            end = end - timedelta(days= end.isoweekday() - 1)

        current_week = beginning

        while current_week <= end:
            number_of_messages[current_week] = 0
            current_week += timedelta(days=7)

        for mess in self.messages:
            if mess['datetime'].date().isoweekday() != 1:
                number_of_messages[(mess['datetime'].date() - timedelta(days=mess['datetime'].date().isoweekday() - 1))] += 1
            else:
                number_of_messages[mess['datetime'].date()] += 1

        return number_of_messages

    def get_basic_stats(self):
        print(f'Total number of messages: {self.number_of_messages}')