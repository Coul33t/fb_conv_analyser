from datetime import datetime

def convert_timestamp_to_date(obj):
    """ Adds a new key to each messages dict, being the date in a readable format."""
    for mess in obj.messages:
        mess['date'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000).strftime('%d-%m-%Y')
        mess['hour'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000).strftime('%H:%M:%S')
        mess['datetime'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000)


def normalise_length_2(data):
    for person in data.keys():
        pass
        # Check for the latest date
        # for all other values
        #   add missing keys with 0 values

def normalise_length(data):
    beg = list(data[list(data.keys())[0]].keys())[0]
    end = list(data[list(data.keys())[0]].keys())[-1]

    for person in data.keys():
        for dat in data[person].keys():
            if dat < beg:
                beg = dat
            if dat > end:
                end = dat

    for person in data.keys():
        beg_lst = list(data[person].keys())[0]
        if  beg_lst > beg:
            diff = beg_lst - beg
            for i in range(diff.days):
                data[person][beg_lst + timedelta(days=i)] = 0

        end_lst = list(data[person].keys())[-1]
        if end_lst < end:
            diff = end - end_lst
            for i in range(diff.days):
                data[person][end_lst + timedelta(days=i)] = 0

    return data