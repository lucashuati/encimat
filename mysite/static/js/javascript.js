$(document).ready(function(){
  // ----------------------------------------------------- MENU -----------------------------------------------------------

  $(document).on("scroll", onScroll);

  $('a[href^="#"]').on('click', function (e) {
    var menuSize = 85;
    e.preventDefault();
    $(document).off("scroll");

    $('a').each(function () {
        $(this).removeClass('active');
    })
    $(this).addClass('active');

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

  // -----------------------------------------------  Painel Principal ----------------------------------------------------
  var currentDiv;
  var title = $(".hex-column").find("h2");
  var animation_title_entrance = "zoomIn animated title-active";
  var animation_title_exit_r = "zoomOut animated title-deactive";
  var animation_title_exit = "zoomOut animated title-active";
  $(title).hover(function(){
    $(this).removeClass(animation_title_exit_r);
    $(this).addClass(animation_title_entrance);
  },function(){
    $(this).removeClass(animation_title_entrance);
    $(this).addClass(animation_title_exit);
  });
  // $(".hexagon-link").hover(function(){
  //   $(this).parent(".hex-column").find("h2").removeClass(animation_title_exit_r);
  //   $(this).parent(".hex-column").find("h2").addClass(animation_title_entrance);
  // },function(){
  //   $(this).parent(".hex-column").find("h2").removeClass(animation_title_entrance);
  //   $(this).parent(".hex-column").find("h2").addClass(animation_title_exit);
  // });
  $(".hexagon").hover(function(){
    $(this).parent(".hex-column").find("h2").removeClass(animation_title_exit_r);
    $(this).parent(".hex-column").find("h2").addClass(animation_title_entrance);
  },function(){
    $(this).parent(".hex-column").find("h2").removeClass(animation_title_entrance);
    $(this).parent(".hex-column").find("h2").addClass(animation_title_exit);
  });
  // -----------------------------------------------  Painel Equipe ----------------------------------------------------
  var altura_painel = $(".painel-equipe").height() / 2;
  var altura_icon = $(".seta").height() / 2;
  console.log("altura icon: " + altura_icon);
  console.log(altura_painel-altura_icon + "px");
  var new_margin = altura_painel-altura_icon + "px";
  $(".seta").css("margin-top",new_margin);

});

// Objeto no tamanho da tela
// var altura_tela = $(window).height() - $(".header-bg").height();/*cria variável com valor do altura da janela*/
// $(".bloco").height(altura_tela); /* aplica a variável a altura da div*/
// $( window ).resize(function() { /*quando redimensionar a janela faz a mesma coisa */
//   var altura_tela = $(window).height() - $(".header-bg").height();
//   $(".bloco").height(altura_tela);
// });

function onScroll(event){
    var scrollPos = $(document).scrollTop();
    // console.log($('.menu ul li a'));
    $('.menu ul li a').each(function () {
        var offSetMenu = 85;
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        console.log(refElement.position().top - 85);
        if (refElement.position().top - offSetMenu <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('.menu ul li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });
}
