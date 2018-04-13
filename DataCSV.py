import pandas as pd

# Used for encoding
import locale

from datetime import datetime, timedelta

import pdb

class DataCSV:
    def __init__(self, path, file):
        try:
            self.df = pd.read_csv(path + file, encoding=locale.getpreferredencoding())
        except UnicodeDecodeError:
            try:
                self.df = pd.read_csv(path + file, encoding='cp850')
            except UnicodeDecodeError:
                try:
                    self.df = pd.read_csv(path + file, encoding='utf-8')
                except UnicodeDecodeError:
                    try:
                        self.df = pd.read_csv(path + file, encoding='cp1252')
                    except:
                        print(f'WARNING: couldn\'t decode with cp1252')
                        print('ERROR: no correct encoding has been found')
                        return
                    else:
                        print(f'INFO: decoded with cp1252 (local is {locale.getpreferredencoding()})')
                else:
                    print(f'INFO: decoded with utf-8 (local is {locale.getpreferredencoding()})')
            else:
                print(f'INFO: decoded with cp850 (local is {locale.getpreferredencoding()})')

    def columns_names(self):
        return list(self.df.columns.values)

    def rows_number(self):
        return self.df.shape[0]

    def date_ref(self, date_str):
        return datetime.strptime(date_str[:-5] + date_str[-5:].replace(':', ''), '%Y-%m-%dT%H:%M%z')

    def reformate_date(self):
        self.df['date'] = self.df['date'].apply(self.date_ref)


    def keep_values(self, **kwargs):
        # Validating keys
        if not set(kwargs.keys()) & set(self.df.columns.values) == set(kwargs.keys()):
            print('ERROR: bad arguments')
            return

        for key, val in kwargs.items():
            self.df = self.df[self.df[key] == val]

    def get_values(self, **kwargs):
        # Validating keys
        if not set(kwargs.keys()) & set(self.df.columns.values) == set(kwargs.keys()):
            print('ERROR: bad arguments')
            return

        df_r = self.df

        for key, val in kwargs.items():
            df_r = df_r[df_r[key] == val]

        return df_r

    def count_words(self, column=None, value=None):
        counter = 0
        if (column and not value) or (value and not column):
            print('ERROR: if you set a column, you must give a value too (and vice versa)')
            return counter

        if not column or not value:
            for line in self.df.message:
                counter += len(str(line).split())
        else:
            for line in self.df[self.df[column] == value].message:
                counter += len(str(line).split())

        return counter

    def plot_number_words(self, person=None, beg=None, end=None):
        
        data = self.df

        if beg:
            data = data[data['date'] > beg]

        if end:
            data = data[data['date'] < end]

        words_per_day = {}

        for name in data.sender.unique():
            words_per_day[name] = {}
            if not beg:
                beg = data.iloc[0]['date'].date()
            if not end:
                end = data.iloc[-1]['date'].date()

            for i in range((end - beg).days):
                words_per_day[name][(beg + timedelta(i)).strftime('%d-%m-%Y')] = 0

        pdb.set_trace()
        counter = 0

        current_day = data.iloc[0].date.date()

        for idx, row in data.iterrows():

            if row['date'].date() > current_day:
                current_day = row['date'].date()
                words_per_day[row['sender']][current_day.strftime('%d-%m-%Y')] = counter
                counter = 0

            counter += len(str(row['message']).split())
            

        pdb.set_trace()



if __name__ == '__main__':
    data = DataCSV(r'C:\Users\quentin\Desktop\FB\facebook-quentincouland\html\\', r'fb_conv.csv')
    data.keep_values(thread='Marie Sea')
    print('Conversation: Marie Sea')
    print(f'Total word count: {data.count_words()}')
    cld_c = data.count_words(column='sender', value='Quentin Cld')
    sea_c = data.count_words(column='sender', value='Marie Sea')
    print(f'Quentin Cld word count: {cld_c}')
    print(f'Marie Sea word count: {sea_c}')
    data.reformate_date()
    data.plot_number_words()
    pdb.set_trace()