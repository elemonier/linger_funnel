
$( document ).ready(function() {

	console.log($(location).attr('pathname'));
	setInterval('shift_about_carousel()', 2000);




});

function shift_about_carousel() {
	$('.about-carousel-on').addClass('about-carousel-off');
	$('.about-carousel-on').removeClass('about-carousel-on');
	$('.about-carousel-next').addClass('about-carousel-on');
	$('.about-carousel-next').removeClass('about-carousel-next');
	$('.about-carousel-next-next').addClass('about-carousel-next');
	$('.about-carousel-next-next').removeClass('about-carousel-next-next');
}