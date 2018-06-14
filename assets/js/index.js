
(function($){


	$(document).ready(function() {

		/* ---------------------------------------------- /*
		 * Smooth scroll / Scroll To Top
		/* ---------------------------------------------- */

		$('a[href*=#]').bind("click", function(e){
           
			var anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top
			}, 1000);
			e.preventDefault();
		});

		$(window).scroll(function() {
			if ($(this).scrollTop() > 100) {
				$('.scroll-up').fadeIn();
			} else {
				$('.scroll-up').fadeOut();
			}
		});

       
        /* ---------------------------------------------- /*
		 * Skills
        /* ---------------------------------------------- */    
        $('.skills').waypoint(function(){
            $('.chart1').each(function(){
            $(this).easyPieChart({
                    size:140,
                    animate: 2000,
                    lineCap:'butt',
                    scaleColor: false,
                    barColor: '#03ea35',
                    trackColor: 'transparent',
                    lineWidth: 10
                });
            });

             $('.chart2').each(function(){
            $(this).easyPieChart({
                    size:140,
                    animate: 2000,
                    lineCap:'butt',
                    scaleColor: false,
                    barColor: '#0ff',
                    trackColor: 'transparent',
                    lineWidth: 10
                });
            });

              $('.chart3').each(function(){
            $(this).easyPieChart({
                    size:140,
                    animate: 2000,
                    lineCap:'butt',
                    scaleColor: false,
                    barColor: '#ff0',
                    trackColor: 'transparent',
                    lineWidth: 10
                });
            });

               $('.chart4').each(function(){
            $(this).easyPieChart({
                    size:140,
                    animate: 2000,
                    lineCap:'butt',
                    scaleColor: false,
                    barColor: '#3a427e',
                    trackColor: 'transparent',
                    lineWidth: 10
                });
            });




        },{offset:'80%'});
        
		/* ---------------------------------------------- /*
		 * WOW Animation When You Scroll
		/* ---------------------------------------------- */

		wow = new WOW({
			mobile: false
		});
		wow.init();

	});

})(jQuery);





// SCROLL SPEED
    $('a[href^="#"]').click(function(){
    //Сохраняем значение атрибута href в переменной:
    var target = $(this).attr('href');
    $('html, body').animate({scrollTop: $(target).offset().top}, 1000);
    return false;
    });