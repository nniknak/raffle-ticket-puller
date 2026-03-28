# Raffle Ticket Puller
_These instructions assume almost no coding knowledge and the use of a Mac computer._

First, download "raffle.py"!

In order to work this script, you'll need Python on your computer: https://www.python.org/downloads/

Then, you'll need to have a folder with your exported venmo statement and this script in it.

Copy the relative path of that folder by right-clicking the folder and then holding the option key while the right-click menu is pulled up. This will reveal a menu option to "copy '[folder-name]' as Pathname"

Open the Terminal app on your computer and type "cd " and then paste the Pathname. Press enter.

Type "python3 raffle.py" and press enter.

Input what the script asks and press enter after each entry.

The script will tell you what lines it is skipping in the venmo statement, and then it will tell you the winners. There will now be a csv file in the folder which will be the list of raffle tickets (with names and contacts repeated as many times as they've donated money for).
