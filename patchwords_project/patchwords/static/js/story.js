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
    //parentCarousel.nextAll().on('slid.bs.carousel', onSlide);
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
});

$(document).on('slid.bs.carousel','.carousel', onSlide);

$(document).on('mouseleave','.carousel', function(){
  $(this).carousel('pause');
});


//the javascript that makes the like buttons work
$(document).on('click','.btn-like', function(e){
  console.log(e.target);
  var btn = $(e.target);
  var glyph = btn.children('.glyphicon');
  var parentParagraphId = btn.closest('.item').attr('paragraph-id');

  function updateBadge(data) {
    $('#badge-'+parentParagraphId).html(data);
  }

  //button is in liked state so we have to unlike.
  if(btn.attr('state') == 'Un-like') {
    //changing button to unliked state
    btn.attr('state', 'like');

    glyph.removeClass('glyphicon-heart');
    glyph.addClass('glyphicon-heart-empty');
    btn.children('.like-text').text(' Like');

    //requesting an unlike
    $.ajax({
      method: "GET",
      url: "/patchwords/like/",
      data: {paragraph:parentParagraphId, type:'Un-like'}
    })
    .done(updateBadge);


  }
  else { //button is in unliked state so we have to like.
    //changing button to liked state
    btn.attr('state', 'Un-like');

    glyph.removeClass('glyphicon-heart-empty');
    glyph.addClass('glyphicon-heart');
    btn.children('.like-text').text(' Un-like');

    //requesting like
    $.ajax({
      method: "GET",
      url: "/patchwords/like/",
      data: {paragraph:parentParagraphId, type:'like'}
    })
    .done(updateBadge);

  }

});


//the javascript that makes the add below buttons work
$(document).on('click','.btn-add', function(e){
  console.log(e.target);
  var btn = $(e.target);
  var parentStoryRow = btn.closest('.story-row');
  //var nextStoryRows = parentStoryRow.nextAll('.story-row');
  var parentParagraphId = btn.closest('.item').attr('paragraph-id');

  //removing all of the next story rows.
  parentStoryRow.nextAll().remove();
  console.log(parentParagraphId);

  //showing a form to add a paragraph.
  $.ajax({
    method: "GET",
    url: "/patchwords/newparagraph/",
    data: {parentid:parentParagraphId}
  })
  .done(function(data) {
    parentStoryRow.after(data);
  });

});

//the javascript that makes the add-submit button work
$(document).on('click','.btn-add-submit', function(e){
  console.log(e.target);
  var btn = $(e.target);
  //var aboveStoryRow = btn.closest('.story-row');
  //var nextStoryRows = parentStoryRow.nextAll('.story-row');
  var parentParagraphId = btn.prevAll('#parentid').attr('value');
  var content = $('#content').val();
  console.log(parentParagraphId + "    " + content);

  function onSubmit(data) {
    //removing this form from the DOM
    $('.new-paragraph-row').remove();

    //adding the data
    var parentStoryRow = $('#story-container').children().last();
    console.log("last");
    console.log(parentStoryRow);
    parentStoryRow.after(data);

    //getting the new story row, and sliding left to show the user's paragraph.
    var newStoryRow = parentStoryRow.next();
    newStoryRow.carousel('prev');
    newStoryRow.carousel('pause');

    //since programmatically sliding the carousel doesn't reload the story tree,
    //we need to remove the stuff that comes after it.
    newStoryRow.nextAll().remove();

    //flashing the paragraph to draw attention
    var active = newStoryRow.find('.active');
    console.log(active);
    active.css("background-color", "#FFFF99");
    active.stop().animate({backgroundColor: "white"}, 10);

    //updating all of the carousels to pause them
    $('.story-row').each(function(i, val){
      $(val).carousel({
        pause: true,
        interval: false,
      });


    });
  }

  //showing a form to add a paragraph.
  $.ajax({
    method: "GET",
    url: "/patchwords/newparagraph/",
    data: {parentid:parentParagraphId, content:content, type:'submit'}
  })
  .done(onSubmit);

});
