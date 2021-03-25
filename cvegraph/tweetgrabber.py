from cvegraph.models import CVE, Time
from django.conf import settings
import tweepy as tweepy
from datetime import datetime, timedelta
import re


def init():
    try:
        CVE.objects.all().update(today_occurrence_number=0)
        CVE.objects.all().update(weekly_occurrence_number=0)
    except Exception:
        pass


def authenticate():
    # Getting private keys

    auth = tweepy.OAuthHandler(
        settings.API_KEY,
        settings.API_KEY_SECRET
    )

    auth.set_access_token(
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api


def grab_tweet():
    init()
    api = authenticate()
    print("Retrieving data...")

    # Getting date of the day to perform search
    today = datetime.today()
    date_since = today - timedelta(days=7)
    date_since = date_since.strftime('%Y-%m-%d')

    today = today.strftime('%Y-%m-%d')

    # Filter to get ride of retweets
    query = 'CVE -filter:retweets'

    if Time.objects.filter(id=1).exists():
        time_object = Time.objects.get(id=1)
        time_object.last_retrieve_time = datetime.now()
        time_object.save()

    # Finding each tweet in english to avoid some bad one
    for tweet in tweepy.Cursor(api.search, lang='en', q=query, since=date_since, tweet_mode="extended").items():
        pattern = "(?i)(CVE-(1999|2\d{3})-(\d{3,}))"
        x = re.search(pattern, tweet.full_text)
        print(x)
        print(tweet.created_at)
        created_at = tweet.created_at.strftime('%Y-%m-%d')
        if x:
            print("Je passe ici !")
            cve_id = x.group(0)
            if CVE.objects.filter(cve_id=cve_id).exists():
                obj = CVE.objects.get(cve_id=cve_id)
                if created_at == today:
                    obj.today_occurrence_number += 1
                    obj.weekly_occurrence_number += 1
                else:
                    obj.weekly_occurrence_number += 1
                obj.save()
            else:
                cve = CVE()
                cve.cve_id = cve_id
                if created_at == today:
                    cve.today_occurrence_number = 1
                    cve.weekly_occurrence_number = 1
                else:
                    cve.weekly_occurrence_number = 1
                cve.link = "https://nvd.nist.gov/vuln/detail/" + cve_id
                cve.save()

    print('END RETRIEVING')
