#!/usr/bin/python3
"""
This module has one function: number_of_subscribers(subreddit).
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries a subreddit and returns the number of subscribers.
    """
    # URL and headers to make API requests from
    url = 'https://reddit.com/r'

    # Subscriber count information
    subscriber_count = requests.get('{}/{}/about.json?subscribers'
                                    .format(url, subreddit),
                                    headers={'User-Agent': 'Mozilla/5.0'}) \
        .json().get('data').get('subscribers')

    if not subscriber_count:
        subscriber_count = 0

    return subscriber_count
