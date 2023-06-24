var $ = jQuery.noConflict();

$(document).ready(function($) {
    "use strict";

//  Isotope

    var $container = $('.portfolio-wrap');
    var $filter = $('#filter');
    // Initialize isotope

//    if (document.documentElement.clientWidth > 768) {
//    $container.isotope({
//        filter: '*',
//        layoutMode: 'fitRows',
//        animationOptions: {
//            duration: 750,
//            easing: 'linear'
//        }
//    });
//    }

    $filter.find('a').click(function () {
        var selector = $(this).attr('data-filter');
        $filter.find('a').removeClass('current');
        $(this).addClass('current');
        $container.isotope({
            filter: selector,
            animationOptions: {
                animationDuration: 750,
                easing: 'linear',
                queue: false
            }
        });
        return false;
    });

//  CounterUp

    $('.number').counterUp({
        delay: 1,
        time: 200
    });

//  Bootstrap Pills

    $('#work-pills a').click(function (e) {
        e.preventDefault();
        $(this).tab('show')
    });

//  Change <img> tags in .has-parallax into CSS background

    $('.has-parallax').each(function () {
        var imgSrc = $(this).children('.parallax-bg').attr('src');
        $(this).css('background', 'url("' + imgSrc + '") 50% 0%');
        $(this).children('.parallax-bg').remove();
    });

//  Contact Form with validation

    $('#submit').click(function(){
        $("#contactform").validate({
            submitHandler: function() {
                $.post("contact.php", $("#contactform").serialize(),  function(response) {
                    $('#form-status').html(response);
                });
                return false;
            }
        });
    });

//  Slider high on small screens

    if (document.documentElement.clientWidth < 768) {
        $('#slider').css('height', $(window).height());
    }

//  FlexSlider

    $('.flexslider').flexslider({
        slideshowSpeed: 8000,
        animationSpeed: 1000,
        directionNav: false,
        controlNav: true,

        after: function(){
            $('.slide-wrapper').removeClass('animated fadeOutUp is-visible');
            $('.slide-wrapper').addClass('animated flipInX is-visible');
        },
        before: function(){
            $('.slide-wrapper').removeClass('animated flipInX is-visible');
            $('.slide-wrapper').addClass('animated fadeOutUp is-visible');
        }

    });

    //  Center slide title

    $('#slider .slides li').each(function () {
        var slideHeight = $(this).height();
        var contentHeight = $(this).children('.slide-content').height();
        var padTop = (slideHeight / 2) - (contentHeight / 2);
        $(this).children('.slide-content').css('padding-top', padTop);
    });

    $(window).scroll(function () {

        if ($(window).scrollTop() > 1) {
            $('.navigation').addClass('header-solid');
        } else {
            $('.navigation').removeClass('header-solid');
        }

//  Parallax

        var scrollAmount = $(window).scrollTop() / 1.5;
        scrollAmount = Math.round(scrollAmount);
        $('.has-parallax').css('backgroundPosition', '50% ' + scrollAmount + 'px');
    });

//  Scroll Reveal

    if (document.documentElement.clientWidth > 768) {

    window.scrollReveal = new scrollReveal();

    }

//  Smooth Navigation Scrolling

    $('.navigation .nav a[href^="#"], a[href^="#"].roll').on('click',function (e) {
        e.preventDefault();
        var target = this.hash,
            $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 2000, 'swing', function () {
            window.location.hash = target;
        });
    });

//  Testimonial Carousel (Owl Carousel)

    $(".testimonials-carousel").owlCarousel({
        items: 1,
        autoPlay: false,
        stopOnHover: true,
        responsiveBaseWidth: ".testimonial"
    });

//  Placeholder

    $('input, textarea').placeholder();

//  Portfolio Carousel
    $(".portfolio-carousel").owlCarousel({
        items: 1,
        autoPlay: true,
        stopOnHover: true,
        responsiveBaseWidth: ".portfolio-detail-image"
    });

//  Vanilla Box

    if ($('.image-popup').length > 0) {
        $('a.image-popup').vanillabox({
            animation: 'default',
            type: 'image',
            closeButton: true,
            repositionOnScroll: true
        });
    }
    if ($('.video').length > 0) {
        $('a.video').vanillabox({
            animation: 'default',
            preferredWidth: 1100,
            type: 'iframe'
        });
    }
});


