$(window).scroll(function () {
    var $navbar = $(".navbar");
    $navbar.offset() && ($navbar.offset().top > 50 ? $navbar.addClass("top-nav-collapse") : $navbar.removeClass("top-nav-collapse"))
});

$('#search_submit').click(function(){
    if($('#search_input').hasClass('search-input-focus') && $('#search_input').val() != ""){
        location.href = '';
    }else {
       $('#search_input').addClass('search-input-focus').focus();
    }
});

$( "body" ).click(function( e ) {
  if($(e.target).closest("#search_wrap").attr('id') != "search_wrap"){
      $('#search_input').removeClass('search-input-focus');
  }
});