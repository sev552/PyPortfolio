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
import shelve

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
        self.ticker = ticker
        self.asset_class = asset

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
        self.ticker = ticker
        self.asset_class = asset

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

def save_urls(url_object):
    data = shelve.open('url_data')
    try:
        data[url_object.ticker]
        print(url_object.ticker + ': urls already saved!')
        data.close()
        # add ticker object
    except KeyError:
        data[url_object.ticker] = url_object
        data.close()
    return


def remove_ticker_urls():
    rem = y_or_n("Remove any saved ticker urls (y/n):")
    if rem == 1:
        remove_ticker_url()
    else:
        return
   
    
    
def remove_ticker_url():
    data = shelve.open('url_data')
    print("Present Tickers:")
    curr_list = list(data.keys())
    list_len = len(curr_list)
    print(curr_list)
    while True:
        ticker = input("Which ticker:").lower()
        try:
            data[ticker]
            confirm = y_or_n("Confirm you want to delete (y/n):")
            if confirm == 1:
                del data[ticker]
                list_len = list_len - 1
                
                cont = y_or_n("Remove more (y/n):")
                if not cont:
                    return
                elif list_len == 0:
                    print("no tickers are still stored")
                    return
                else:
                    remove_ticker_url()
                    return
            
            else:
                data.close()
                return
        except KeyError:
            print("invalid ticker")



def validate_directory():
    cwd = os.getcwd()
    if os.path.basename(cwd) != "PyPortfolio":
        raise("You're in the wrong working directory, friend")

# given a string of a questions asking for "y" and "n", returns 1 if 'y', 0 if 'n'
def y_or_n(question):
    while True:
        answer = input(question)
        if answer.lower() == "y":
            return 1
        elif answer.lower() == "n":
            return 0
        else:
            print("y or n, please")
            continue
        
def end():
    return




# todo -> get cracking on using urls to import to sheets, download as csv
        # selenium guh
