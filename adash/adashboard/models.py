from django.db import models

# Create your models here.
class Tweet(models.Model):
  status_twitterid = models.CharField(max_length=30)
  status_text = models.CharField(max_length=140)
  favorite_count = models.IntegerField()
  user_twitterid = models.CharField(max_length=30)
  user_screen_name = models.CharField(max_length=30)
  user_name = models.CharField(max_length=30)
  user_profile_image_url = models.CharField(max_length=256)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  @classmethod
  def create(cls, tweet_from_twitter):
    tweet = cls(status_twitterid=tweet_from_twitter.id,
                status_text=tweet_from_twitter.id,
                favorite_count=tweet_from_twitter.favorite_count,
                user_twitterid=tweet_from_twitter.user.id,
                user_screen_name=tweet_from_twitter.user.screen_name,
                user_name=tweet_from_twitter.user.name,
                user_profile_image_url=tweet_from_twitter.user.profile_image_url)
    tweet.save()
    return tweet

  @classmethod
  def create_or_update(cls, tweet_from_twitter):
    try:
      tweet = Tweet.objects.get(status_twitterid=tweet_from_twitter.id)
      tweet.favorite_count = tweet_from_twitter['favoriteCount']
      tweet.save()
      return tweet
    except Tweet.DoesNotExist:
      return Tweet.create(tweet_from_twitter)

  def to_hash(self):
    return {'id': "%s" % self.status_twitterid,
            'text': self.status_text,
            'favoriteCount': self.favorite_count,
            'userId': "%s" % self.user_twitterid,
            'userScreenName': self.user_screen_name,
            'userName': self.user_name,
            'userProfileImageUrl': self.user_profile_image_url}

class Configuration(models.Model):
  name = models.CharField(max_length=30)
  value = models.CharField(max_length=256)
  updated = models.DateTimeField(auto_now=True)
