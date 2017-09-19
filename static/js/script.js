$(document).ready(function(){

    $(document).on("scroll", onScroll);
    $(".menu ul li:first-child a").css("cssText", "color: #E6BD00 !important;");
    $('a[href^="#"]').on('click', function (e) {
        var menuSize = 75;
        e.preventDefault();
        $(document).off("scroll");
        $('.menu ul li a').each(function () {
            $(this).css("cssText", "color: white !important;");
        })
        $(this).css("cssText", "color: #E6BD00 !important;");

        var target = this.hash,
            menu = target;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top-menuSize
        }, 1000, 'swing', function () {
            window.location.hash = target;
            $(document).on("scroll", onScroll);
        });
    });

    function onScroll(event){
        var scrollPos = $(document).scrollTop();
        $('.menu ul li a').each(function () {
            var offSetMenu = 75;
            var currLink = $(this);
            var refElement = $(currLink.attr("href"));
            if (refElement.position().top - offSetMenu <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                currLink.css("cssText", "color: #E6BD00 !important;");
            }
            else{
                currLink.css("cssText", "color: white !important;");
            }
        });
    }

    // Painel
  $(".hexLink").hover(function(){
    $(this).find("h2").removeClass("visible animated fadeOutRight");
    $(this).find("h2").addClass("visible animated fadeInLeft");
  },
  function(){
    $(this).find("h2").removeClass("visible animated fadeInLeft");
    $(this).find("h2").addClass("visible animated fadeOutRight");
  });

  // Equipe
  $(function() {
       var jcarousel = $('.jcarousel');

       jcarousel
           .on('jcarousel:reload jcarousel:create', function () {
               var carousel = $(this),
                   width = carousel.innerWidth();

               if (width >= 600) {
                   width = width / 2;
               } else if (width >= 350) {
                   width = width;
               }

               carousel.jcarousel('items').css('width', Math.ceil(width) + 'px');
           })
           .jcarousel({
               wrap: 'circular'
           });

       $('.jcarousel-control-prev')
           .jcarouselControl({
               target: '-=1'
           });

       $('.jcarousel-control-next')
           .jcarouselControl({
               target: '+=1'
           });

       $('.jcarousel-pagination')
           .on('jcarouselpagination:active', 'a', function() {
               $(this).addClass('active');
           })
           .on('jcarouselpagination:inactive', 'a', function() {
               $(this).removeClass('active');
           })
           .on('click', function(e) {
               e.preventDefault();
           })
           .jcarouselPagination({
               perPage: 1,
               item: function(page) {
                   return '<a href="#' + page + '">' + page + '</a>';
               }
           });
   });
});
