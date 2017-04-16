$(document).ready(function(){
    // $('.material').hide();
    $('.sub-tree ul').each(function (i) {
        if(i != 0){
            $(this).hide();
        }
    });
    $('.link-parent').click(function () {
        var show = $(this).next();
        if($(show).is(':visible')){
            $(show).slideUp('slow');
        }else {
            $(show).slideDown('slow');
        }
    });

});
