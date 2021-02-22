from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from cvegraph import tweetgrabber
from cvegraph.views import cve_chart_today


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tweetgrabber.grab_tweet, 'interval', hours=1)
    # scheduler.add_job(tweetgrabber.grab_tweet, 'interval', minutes=2)
    scheduler.start()
