var storiesList;
var chunksize = 10;
var lastfetched = 0;
var categoryTitle = "";

function getMoreStories() {
  lastfetched = lastfetched + chunksize;
  $.ajax({
    method: "GET",
    url: "/patchwords/gettopstories",
    data: { start: lastfetched, end:lastfetched+chunksize, category:categoryTitle }
  })
  .done(function( msg ) {
    alert( "Data Saved: " + msg );
    storiesList.append(msg);
  });
}

$(function() {
  //getting the stories list
  storiesList = $('#stories-list');

  //getting the load more button and

});
