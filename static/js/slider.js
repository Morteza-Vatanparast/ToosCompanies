function change_slide(__elm){
    $(".custom-slider-small .slider-large-box").find('img').attr('src', __elm.find('img').attr('src'));
    $('.slider-small-image.active').removeClass('active');
    __elm.addClass('active');
}

$(document).on('click', '.slider-small-image', function(e){
    var elm = $(e.target).closest('.custom-slider-small .slider-small-image');
    change_slide(elm);
});

$(document).on('click', '.slider-angle-left.slider-angle', function(){
    var $slide = $(".slider-small-image.active");
    var _slide = parseInt($slide.attr("data-slide"));
    var all_slide = parseInt($slide.attr("data-all-slide"));
    var new_slide = _slide + 1;
    if(new_slide > all_slide){
        new_slide = 1;
    }
    var elm = $('.slider-small-boxes .slider-small-image[data-slide=' + new_slide + ']');
    change_slide(elm);

});

$(document).on('click', '.slider-angle-right.slider-angle', function(){
    var $slide = $(".slider-small-image.active");
    var _slide = parseInt($slide.attr("data-slide"));
    var all_slide = parseInt($slide.attr("data-all-slide"));
    var new_slide = _slide - 1;
    if(new_slide <= 0){
        new_slide = all_slide;
    }
    var elm = $('.slider-small-boxes .slider-small-image[data-slide=' + new_slide + ']');
    change_slide(elm);
});