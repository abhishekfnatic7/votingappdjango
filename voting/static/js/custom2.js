
$(document).ready(function(){
    $('.save-button').on('select',$(this),function(){
        var a=$(this).attr('data-blogid')
        var b=$('input[class=form-check-input]:checked').val()
        $.ajax({
            url:'vid',
            method:'get',
            data:{
                a:a,b:b
            },
            dataType:'json',
            success:function(res,data){
               alert("Vote counted")
               window.location="http://127.0.0.1:8000/home"

            },
            error:function(){
                alert('errr')
            }
            

        })
    })
})

// $(document).ready(function(){
//     $('.save-button').on('click',$(this),function(){
//         var a=$(this).attr('data-blogid')
//         var b=$('input[class=form-check-input]:checked').val()
//         $.ajax({
//             url:'vid',
//             method:'get',
//             data:{
//                 a:a,b:b
//             },
//             dataType:'json',
//             success:function(res,data){
//                alert("Vote counted")
//                window.location="http://127.0.0.1:8000/home"

//             },
//             error:function(){
//                 alert('errr')
//             }
            

//         })
//     })
// })