$('.showGif').click(function(e)
        {
            $( this ).hide(  );
            document.getElementById("static/images/explanationgif.gif").src="{% static "images/explanationgif.gif" %}";
            document.getElementById("static/images/explanationgif.gif").style.display='block';
            document.getElementById('help').style.display = 'none';
            document.getElementById('less').style.display = 'block';
        });

$('.hideGif').click(function()
            document.getElementById("static/images/explanationgif.gif").style.display = 'none';
            document.getElementById('help').style.display = 'block';
            document.getElementById('less').style.display = 'none'
        });

*note to self*Want to use the help + less buttons on lots of different pages
but idk hwo to javascript in an actual javascript file