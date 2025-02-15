console.log("working fine");

const moonthNames=["Jan", "Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"];

$(document).ready(function() {
    $("#commentForm").submit(function(e){
        e.preventDefault();

        let dt = new Date();
        let time = dt.getDay() + " " + moonthNames[dt.getUTCMonth()]+", "+dt.getFullYear

        $.ajax({
            data:$(this).serialize(),
    
            method: $(this).attr('method'),
    
    
            url:$(this).attr('action'),
    
            dataType: 'json',
    
            success:function(response){
                console.log('Comment Saved to DB......');


                console.log(response);
                if(response.bool == true){
                   $('#review-res').html('Review added successfully.');
                //    $('.hide-comment-form').hide();
                   $('.add-review').hide()

                   let _html = '<div class="single-comment justify-content-between d-flex mb-30">'
                        _html +='<div class="user justify-content-between d-flex">'
                        _html +='<div class="thumb text-center">'
                        _html +='<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Favatar-profil&psig=AOvVaw3XnjvREWqIdnrRD4dN6IAq&ust=1712647501301000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNDmp6GLsoUDFQAAAAAdAAAAABAE" alt="" />'
                        _html +='<a href="#" class="font-heading text-brand">'+ response.context.user +'</a>'
                        _html +='</div>'


                        _html +='<div class="desc">'
                        _html +='<div class="d-flex justify-content-between mb-10">'
                        _html +='<div class="d-flex align-items-center">'
                        _html +='<span class="font-xs text-muted">'+ time +'</span>'
                        _html +='</div>'


                        for(let i = 1 ; i <= response.context.rating; i ++ ){
                            _html += '<i class="fas fa-star text-warning"></i>'
                        }

                        _html +='</div>'
                        _html +='<p class="mb-10">'+ response.context.review +'</p>'


                        _html +='</div>'
                        _html +='</div>'
                        _html +='</div>'
                        $('.comment-list').prepend(_html)
                }
            }
        })
    })
})



$(document).ready(function (){
    $(".filter-checkbox ,#price-filter-btn").on("click", function(){
        console.log("A checkbox have bin clicked");

        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data('filter')

            // console.log("This value is:", function_value);
            // console.log("This key is:", function_key);

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter='+ filter_key + ']:checked')).map(function(element){
                return element.value
            })
        })
        console.log("Filter object is:", filter_object);
        $.ajax({
            url:'/filter-products',
            data:filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log('Trying to filter product.....');
            },
            success: function(response){
                console.log(response);
                console.log('Data filtered successfully');
                $('#filtered-product').html(response.data)
            }
        })
    })


    $("#max_price").on("blur", function(){
        let min_price = $(this).attr("min");
        let max_price = $(this).attr("max");
        let current_price = $(this).val();

        // console.log("Current price is: ", current_price);
        // console.log("Max price is: ", max_price);
        // console.log("Min price is: ", min_price);

        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){
            console.log("Price Error Occured");

            min_price =  Math.round(min_price*100)/100;
            max_price = Math.round(max_price*100)/100;

            // console.log("######################################");
            // console.log("######################################");
            // console.log("######################################");
            // console.log("######################################");
            // console.log("Max Price Is: ", max_Price);
            // console.log("Min Price Is: ", min_Price);

            alert("Price must between"+ min_price + ' and' + max_price)
            $(this).val(min_price)
            $('#range').val(min_price)

            $(this).focus()

            return false
        }
    })
})



// $(".add-to-cart-btn").on("click", function(){
//     let this_val = $(this)
//     let index = this_val.attr("data-index")

//     // let quantity = $(".product-quantity-" + index).val()
//     let product_title = $(".product-title-" + index).val()

//     let product_id = $(".product-id-"+ index).val()
//     let product_price = $(".current-product-price-"+ index).text()

//     let product_pid = $(".product-pid-"+ index).val()
//     let product_image = $(".product-image-" + index).val()
    



//     // console.log("Quantity", quantity);
//     console.log("Product id", product_id);
//     console.log("product pid",product_pid);
//     console.log("product image",product_image);
//     console.log("product title",product_title);
//     console.log("index",index);        
//     console.log("product price",product_price);
//     console.log("This val",this_val);


//     $.ajax({
//         url:'/add-to-cart',
//         data: {
//             'id':product_id,
//             'pid': product_pid,
//             'image':product_image,
//             'qty': quantity,
//             'title': product_title,
//             'price': product_price,
//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log('Adding product to Cart.....');
//         },
//         success: function(response){
//             this_val.html("Item added to Cart...")
//             console.log('ADDED product to cart...');
//             $(".cart-items-count").text(response.totalcartitems)
//         }
//     })
// })


//Add to Card function

$("#add-to-cart-btn").on("click", function(){
    let quantity = $("#product-quantity").val()
    let product_title = $(".product-title").val()
    let product_id = $(".product-id").val()
    let product_price = $("#current-product-price").text()
    let this_val = $(this)



    console.log("A", quantity);
    console.log("B", product_id);
    console.log("C",product_title);
    console.log("D",product_price);
    console.log("E",this_val);


    $.ajax({
        url:'/add-to-cart',
        data: {
            'id':product_id,
            'qty': quantity,
            'title': product_title,
            'price': product_price
        },
        dataType: 'json',
        beforeSend: function(){
            console.log('Adding product to Cart.....');
        },
        success: function(response){
            this_val.html("Item added to Cart...")
            console.log('ADDED product to cart...');
            $(".cart-items-count").text(response.totalcartitems)
        }
    })
})