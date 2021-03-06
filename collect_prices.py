'''
Includes functions for retrieving and storing bitcoin prices
This is intended to run every hour.

'''

import requests
import sentiment

def get_btc_info():
    try:
        url = "JSON to be ADDED"
        response = requests.get(url)
        return response.text
    except:
        return None
    

def write_price_to_file(price, fname):
    if price:
        try:
            with open(fname, 'a') as f:
                f.write(price+"\n")
            print("Successfully wrote btc price")
        except:
            print("Error writing price to '" + fname + "'")
    else:
        print("No tweet to write")
  
if __name__ == "__main__":          
    p = get_btc_info()
    write_price_to_file(p, 'prices.txt')
