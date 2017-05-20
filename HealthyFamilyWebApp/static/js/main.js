/**
 * Created by Royce on 16/05/2017.
 */

// $(function(){
//     $('#btnOrder').click(function() {
//         console.log("Hello World");
//         window.alert("Hello World");
//         /*
//         $.ajax({
//                   url:'/orderwindow',
//                   data: $('form').serialize(),
//                   type: 'GET',
//                   success: function(response){
//                       window.alert("Hello World");
//                       console.log(response);
//
//                   },
//                   error: function(error){
//
//                       console.log(error);
//                   }
//         });
//         */
//     });
// });

function showOrderWindow(){
console.log("Order Window Launched");
// window.alert("Hello World");
window.open("/orderWindow", "window-name", "menubar=no,innerWidth=300,innerHeight=150,toolbar=no,location=no,screenX=400,screenY=40");
}

function showModifyOrderWindow(){
console.log("Modify Order Window Launched");
// window.alert("Hello World");
window.open("/modifyorderWindow"", "window-name", "menubar=no,innerWidth=300,innerHeight=250,toolbar=no,location=no,screenX=400,screenY=40");
}
