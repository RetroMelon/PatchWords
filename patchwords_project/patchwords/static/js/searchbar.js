function search() {
  window.location='/patchwords/search/?parameter='+document.getElementById('SearchInput').value+'&filter='+document.getElementById('dropdownMenu').value;
}


$('#search-button').click(search);

$('#SearchInput').keypress(function(e){
  var code = e.keyCode || e.which;
  if(code == 13) { //Enter keycode
    e.preventDefault();
    search();
  }
});
