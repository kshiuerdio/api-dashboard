import twitter
from datetime import datetime, timedelta
from adashboard.models import Configuration, Tweet
from adash.settings import DATA_SOURCE_KEYS


def get_api():
  consumer_key = DATA_SOURCE_KEYS['twitter']['consumer_key']
  consumer_secret = DATA_SOURCE_KEYS['twitter']['consumer_secret']
  access_token = DATA_SOURCE_KEYS['twitter']['access_key']
  access_token_secret = DATA_SOURCE_KEYS['twitter']['access_secret']
  api = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token,
                    access_token_secret=access_token_secret)
  return api

def get_favorites():
  # if last updated was recent, don't get favorites
  # otherwise, get them.  return whatever we have from the database.
  twitter_last_updated = Configuration.objects.filter(name='twitter_last_updated')
  if twitter_last_updated and twitter_last_updated[0].updated.replace(tzinfo=None) > (datetime.now() - timedelta(minutes=10)):
    favorites = Tweet.objects.order_by('id', '-created')
  else:
    api = get_api()
    user = api.GetUser(screen_name='rdioapi')
    favorites = update_favorites(api.GetFavorites(user_id=user.id))
    config = Configuration(name='twitter_last_updated')
    config.save()
  return [ tweet_obj.to_hash() for tweet_obj in favorites ]

def status_to_hash(status):
  return { 'id' : "%s" % status.id,
           'text' : status.text,
           'favoriteCount' : status.favorite_count,
           'userId' : "%s" % status.user.id,
           'userScreenName' : status.user.screen_name,
           'userName' : status.user.name,
           'userProfileImageUrl' : status.user.profile_image_url }

def update_favorites(statuses):
  results = []
  for status in reversed(statuses):
    # We're almost always delivered the set of favorites from twitter in reversed order, most recent to least recent,
    # So deal with it that way.
    results.append(Tweet.create_or_update(status))
  return results