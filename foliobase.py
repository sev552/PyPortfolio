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

import re

# Basic Strategy & Program Structure:
# - parse webpage for financial data, import as csv File
#   - use selenium to drive google sheets importhtml call, import as csv
# - generate dictionary/list storing present filenames
#   - must support adding AND deleting filenames
# - Analytics lie in supporting queries on files(imported as dataframes)
#   - TODO?: Maintain persistent dataframe over a given program run?


# *constants*

marketwatch = "https://www.marketwatch.com/investing"


class stock_urls:
    
    def __init__(self, ticker, asset):
        base_url = build_base_addr(ticker, asset)
        self.financial_urls = {"Income Statment": base_url +"financials",
                          "Balance Sheet": base_url + "financials/balance-sheet",
                          "Cash Flow Statement": base_url +"financials/cash-sheet"}
        
        self.profile_url = base_url + "profile"
        
        self.profile_cat = ["Valuation", 
                            "Profitability", 
                            "Efficiency", 
                            "Capital Structure", 
                            "Liquidity"]
       

class etf_urls:
    
    def __init__(self, ticker, asset):
        base_url = build_base_addr(ticker, asset)
        self.holdings_url = base_url + "holdings"
        self.holdings_cat = ["Investment Information",
                             "Detailed Information",
                             "Performance"]
        
        self.profile_url = base_url +"profile"
        self.profile_cat = ["Investment Information",
                            "Detailed Information",
                            "Performance"]


# Functions 

# Given ticker, returns object holding relevant urls to feed importing functions
def build_base_addr(ticker, asset_type):
    ticker_regex = re.compile(r'\d+')
    if ticker_regex.findall(ticker) != []:
        print('there are no numbers in tickers: terminating')
        return
    ticker = ticker.lower()
    
    while True:
        if asset_type.lower() not in ("stock", "fund"):
            print('We\'re only doing stocks and funds right now')
        else:
            if asset_type.lower() == "stock":
                asset_type = "stock"
            asset_type = "fund"
            break
    
    
    base_url = marketwatch + "/" + asset_type + "/" + ticker + "/"
    
    return base_url


def get_urls(ticker, asset_class):
    urls = None
    if asset_class.lower() == "stock":
        urls = stock_urls(ticker, asset_class)
    else:
        urls = etf_urls(ticker, asset_class)
    return urls


# todo -> get cracking on using urls to import to sheets, download as csv
    
    
    
    
    
    
    
    