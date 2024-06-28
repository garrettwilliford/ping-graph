# ping-graph
plotext graph in python displaying basic network information

When using my computer, I usually find myself running a ping command(ping 8.8.8.8) on one of my screens.
I do this since I always have a vpn on, and sometimes they can be a little spotty depending on the country of origin.
I wanted a way to display basic network information with a little more flair.

Requirements
-----------------------------------------
- python: version 3
- python pandas
- python json


this was run on a linux machine, so when running on windows you need to change the os.system commands from
- os.system('clear')
  to
- os.system('clr')
