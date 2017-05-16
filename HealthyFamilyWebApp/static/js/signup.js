/**
 * Created by user on 04/16/17.
 */

$(function(){
            $('#btnSignUp').click(function(){
                console.log("This is working so far");
                $.ajax({
                  url:'/createAccount',
                  data: $('form').serialize(),
                  type: 'POST',
                  success: function(response){
                      console.log("Account creation proceeding to backend!");
                      console.log(response);
                      window.alert("Account Creation Successful!");
                  },
                  error: function(error){
                      console.log("Account creation not successful");
                      console.log(error);
                  }
              });
            });
});
