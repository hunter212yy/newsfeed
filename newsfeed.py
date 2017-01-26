import feedparser as fp
import os

feed = fp.parse('http://www.tvn24.pl/najnowsze.xml')

#Trying to be fancy and getting that terminal window width.
_, columns = os.popen('stty size', 'r').read().split()

for index, entry in enumerate(feed.entries):
    entry_title = entry.title.rstrip()
    #The .split(...) removes one html tag they might want to smuggle there
    entry_description = str(entry.description).lstrip().split('/>', 1)[-1]
    entry_description = entry_description.lstrip().split(' - ',1)[-1].rstrip()

    print(str(index+1)+ "\n")
    print(entry_title + "\n" + "."*len(entry_title) + "\n\n" + entry_description)
    print("\n\n" + entry.link)
    print("-"*int(columns))

