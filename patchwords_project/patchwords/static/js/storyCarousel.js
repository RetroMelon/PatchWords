//a
function onSlide (e) {
  //console.log(e.relatedTarget);

  //getting the item and the parent story row.
  var item = $(e.relatedTarget);
  //console.log(item.attr('paragraph-id'));
  var parentCarousel = $(item.parents('.story-row')[0]);
  //console.log(parentCarousel);

  //getting rid of the old subtree
  parentCarousel.nextAll().remove();

  //fetching a new most popular subtree based on the paragraph id
  $.get( "/patchwords/getsubtree/"+item.attr('paragraph-id')+"/", function(data) {
    //putting the new carousels in the DOM
    parentCarousel.after(data);

    var nextstuff = parentCarousel.nextAll();

    //setting up the carousels not to auto-cycle
    //parentCarousel.nextAll()
    $('.story-row').each(function(i, val){
      $(val).carousel({
        //pause: true,
        interval: false,
      });
    });

    //setting up the carousels to recognise clicks
    parentCarousel.nextAll().on('slid.bs.carousel', onSlide);
  });

  //console.log("loaded new data for paragraph "+item.attr('paragraph-id')+"'s subtree");
}


// When the DOM is ready, run this function
$(document).ready(function() {
  //setting all carousels not to automatically transition
  $('.carousel').carousel({
    pause: true,
    interval: false,
  });

  $('.carousel').on('slid.bs.carousel', onSlide);
});


$(document).on('mouseleave','.carousel', function(){
  $(this).carousel('pause');
});

$(document).on('click','.btn-like', function(e){
  console.log(e.target);
  var btn = $(e.target);
  var glyph = btn.children('.glyphicon');
  var parentParagraphId = btn.closest('.item').attr('paragraph-id');

  function updateBadge(data) {
    $('#badge-'+parentParagraphId).html(data);
  }

  //button is in liked state so we have to unlike.
  if(btn.attr('state') == 'liked') {
      //changing button to unliked state
      btn.attr('state', 'like');

      glyph.removeClass('glyphicon-heart');
      glyph.addClass('glyphicon-heart-empty');
      btn.children('.like-text').text(' Like');

      //requesting an unlike
      $.ajax({
        method: "GET",
        url: "/patchwords/like/",
        data: {paragraph:parentParagraphId, type:'unlike'}
      })
      .done(updateBadge);


  }
  else { //button is in unliked state so we have to like.
      //changing button to liked state
      btn.attr('state', 'liked');

      glyph.removeClass('glyphicon-heart-empty');
      glyph.addClass('glyphicon-heart');
      btn.children('.like-text').text(' Liked');

      //requesting like
      $.ajax({
        method: "GET",
        url: "/patchwords/like/",
        data: {paragraph:parentParagraphId, type:'like'}
      })
      .done(updateBadge);

  }

});
