
$( document ).ready(function() {

	console.log($(location).attr('pathname'));
	$("#myCarousel").carousel({
	         interval : 1000
	});

	$('.carousel').carousel('next');


});
