# PyPortfolio - 3/23/2020 - Andrew J Clark
#
# Skeleton File of basic single functions, Description of structure and dependencies

# Structure:
# -

# Basic Dependencies:
# os, sys, csv
# - Selenium: Webpage manipulation
# - Beautiful Soup: Parsing HTML
# - NumPy/Pandas: Data Analysis, Modeling
# - Plotly(?): Data Visualization

#
# Begin

import os, sys

import requests, bs4

# Basic Strategy & Program Structure:
# - parse webpage for financial data, import as csv File
#   - use selenium to drive google sheets importhtml call, import as csv
# - generate dictionary/list storing present filenames
#   - must support adding AND deleting filenames
# - Analytics lie in supporting queries on files(imported as dataframes)
#   - TODO?: Maintain persistent dataframe over a given program run?
