(function () {
  Renderer = {
    allFavorites: function(parentDiv) {
      var self = this;
      $.ajax({
        url: '/favorites.json'
      }).success(function(data) {
        _.each(data, function(tweet) {
          var myDiv = $('<div class="tweet">');
          self.renderIndividualTweet(myDiv, tweet);
          myDiv.appendTo(parentDiv);
        });
      });
    },

    renderIndividualTweet: function(parentDiv, tweet) {
      var text = $('<div class="tweet-text">').append(tweet.text);
      var userImg = $('<img>').attr('src', tweet.userProfileImageUrl);
      var user = $('<a>').attr('href', 'http://twitter.com/' + tweet.userScreenName).append(userImg);
      var userDiv = $('<div class="tweet-user-pic">').append(user);
      var userName = $('<div class="tweet-username">').append(tweet.userName);
      text.appendTo(parentDiv);
      userDiv.appendTo(parentDiv);
      userName.appendTo(parentDiv);
    }
  }
})();