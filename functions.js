$.ajax({
  url: 'elements.json', // get element json
  success: function(result){
    for (var i = 0; i < result.element.length; i++){ // for element in element json
      var element = result.element[i];
      $('.' + element.symbol.toLowerCase()).append(element.symbol); // put element symbol in its div
      // console.log(element.name, element.charge); // console.log element and its charge(s)
    };
  }
});


// overlay setup
$('#element-overlay').hide();
$('#element-overlay').on('click', function(){
  $(this).hide();
});


// overlay element customization
$('.element').on('click', function(){
  // local vars
  var $this = $(this),
      $overlay = $('#element-overlay');

  var element = {};

  // setup the overlay
  $.getJSON('elements.json', function(result){
    for (var i = 0; i < result.element.length; i++){
      $json = result.element[i];
      if ($this.hasClass($json.symbol.toLowerCase())){
        element.atomicnumber = $json.atomic_number;
        element.boilingpoint = $json.boiling_point;
        element.charge = $json.charge;
        element.density = $json.charge;
        element.electronegativity = $json.electronegativity;
        element.link = $json.link;
        element.mass = $json.mass;
        element.meltingpoint = $json.melting_point;
        element.name = $json.name;
        element.symbol = $json.symbol;
        element.thermalconductivity = $json.thermal_conductivity
      }
    }
  });
  console.log(element[name]);
  // show overlay
  $overlay.show();
});
