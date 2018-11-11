# fb_conv_analyser

A small tool I'm currently developping, used to analyse your Facebook conversations with people. For the moment, it can output the total/per person word count, and plot a graph with these data (either per day or per month). In order to use it, you'll need to extract your data from Facebook in the JSON format (Settings -> Your Facebook Information -> Download your information -> Format: JSON).

Requirement:
1. Python 3.5+
1. PyQt5
1. Facebook data in JSON format

Usage:
1. Run the script with `py -3 guibase.py` (or `py guibase.py` if `py` is your alias for Python 3.X)
1. Find the top folder containing all of your information ("Folder")
1. Load the conversations ("Get Conversations")
1. Select a conversation, and load the data ("Load conversation data")
