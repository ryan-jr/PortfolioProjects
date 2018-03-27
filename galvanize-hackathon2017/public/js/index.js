function displayOne(){
  $( ".canvas-content" ).html("<a-scene>"+
  "<a-sphere color='red' position='0 0 0' rotation='0 45 0 ' scale='2 1 3'></a-sphere>" +
  "<a-marker-camera preset='hiro'></a-marker-camera>" +
  "</a-scene>");
}

function displayTwo(){
  $( ".canvas-content" ).html("<a-scene>"+
    "<a-assets>" +
      "<a-asset-item id='optimerBoldFont' src='https://rawgit.com/mrdoob/three.js/dev/examples/fonts/optimer_bold.typeface.json'></a-asset-item>" +
    "</a-assets>" + 
      "<a-box src='https://i.imgur.com/mYmmbrp.jpg' position='0 0 0' rotation='0 0 0' scale='1 1 1'></a-box>" + 
  "<a-sky color='#222'></a-sky>" +
  "<a-marker-camera preset='hiro'></a-marker-camera>" +
  "</a-scene>");
}

function displayThree(){
   $( ".canvas-content" ).html("<a-scene>"+
  "<a-sphere position='0 .5 0' radius='1.25' color='blue'>" + 
      
      "<a-sphere position='   0  1  0 ' radius='1' color='green'></a-sphere>" +
      "<a-sphere position='   0  2  0' radius='.75' color='red'></a-sphere>"+
      "<a-sphere position='   0  3  0' radius='.5' color='yellow'></a-sphere>" +
      
   "</a-sphere>" + 
   "<a-marker-camera preset='hiro'></a-marker-camera>" +
  "</a-scene>");
}

function displayFour(){
  $( ".canvas-content" ).html("<a-scene>"+
  "<a-cylinder position='0 0 0' radius='0.5' height='3' src='https://i.imgur.com/mYmmbrp.jpg'>" +

    "<a-cylinder position='.25 -1 1' rotation='0 45 0' radius='0.5' height='1.5' color='red'></a-cylinder>" +
    "<a-cylinder position='-.25 0.5 1' rotation='0 45 45' radius='0.5' height='1.5' color='yellow'></a-cylinder>" +
    "<a-cylinder position='0 1 .5' radius='0.5' height='1.5' color='blue'></a-cylinder>" +

    "<a-animation attribute='position' to='0 2 0' direction='alternate' dur='2000' repeat='indefinite'></a-animation>" +

  "</a-cylinder>" +
  "<a-marker-camera preset='hiro'></a-marker-camera>" +
  "</a-scene>");
}

function displayFive(){
  $( ".canvas-content" ).html("<a-scene>"+
    "<a-box position='0 .5 0' radius='.5' color='yellow'>" +

      "<a-box position='0 0 -.5' rotation='0 45 0' radius='1.25' color='purple'></a-box>" +
      "<a-box position='0 1 .5' rotation='0 0 45' radius='2' color='pink'></a-box>" +
      "<a-box position='.5 1.5 0' rotation='45 0 0' radius='3' color='orange'></a-box>" +

    "</a-box>" +
    "<a-marker-camera preset='hiro'></a-marker-camera>" +
  "</a-scene>");
}

$(function() {
    displayThree();
});