import os, sys
import importlib
import foliobase as fb

path = 'C:\\Users\\ajste\\OneDrive\\Documents\\GitHub\\PyPortfolio' # can't make it public with that...
os.chdir( path )



def main():
    if (len(sys.argv) < 3) | (len(sys.argv) > 3):
        print("Invalid call")
        print("Usage: pyportfolio.py ticker_name asset_class")
        return
    
    if sys.argv[2].lower() not in ["stock", "fund"]:
        print("Given invalid asset class")
        print("Usage: stock OR fund (ETF)")
    ticker = sys.argv[1]
    asset_class = sys.argv[2]
    
    urls = fb.get_urls(ticker, asset_class)
    return 0

main()