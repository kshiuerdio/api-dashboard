(function () {
  Renderer = {
    allFavorites: function(parentDiv) {
      var self = this;
      $.ajax({
        url: '/favorites.json'
      }).success(function(data) {
        var myDiv = $('<div>');
        _.each(data, function(tweet) {
          self.renderIndividualTweet(myDiv, tweet.id);
        });
        myDiv.prependTo(parentDiv);
        $('<script src="http://platform.twitter.com/widgets.js" charset="utf-8"></script>').appendTo(parentDiv);
      });
    },

    renderIndividualTweet: function(parentDiv, tweet) {
      $.ajax({
        url: 'https://api.twitter.com/1/statuses/oembed.json?omit_script=true&id=' + tweet,
        crossDomain: true,
        dataType: 'jsonp'
      }).success(function(data) {
        $('<div>').html(data.html).prependTo(parentDiv);
      });
    }
  }
})();