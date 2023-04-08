$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 1,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    console.log("plus Clicked")
    var id = $(this).attr("pid").toString();
    //var eml = this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id: id
        },
        success: function(data){
           Element.innerText = data.quantity
           document.getElementById("amount").innerText = data.amount
           document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.minus-cart').click(function(){
    console.log("minus Clicked")
    var id = $(this).attr("pid").toString();
    //var eml = this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id: id
        },
        success: function(data){
           Element.innerText = data.quantity
           document.getElementById("amount").innerText = data.amount
           document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.remove-cart').click(function(){
    console.log("remove Clicked")
    var id = $(this).attr("pid").toString();
    var eml = this
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id: id
        },
        success: function(data){
           console.log('Delete')
           document.getElementById("amount").innerText = data.amount
           document.getElementById("totalamount").innerText = data.totalamount
           eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})








