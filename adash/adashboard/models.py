from django.db import models

# Create your models here.
class Tweet(models.Model):
  status_id = models.CharField(max_length=30)
  status_text = models.CharField(max_length=140)
  favorite_count = models.IntegerField()
  user_id = models.CharField(max_length=30)
  user_screen_name = models.CharField(max_length=30)
  user_name = models.CharField(max_length=30)
  user_profile_image_url = models.CharField(max_length=256)

  # TODO: need a created/last_updated stamps

  @classmethod
  def create(cls, tweet_hash):
    tweet = cls(status_id=tweet_hash['id'],
                status_text=tweet_hash['text'],
                favorite_count=tweet_hash['favoriteCount'],
                user_id=tweet_hash['userId'],
                user_screen_name=tweet_hash['userScreenName'],
                user_name=tweet_hash['userName'],
                user_profile_image_url=tweet_hash['userProfileImageUrl'])
    tweet.save()
    return tweet

  def to_hash(self):
    return {'id': "%s" % self.status_id,
            'text': self.status_text,
            'favoriteCount': self.favorite_count,
            'userId': "%s" % self.user_id,
            'userScreenName': self.user_screen_name,
            'userName': self.user_name,
            'userProfileImageUrl': self.user_profile_image_url}

