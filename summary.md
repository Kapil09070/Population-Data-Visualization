# Project Summary

## About

This project is a Python program that reads city population data from a CSV file and makes sense of it. It gives a quick summary, works out how much each city has grown, and draws a couple of charts so the numbers are easier to understand at a glance.

## What it does

- Reads a CSV file with three columns: city, year, and population
- Cleans up the data by removing blank names, bad numbers, and duplicate rows
- Shows the total population, the biggest city, and the fastest-growing city
- Calculates how much each city grew, in percent, from its first year to its last
- Draws a bar chart of growth and a line chart of population over the years

## How it works

You type in the name of your CSV file, and the program loads and cleans the data. Then a simple menu lets you see the summary, check the growth with charts, or exit.

## Built with

- Python
- pandas, to read and clean the data
- matplotlib, to draw the charts

## When things go wrong

- If the file can't be opened, the program shows an error and stops
- If there's only one year of data, it tells you growth can't be worked out
- If you pick a wrong menu option, it just asks you again

## Conclusion
This was a simple way to explore population data right from the terminal. The program copes with messy input without crashing, and it shows the results both as text and as charts.