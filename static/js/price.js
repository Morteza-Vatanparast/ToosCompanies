/**
 * Created by Morteza on 8/12/2016.
 */


setInterval(function () {
    var postData = [
        {name: '_xsrf', value: xsrf_token}
    ];
    jQuery.ajax(
        {
            url: '',
            type: "post",
            data: postData,
            success: function (response) {
                if(response != false){
                    $('#DollarPrice').html(response['dollar']);
                    $('#CoinPrice').html(response['coin']);
                    $('#OilPrice').html(response['oil']);
                }
            }
        });
}, 60000);