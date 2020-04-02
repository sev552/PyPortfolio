# -*- coding: utf-8 -*-
# PyPortfolio - 3/23/2020 - Andrew J Clark
#
# Description of structure and dependencies

# Structure:
# -

# Basic Dependencies:
# requests, pandas, re, shelve
# - Requests: get HTML files of webpages
# - Pandas: Data importation, cleaning, analysis
# - re: regex validation
# - shelve: data storage

#
# Begin

import shelve

import requests, re
import pandas as pd

import exceptions as exc

# Basic Strategy
# - construct urls to all relevant data pages
# - get html with requests
# - read into dataframe with pandas
#
# - generate dictionary/list storing present filenames
#   - must support adding AND deleting filenames
# - Analytics lie in supporting queries on files(imported as dataframes)
#   - TODO?: Maintain persistent dataframe over a given program run?



marketwatch = "https://www.marketwatch.com/investing"

valid_asset_types = ["stock", "fund"]

ticker_regex = re.compile(r'\d+')

url_file = "url_data"

table_file = "table_data"

class asset_info:
    
    
    def __init__(self, ticker, asset):
        tckr = self.validate_ticker(ticker)
        self.ticker = tckr
        
        categ = self.validate_asset_category(asset)
        self.category = categ
        
        self.validate_combo()
        
        self.urls = {}
        self.urls["Profile"] = self.build_base_addr() + "profile/"
        
        self.data = {}
        
        
    # returns the ticker name
    def get_name(self):
        return self.ticker
    
    # returns the ticker's category    # Not necessarily true - url corrects if given wrong other type
    def get_cat(self):
        cat = self.category
        if cat == "fund":
            cat = "etf"
        return cat
    
    # Minimal check on validity of given ticker string 
    # TODO: refine regex
    def validate_ticker(self, ticker):
        tries = range(0,3)
        if ticker_regex.findall(ticker) != []:
            for i in tries:
                print('there are no numbers in tickers: ' + str(3-i) + " tries left.")
                ticker = input("Type ticker again: ")
                if ticker_regex.findall(ticker) == []:
                    break
                if i == 2:
                    raise(exc.TickerError)
            ticker = ticker.lower()
        return ticker
        
        # if user doesn't give valid ticker within # of tries, error
        raise(exc.TickerError)

    # forces choice of valid asset category - no way to know if it's correct
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
            
        response.close()
        
    # saves all the urls corresponding to a given ticker to the url shelf
    def save_urls(self):
        save_file = shelve.open(url_file)
        try:
            save_file[self.get_name()]
            print(self.get_name() + ': urls already saved!')
            save_file.close()
        # add ticker object
        except KeyError:
            save_file[self.get_name()] = self.urls
            print(self.get_name() + ": urls saved")
            save_file.close()
        return
    
    # deletes any urls saved to a given ticker in the url shelf
    def delete_urls(self):
        save_file = shelve.open(url_file)
        try:
            del save_file[self.get_name()]
            print("urls deleted")
            save_file.close()
        # urls not present
        except KeyError:
            print(self.get_name() + ": no urls present to delete")
            save_file.close()
        return
    
    
class stock_info(asset_info):
    
    def __init__(self, ticker, asset):
        super().__init__(ticker, asset)
        base_url = self.build_base_addr()
        self.urls.update ({"Income Statment": base_url +"financials/",
                          "Balance Sheet": base_url + "financials/balance-sheet/",
                          "Cash Flow Statement": base_url +"financials/cash-sheet/"})
    
        
        
        
        
        
        
class etf_info(asset_info):
    
    def __init__(self, ticker, asset):
        super().__init__(ticker, asset)
        base_url = self.build_base_addr()
        self.urls.update({"Holdings": base_url + "holdings/"})
    
    
    
            
            






























