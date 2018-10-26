from datetime import datetime

def convert_timestamp_to_date(obj):
    """ Adds a new key to each messages dict, being the date in a readable format."""
    for mess in obj.messages:
        mess['date'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000).strftime('%d-%m-%Y (%H:%M:%S)')
        mess['datetime'] = datetime.utcfromtimestamp(mess['timestamp_ms'] / 1000)