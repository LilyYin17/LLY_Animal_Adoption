$(function() {
  $(".like-btn").click(function(event) {
    var petId = event.target.id;
    $.ajax({
      type: "POST",
      url: "/customer_like_pet/" + petId,
      success: function(response) {
        alert("Pet added to favorite list");
        console.log("succeeded:" + response);
      },
      error: function(response) {
        alert("Something unexpected failed. Please try again later.");
      }
    });
  });
});

// TODO:ADD ajax for this function
// $(function() {
//   $( ".like-button" ).click(function() {
//     $(this).toggleClass( "press", 1000 );
//   });
// });

$(function() {
  $(".like-button").click(function(event) {

    $(this).toggleClass( "press", 1000 );
    var petId = event.target.id;
    $.ajax({
      type: "POST",
      url: "/customer_like_pet/" + petId,
      success: function(response) {
        alert("Pet added to favorite list");
        console.log("succeeded:" + response);
      },
      error: function(response) {
        alert("Something unexpected failed. Please try again later.");
      }
    });
  });
})
