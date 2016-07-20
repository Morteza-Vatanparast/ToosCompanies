var slider_setInterval = null;
function change_icon_slider(__new_slide){
    $(".custom-carousel-indicators li.active").removeClass("active");
    $(".custom-carousel-indicators li[data-slide=" + __new_slide + "]").addClass("active");
}
function change_slide(__new_slide){
    var __x = $(".custom-slide.active");
    __x.hide().removeClass("active");
    $(".custom-slide[data-slide=" + __new_slide + "]").addClass("active").show();
}
function start(){
    slider_setInterval = setInterval(function () {
        var $slide = $(".custom-slide.active");
        var _slide = parseInt($slide.attr("data-slide"));
        var all_slide = parseInt($slide.attr("data-all-slide"));
        var new_slide = _slide + 1;
        if(new_slide > all_slide){
            new_slide = 1;
        }
        change_slide(new_slide);
        change_icon_slider(new_slide);
    }, 3000);
}
function stop(){
    clearInterval(slider_setInterval);
    slider_setInterval = null;
}
start();

$(document).on('mouseenter', '.custom-slider', function(){
    stop();
    $('.custom-carousel-control').fadeIn();
    $('.custom-carousel-indicators').fadeIn();
});
$(document).on('mouseleave', '.custom-slider', function(){
    start();
    $('.custom-carousel-control').fadeOut();
    $('.custom-carousel-indicators').fadeOut();
});
$(document).on('click', '.custom-carousel-control.left', function(){
    var $slide = $(".custom-slide.active");
    var _slide = parseInt($slide.attr("data-slide"));
    var all_slide = parseInt($slide.attr("data-all-slide"));
    var new_slide = _slide + 1;
    if(new_slide > all_slide){
        new_slide = 1;
    }
    change_slide(new_slide);
    change_icon_slider(new_slide);
});

$(document).on('click', '.custom-carousel-control.right', function(){
    var $slide = $(".custom-slide.active");
    var _slide = parseInt($slide.attr("data-slide"));
    var all_slide = parseInt($slide.attr("data-all-slide"));
    var new_slide = _slide - 1;
    if(new_slide <= 0){
        new_slide = all_slide;
    }
    change_slide(new_slide);
    change_icon_slider(new_slide);
});
$(document).on('click', '.custom-carousel-indicators li', function(){
    var elm = $(this).closest(".custom-carousel-indicators li");
    $(".custom-carousel-indicators li.active").removeClass("active");
    elm.addClass("active");
    var new_slide = elm.attr("data-slide");
    change_slide(new_slide);
});