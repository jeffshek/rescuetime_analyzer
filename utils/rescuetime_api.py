from settings import RESCUE_TIME_API_KEY

import datetime
import json
import urllib
import urllib2

RT_URL = "https://www.rescuetime.com/anapi/"

DAILY_SUMMARY_FEED_PAGE = "daily_summary_feed"
ANALYTIC_DATA_PAGE = "data"
ALERTS_PAGE = "alerts"

DAILY_SUMMARY_FEED_URL = RT_URL + DAILY_SUMMARY_FEED_PAGE
ANALYTIC_DATA_URL = RT_URL + ANALYTIC_DATA_PAGE
ALERTS_URL = RT_URL + ALERTS_PAGE

####
# RescumeTime API Utils that is used to connect to RescueTime
####

class RescueTimeAPI(object):
    def __init__(self, api_key=RESCUE_TIME_API_KEY):
        self.API_KEY = RESCUE_TIME_API_KEY

    ####
    # Getters
    ####
    def _get_daily_summary_feed(self, days_back=7):
        # RescueTime's Daily Summary Feed is a snapshot and does not
        # allow you to go back more than 14 days
        if days_back > 14:
            raise AttributeError("Cannot go further than 14 days")

        params = {
            'key': self.API_KEY,
            'format': 'json',
            'restrict_begin': '2010-01-01',
            'restrict_end': '2015-05-07',
        }

        resp = requests.get(url=DAILY_SUMMARY_FEED_URL, params=params)
        json_data = resp.json()
        return json_data

    def _get_analytic_data_feed(self, days_back=7):
        return

    ####
    # User Commands
    ####
    def get_daily_summary_feed(self, days_back=7):
        return self._get_daily_summary_feed(days_back)

    def store_daily_summary_feed(self, days_back):
        pass

    def get_and_store_daily_summary_feed(self, days_back=7):
        pass

    def get_analytic_data_feed(self):
        pass

    def store_analytic_data_feed(self):
        pass