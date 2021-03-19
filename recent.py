import requests
import json
import secrets

class RecentTweetAPI:
    def __init__(self,BEARER_TOKEN):
        self.BEARER_TOKEN = BEARER_TOKEN

    def get_tweet(self,keyword):
        url = f'https://api.twitter.com/2/tweets/search/recent?query={keyword}'#&expansions=geo.place_id&place.fields=geo,id'
        headers = {'Authorization': f'Bearer {self.BEARER_TOKEN}'}
        req = requests.get(url,headers=headers,stream=True)
        if req.status_code!=200:
            raise Exception(
            f'The request returned error:{req.status_code} {display_tweet(req)}'
            )
        return req
