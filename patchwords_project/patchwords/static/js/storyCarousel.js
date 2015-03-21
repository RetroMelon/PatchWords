//a
function onSlide (e) {
  console.log(e.relatedTarget);

  //getting the item and the parent story row.
  var item = $(e.relatedTarget);
  console.log(item.attr('paragraph-id'));
  var parentCarousel = $(item.parents('.story-row')[0]);
  console.log(parentCarousel);

  //getting rid of the old subtree
  parentCarousel.nextAll().remove();

  //fetching a new most popular subtree based on the paragraph id
  $.get( "/patchwords/getsubtree/"+item.attr('paragraph-id')+"/", function(data) {
    //putting the new carousels in the DOM
    parentCarousel.after(data);

    //setting up the carousels not to auto-cycle
    parentCarousel.nextAll().carousel({
      pause: true,
      interval: false,
    });
    //setting up the carousels to recognise clicks
    parentCarousel.nextAll().on('slid.bs.carousel', onSlide);
  });

  console.log("loaded new data for paragraph "+item.attr('paragraph-id')+"'s subtree");
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
