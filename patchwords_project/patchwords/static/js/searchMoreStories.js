var storiesList;
var chunksize = 5;
var lastfetched = 4;
var q = "";

function searchMoreStories() {
  lastfetched = lastfetched + chunksize;

  $.ajax({
    method: "GET",
    url: "/patchwords/searchtopstories",
    data: { start: lastfetched, end:lastfetched+chunksize, q:q }
  })
  .done(function( msg ) {
    stories_list.append(msg);
  });
}

$(function() {
  //getting the stories list
  stories_list = $('#stories-list');

  //getting the load more button and

});
