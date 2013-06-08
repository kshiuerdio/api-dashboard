import twitter
from adashboard.models import Tweet
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
  # TODO
  # if last updated was recent, don't get favorites
  # otherwise, get them.  return whatever we have from the database.
  api = get_api()
  user = api.GetUser(screen_name='rdioapi')
  return api.GetFavorites(user_id=user.id)

def status_to_hash(status):
  return { 'id' : "%s" % status.id,
           'text' : status.text,
           'favoriteCount' : status.favorite_count,
           'userId' : "%s" % status.user.id,
           'userScreenName' : status.user.screen_name,
           'userName' : status.user.name,
           'userProfileImageUrl' : status.user.profile_image_url }

def update_favorites(statuses):
  for status in statuses:
    try:
      tweet = Tweet.objects.get(status_id=status['id'])
      tweet.favorite_count = status['favoriteCount']
      tweet.save()
    except Tweet.DoesNotExist:
      Tweet.create(status)