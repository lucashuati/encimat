$(document).ready(function(){
  $('.sub').hide();
  $('.list-group a').click(function(){
    var IdPai = $(this).attr('id');
    var isHidden = $('.' + IdPai).is(':visible');
    console.log(IdPai);
    if(isHidden){
      $(this).removeClass('active');
      $('.' + IdPai).slideUp('slow');
    }else {
      $(this).addClass('active');
      $('.' + IdPai).slideDown('slow');
    }
  });
});
