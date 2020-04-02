# -*- coding: utf-8 -*-
# PyPortfolio - 3/23/2020 - Andrew J Clark
#
# Description of structure and dependencies

# Structure:
# -

# Basic Dependencies:
# os, sys, requests, pandas
# - Beautiful Soup: Parsing HTML
# - NumPy/Pandas: Data Analysis, Modeling
# - Plotly(?): Data Visualization

#
# Begin

import os, sys
import shelve

import requests, bs4

import re

import exceptions as exc

# Basic Strategy & Program Structure:
# - parse webpage for financial data, import as csv File
#   - use selenium to drive google sheets importhtml call, import as csv
# - generate dictionary/list storing present filenames
#   - must support adding AND deleting filenames
# - Analytics lie in supporting queries on files(imported as dataframes)
#   - TODO?: Maintain persistent dataframe over a given program run?



marketwatch = "https://www.marketwatch.com/investing"

valid_asset_types = ["stock", "fund"]

ticker_regex = re.compile(r'\d+')


class asset_info:
    
    def __init__(self, ticker, asset):
        tckr = self.validate_ticker(ticker)
        self.ticker = tckr
        
        categ = self.validate_asset_category(asset)
        self.category = categ
        
        self.validate_combo()
        
        
    # gets the ticker name
    def name(self):
        return self.ticker
    
    # gets the ticker's category    # Not necessarily true - url corrects if given 
    def cat(self):
        cat = self.category
        if cat == "fund":
            cat = "etf"
        return cat
    
    
    def validate_ticker(self, ticker):
        tries = range(0,3)
        if ticker_regex.findall(ticker) != []:
            print('there are no numbers in tickers: 3 tries left')
            for i in tries:
                ticker = input("Type ticker again: ")
                if ticker_regex.findall(ticker) == []:
                    break
                if i == 2:
                    raise(exc.TickerError)
            ticker = ticker.lower()
        return ticker
        
        # if user doesn't give valid ticker within tries, error
        raise(exc.TickerError)

    
    def validate_asset_category(self, asset):
        tries =range(0,3)
        for i in tries:
            if asset.lower() in valid_asset_types:
                print()
                break
            
            print("PyPortfolio currently only handles:")
            print(valid_asset_types)
            asset = input("type asset category again: ")
            if i == 2:
                raise(exc.AssetCategoryError)
                
        asset = asset.lower()
        return asset
    
    # constructs the url on which all specific category urls are based
    def build_base_addr(self):
        base_url = marketwatch + "/" + self.category + "/" + self.ticker + "/"
        return base_url
    
    
    # checks if a given ticker and asset category generate a valid url
    def validate_combo(self):
        url = self.build_base_addr()
        response = requests.get(url)
        if response.status_code == 405:
            print("Reached an overview page, proceed.\n")
                
        elif response.status_code == 404:
            print("Page not found, terminating run:")
            raise(exc.TickerAssetMatchError)
        elif not response.ok:
            print("Unexpected status code encountered, proceed at own risk\n")        
        
        
        
    
    
class stock_info(asset_info):
    
    def __init__(self, ticker, asset):
        super().__init__(ticker, asset)
        
        
    
    
    
    
            
            






























