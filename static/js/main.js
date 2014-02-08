
$( document ).ready(function() {

	console.log($(location).attr('pathname'));
	$("#myCarousel").carousel({
	         interval : 1000
	});

	$('.carousel').carousel('next');

	// window.setTimeout(function() { $(".alert").alert('close'); }, 2000);
	window.setTimeout(function() {
	    $(".alert").fadeTo(500, 0).slideUp(500, function(){
	        $(this).remove(); 
	    });
	}, 3000);

});
