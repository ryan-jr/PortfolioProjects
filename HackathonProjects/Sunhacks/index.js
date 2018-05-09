







$.getJSON("https://api.spotify.com/v1/search?q=Beyonce*&type=artist",
         function(info){
  $span = $("span");
  $span.append("- "+"Searched for: "+info.tracks[1].name)
  
})



$.ajax({
  url:"https://api.spotify.com/v1/search?q=Beyonce*&type=artist",
  
  success: function(json){
  
  // loop

 

for(var i = 0; i<100; i++) {
   var results = "";
    results +=  "<p>Song Title: " + json.tracks[i].name + " | "+ " Artist: "+json.tracks[i].artists[0].name;
  console.log(results);
$("#track").append(results);
}//while 

  
  }
  
  
});

$(document).ready(function(){

   // jQuery methods go here...

});



