$('.plus-cart').click(function (){
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.children[1]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(data)
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.total_amount
            document.getElementById("quant").innerText = data.quantity
        }
    })
})

$('.minus-cart').click(function (){
    var id = $(this).attr('pid').toString();
    var eml = this.parentNode.children[1]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(data)
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.total_amount
            document.getElementById("quant").innerText = data.quantity
        }
    })
})

$('.remove-cart').click(function (){
    var id = $(this).attr('pid').toString();
    var eml = this
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("Code Working")
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.total_amount
            eml.parentNode.parentNode.remove()

        }
    })
})