$(document).on('click','.btn-search', function(e){
    $.ajax({
    method: "GET",
    url: "/patchwords/search/"
}