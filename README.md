# PJM-EIS's GATS RPS retired certificates
Currently, PJM-EIS' Generation Attribute Tracking System offers the platform to buy and sell renewable energy certificates — each represents one megawatt-hour of electricity produced. States that utilize the "PJM grid" include Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia, and the District of Columbia. 

## RPS
Many states have Renewable Portfolio Standards (RPS) on the books, which attempt to encourage the use of renewable energy. RPS programs stipulate that utilities get a certain percentage of their energy from different "clean energy" sources. Electricity generator sells their power (1 MWh of energy = 1 renewable energy certificate or REC) on the market and the price fluctuates depending on market conditions and other factors.

## RPS Retired Certificates
Analyzing data on the number of RECs retired by year and state can provide important insight into the level of subsidies various technologies are receiving. For example, in NJ, one can match up [average REC prices](https://njcleanenergy.com/files/file/rps/EY21/EY21%20RPS%20Compliance%20Results%202004%20to%202021%20Final%202022_05_17.pdf) from the BPU and can estimate the amount of subsidies received by various types of energy plants. 

## Why we  developed this script 
Currently, the GATS database is time-consuming to use. One needs to download a spreadsheet for each compliance period for each state and combine the spreadsheets -- an unnecessary process and a waste of time. Additionally, older data occasionally gets updated. 

This script produces one excel file ("RPS Retired Certificates (GATS).xlsx") that contains data on RECs retired for all states and all years. 

## How to use the script

Running the cross-platform script is straightforward. You need to have [Python 3](https://www.python.org/downloads/) and [Google Chrome](https://www.google.com/chrome/) installed on your PC. Alternatively, you can install [Visual Code Studio](https://code.visualstudio.com/) and run the script from the IDE. 

To run the script, download "[GATS.py](https://github.com/Greatest125/PJM-GATS/blob/main/GATS.py)" to your local computer and run 
`python3 GATS.py`

Then sit back and watch the magic happen! Don't touch your computer :)

Tested on Windows 10 and Google Chrome version 102 (NOT headless)

## Contact
The script was developed by the [Energy Justice Network](https://energyjustice.net). For more information and technical support, contact Leel Dias at leel [at] duck.com
