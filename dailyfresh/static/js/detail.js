$total = $('.total em');
$price = $('.show_pirze em').text();
$num_show = $('#num_show');

$num_show.val(1);
$('.add').click(function(){
    var num = parseInt($num_show.val())+1
    $num_show.val(num);
    $total.text((parseInt($price)*num).toFixed(2)+'元')
});

$('.minus').click(function(){
    if ($num_show.val() > 1) {
        num = parseInt($num_show.val())-1
        $num_show.val(num);
        $total.text((parseInt($price)*num).toFixed(2)+'元')
    }
})

$('#add_cart').click(function(){
    var data = {
        'goods': $('#goods_id').text(),
        'num': $num_show.val(),
        'price': $price
    };
    $.get('/user/add_cart', data, function(list){
        $('#show_count').text(list.order_num);
    });
})
