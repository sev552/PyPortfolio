import sys, shelve
import foliobase as fb



def main():
    # basic check that function is called with appropriate number of args
    if (len(sys.argv) < 3) | (len(sys.argv) > 3):
        print("Invalid call")
        print("Usage: pyportfolio.py ticker_name asset_class")
        return
    
    # check that asset class argument is valid 
    if sys.argv[2].lower() not in ["stock", "fund"]:
        print("Given invalid asset class")
        print("Usage: stock OR fund (ETF)")
    
    # ensure client is in the right directory
    fb.validate_directory()
    
    ticker = sys.argv[1]
    asset_class = sys.argv[2]
    
    urls = fb.get_urls(ticker, asset_class)
    fb.save_urls(urls)
    fb.remove_ticker_urls()
    
    return 0

main()