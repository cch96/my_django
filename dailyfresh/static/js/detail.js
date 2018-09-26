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
        'amount': $num_show.val(),
        'price': $price
    };

    $.get('/user/add_cart', data, function(list){
        $('#show_count').text(list.order_num);
    });
})

//提交购物车数据
$('.buy_btn').click(function(){
    var goods_list = []
    var total = $('.settlements .col03 em').text()
    id = $('#goods_id').text();
    var amount = $('.num_show').val()
    var subtotal = parseFloat($('.show_pirze em').text()) * parseInt(amount)
    goods = {
        'goods_id': id,
        'amount': $('.num_show').val(),
        'subtotal': subtotal
    }
    $.get('/order/to_order', goods, function(data){
        if (data['code'] == '1'){
            window.location.href="/order/place_order" + '?order_id=' + data['msg'];
        }
    })
})
