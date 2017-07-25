# -*- coding: utf-8 -*-

import json
import urllib, urllib2
import traceback
import requests
from rango import key

# Add your BING_API_KEY


def run_query(search_terms):
    # Specify the base
    root_url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    #source = 'Web'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 7
    offset = 0

    mkt='zh-CN'

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    # query = "'{0}'".format(search_terms)
    # query = urllib.quote(query)
    query = search_terms
    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    # search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
    #     root_url,https://api.cognitive.microsoft.com/bing/v5.0/search[?q][&count][&offset][&mkt][&safesearch]
    #     #source,
    #     results_per_page,
    #     offset,
    #     query)
    search_url ="{0}?q={1}&count={2}&offset={3}&mkt={4}&safesearch={5}".format(
        root_url,
        query,
        results_per_page,
        offset,
        mkt,
        'Moderate'
    )

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''


    # Create a 'password manager' which handles authentication for us.
    #password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    #password_mgr.add_password(None, search_url, username, BING_API_KEY)

    # Create our results list which we'll populate.
    headers = {'Ocp-Apim-Subscription-Key':key.key}
    results = []

    try:
        # # Prepare for connecting to Bing's servers.
        # handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        # opener = urllib2.build_opener(handler)
        # urllib2.install_opener(opener)

        # Connect to the server and read the response generated.
        response = requests.get(search_url,headers=headers).text
        # print  response
        json_response = json.loads(response)
        #print json_response
        for result in json_response['webPages']['value']:
            results.append(
                    {
                    'title' : result['name'],
                    'link' : result['url'],
                    'summary': result['snippet']
                    }
            )
        # print json_response['webPages']['value'][1]['name']
        # print json_response['webPages']['value'][1]['url']
        # print json_response['webPages']['value'][1]['snippet']
        #     #
            # results.append(
            #         {
            #         'title' : result['name'],
            #         'link' : result['url'],
            #         'summary': result['snippet']
            #         }
            #
            #                )


        # a=response['_type']
        # print a
        # json_response = json.loads(response)
        # print json_response
        #print response['webPages']
        #print json_response['value']
        #print  json_response['value']


        # Loop through each page returned, populating out results list.
        # for result in json_response:
        #     results.append({
        #     'title': result['name'],
        #     'link': result['Url'],
        #     'summary': result['snippet']})
        # for result in json_response['value']['results']:
        #     results.append({
        #         'title': result['name'],
        #         'link': result['url'],
        #         'summary': result['snippet']})

    # Catch a URLError exception - something went wrong when connecting!
    except requests.ConnectionError, e:
        print "Error when querying the Bing API: ", e
        #print traceback.format_exc()

    # Return the list of results to the calling function.
    return results


if __name__ == '__main__':
    run_query("hello2")



