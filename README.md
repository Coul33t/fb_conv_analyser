# fb_conv_analyser

A small tool I'm currently developping, used to analyse your Facebook conversations with people. For the moment, it can output the total/per person word count, and plot a graph with these data (either per day or per month). In order to use it, you'll need:
1. Extract your data from Facebook (Settings -> General -> " Download a copy of your Facebook data. ") 
1. [this tool](https://github.com/Coul33t/fbchat-archive-parser), which parses your conversation into a CSV file (using the command `fbcap messages ./messages.htm -f csv > fb_conv.csv`)
1. Modify the path of your `fb_conv.csv` file in `DataCSV.py`
1. Run the script
