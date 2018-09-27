$(function(){

    $subtotal = $('.cart_list_td .col07');
    $num_show = '';
    $total = $('.settlements .col03 em');
    $delete = $('.cart_list_td .col08');


    //全选勾选
    $('.settlements .col01 input').click(function(){
        if ($(this).prop('checked') == true){
            $('.cart_list_td .col01 input').each(function(){
                $(this).prop('checked', true);
                total();
            })
        }

        if ($(this).prop('checked') == false){
            $('.cart_list_td .col01 input').each(function(){
                $(this).prop('checked', false);
                total();
            })
        }
    })

    //加按钮，小计改变，总计也改变
    $('.add').click(function(){
        getNum = /\d+/;
        id = $(this).attr('id').match(getNum)
        $num_show = $('#num'+id);
        var num = parseInt($num_show.val())+1
        show_num(num, id);
        add_2_total(id, 1)
    });

    //减按钮，小计改变，总计也改变
    $('.minus').click(function(){
            getNum = /\d+/;
            id = $(this).attr('id').match(getNum)
            $num_show = $('#num'+id);

        if ($num_show.val() > 1) {
            var num = parseInt($num_show.val())-1
            show_num(num, id);
            add_2_total(id, -1)
        }
    });
    //自定义数量
    $('.cart_list_td').delegate('.num_show', 'blur', function(){
        //获得输入的值
        num = $(this).val();
        getNum = /\d+/;
        id = $(this).attr('id').match(getNum);
        $('#subtotal'+id).text((parseInt($('#price'+id).text())*num).toFixed(2) + '元');
        $total.text($('.settlements .col03 em').text() + parseInt($('#price'+id).text())*num);
    })
    //提交购物车数据
    $('.settlements .col04').click(function(){
        var goods_list = []
        var total = $('.settlements .col03 em').text()
        var id = 0
        //如果没选中购物车中商品，则不跳转
        if ($('.settlements .col03 b').text() == '0'){
            return;
        }
        else{
            //打包选中的商品发送到后台
            $('.cart_list_td .col01 input').each(function(){
                if ($(this).prop('checked') == true){
                    id = $(this).parent().parent().attr('id');
                    //把订购的物品数据添加到列表中
                    goods = {
                        'cart_id': id,
                        'goods_id':$(this).parent().val(),
                        'amount': $('#num'+id).val(),
                        'subtotal': $('#subtotal'+id).text()
                    }
                    goods_list.push(goods);
                }
            })
            $.ajax({
               url: '/order/to_order',
               data:  {
                   'goods_list':$.toJSON(goods_list),
                   'total': $('.settlements em').text()
               },
               dataType: "json",
               type: "POST",
               traditional: true,
               success: function (responseJSON) {

                    if (responseJSON['code'] == '1'){
                        window.location.href="/order/place_order" + '?order_id=' + responseJSON['msg'];
                    }
                    else{
                        alert('亲，网络出现问题了，请重试！');
                    }
               },
               error: function() {
                   alert('亲，网络出现问题了，请重试！')
               }
           });
        }
    })


    //删除
    $delete.click(function(){
        getNum = /\d+/;
        id = $(this).attr('id').match(getNum)[0];
        $.get('/user/delete_cart', {'id': id});
        //服务器删除成功后页面上也删除
        $(this).parents('.cart_list_td').remove();
        total();
    })

    //显示总计和小计,以及商品数的变化
    show();

    //小计的变化，合计的显示,
    function show(){
        total();
        //商品勾选合计变化
        $('.cart_list_td .col01').click(function(){
            //选中的商品数量减一
            total();
        })
    };

    //计算合计
    function total(){
        var sum=0, num, counter=0, price;
        $($subtotal).each(function(){
            if ($(this).prevAll('.col01').find('input').prop('checked') == true){
                counter++;
                price = parseFloat($(this).prevAll('.col05').text());
                //找后代用find比较好
                num = $(this).prevAll('.col06').find('input').val();
                $(this).text((price*num).toFixed(2));
                sum += parseInt(parseInt($(this).text()));
            }
        })
        $($total).text(sum);
        $('.settlements .col03 b').text(counter);
    }
    //在加减按键中间显示数字
    function show_num(num, id){
        $subtotal = $('#subtotal'+id);
        $price = $('#price'+id).text();

        $num_show.val(num);
        $subtotal.text((parseInt($price)*num).toFixed(2)+'元');
    };

    //改变总和的值
    function add_2_total(id, sign){
        $price = $('#price'+id).text();
        $total.text(parseInt($total.text())+parseInt($price)*sign);
    }

})
