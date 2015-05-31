from settings import RESCUE_TIME_API_KEY

RT_URL = "https://www.rescuetime.com/anapi/"

DAILY_SUMMARY_FEED_URL = "daily_summary_feed"
ANALYTIC_DATA_URL = "data"
ALERTS_URL = "alerts"

####
# RescumeTime API Utils that is used to connect to RescueTime
####

class RescueTimeAPI(object):
    def __init__(self, api_key=RESCUE_TIME_API_KEY):
        self.API_KEY = RESCUE_TIME_API_KEY

    def get_daily_summary_feed(self, days_back=7):
        # RescueTime's Daily Summary Feed is a snapshot and does not
        # allow you to go back more than 14 days
        if days_back > 14:
            raise AttributeError("Cannot go further than 14 days")

        pass

    def store_daily_summary_feed(self):
        pass

    def get_and_store_daily_summary_feed(self):
        pass

    def get_analytic_data_feed(self):
        pass