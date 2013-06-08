(function () {
  Renderer = {
    allFavorites: function(parentDiv) {
      var self = this;
      $.ajax({
        url: '/favorites.json'
      }).success(function(data) {
        var myDiv = $('<div>');
        var ajaxSelf = this;
        ajaxSelf.finish = function() {
          $('<script src="http://platform.twitter.com/widgets.js" charset="utf-8"></script>').appendTo(parentDiv);
        };
        ajaxSelf.previous = null;
        _.each(data, function(tweet) {
          if (ajaxSelf.previous) {
            var previous = ajaxSelf.previous;
            ajaxSelf.previous = function() {
              self.renderIndividualTweet(myDiv, tweet.id, previous);
            }
          } else {
            ajaxSelf.previous = function() {
              self.renderIndividualTweet(myDiv, tweet.id, ajaxSelf.finish);
            }
          }
        });
        if (ajaxSelf.previous) {
          ajaxSelf.previous();
        }
        myDiv.prependTo(parentDiv);
      });
    },

    renderIndividualTweet: function(parentDiv, tweet, callback) {
      $.ajax({
        url: 'https://api.twitter.com/1/statuses/oembed.json?omit_script=true&id=' + tweet,
        crossDomain: true,
        dataType: 'jsonp'
      }).success(function(data) {
        var tweet_div = $('<div>').html(data.html);
        tweet_div.attr('height', '100px').data('conversation', 'none');  // THIS DOES NOTHING?!
        tweet_div.prependTo(parentDiv);
        if(callback) {
          callback();
        }
      });
    }
  }
})();