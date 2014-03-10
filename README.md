Sloop Betty Locations
=====================
**Coverts Sloop Bety locations to an HTML table.**

Takes as input a Google Spreadsheets csv download file and exports an HTML table formatted in the Sloop Betty locations.html structure. Will export the table to the screen or saved to a file if given optional flags.

To run this program, download the `sbloc.py` file - put this somewhere you can find it, either in your home directory or on your Desktop. Unfortunately, to do this, you're going to need the command line, so go ahead and open a Terminal.

    $ cd ~/Desktop
    $ python sbloc.py -help

This will tell you how to use this program. Basically, you just give it the paths to the CSV files you'd like to convert to HTML tables. (Note that if you have spaces in your file names, you must surround it with quotes).

    $ python sbloc.py "~/Downloads/Sloop Betty Locations.csv"

This will print the HTML table to the screen; now all you have to do is copy and paste it into your HTML file!