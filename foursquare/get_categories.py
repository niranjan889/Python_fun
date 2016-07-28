'''
Created on 2016-07-27

@author: Niranjan
'''
import json
import foursquare
from api_keys import FOURSQUARE_ID4 as CLIENT_ID
from api_keys import FOURSQUARE_SECRET4 as CLIENT_SECRET

def fetch_data():
    client = foursquare.Foursquare(CLIENT_ID, CLIENT_SECRET,version='20160727')
    #Now you can access the Foursquare API!
    result = client.venues.categories()
    with open('dict_sample.json','w') as fp1:
        json.dump(result,fp1)

def read_data():
    result = json.loads(open('dict_sample.json').read())
    for cat in result['categories']:
        print cat['name']

if __name__=='__main__':
#     fetch_data()
    read_data()