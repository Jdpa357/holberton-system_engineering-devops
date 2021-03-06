#!/usr/bin/python3
"""
This module has one function: top_ten(subreddit).
"""
import requests
import sys


def top_ten(subreddit):
    data = ""
    if type(subreddit) is not str:
        data = "None\n"
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'chrome:cybernuki/0.1.0'}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            data = "None\n"
        else:
            data_json = res.json().get("data").get("children")
            for i in range(10):
                data_title = data_json[i].get("data").get("title")
                data += "{}\n".format(data_title)
    print(data, end="")
