//the javascript that makes the add below buttons work
$(document).on('click','.btn-favourite', function(e){
  var btn = $(e.target);
  var storyId = btn.attr('story-id');
  console.log(storyId)
  var glyph = btn.children('.glyphicon');

  function updateBadge(data) {
    btn.children('.badge-favourites').html(data);
  }

  //button is in liked state so we have to unlike.
  if(btn.attr('state') == 'favourited') {
    //changing button to unliked state
    btn.attr('state', 'favourite');

    glyph.removeClass('glyphicon-star');
    glyph.addClass('glyphicon-star-empty');
    btn.children('.favourite-text').text(' Favourite ');

    //requesting an unlike
    $.ajax({
      method: "GET",
      url: "/patchwords/favourite/",
      data: {story:storyId, type:'unfavourite'}
    })
    .done(updateBadge);


  }
  else { //button is in unliked state so we have to like.
    //changing button to liked state
    btn.attr('state', 'favourited');

    glyph.removeClass('glyphicon-star-empty');
    glyph.addClass('glyphicon-star');
    btn.children('.favourite-text').text(' Favourited ');

    //requesting like
    $.ajax({
      method: "GET",
      url: "/patchwords/favourite/",
      data: {story  :storyId, type:'favourite'}
    })
    .done(updateBadge);

  }

});
