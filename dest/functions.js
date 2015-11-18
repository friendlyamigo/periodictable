// grab the elements.json
$.getJSON('elements.json',  function(result){

  // setup periodic table
  for (var i = 0; i < result.element.length; i++){ // for element in element json
    var element = result.element[i];
    $('.' + element.symbol.toLowerCase()).append(element.symbol); // put element symbol in its div
    //console.log(element.name, element.charge); // console.log element and its charge(s)
  };

  // click on an element
  $('.element').on('click', function(){
    var $this = $(this);
    var active_element = getElement(result, $this);
    clearCard();
    populateInfoCard(active_element);

    $('#element-overlay').show();
  });

});


// overlay setup
$('#element-overlay').hide();
$('#element-overlay').on('click', function(){
  $(this).hide();
});


// function to get an element
function getElement(result, $this) {
  // search each element
  for (var i = 0; i < result.element.length; i++) {
    var element = result.element[i];
    // check if element matches current element
    if ($this.hasClass(element.symbol.toLowerCase())) {
      return element
      break;
    }
  }
};


// clear the info cards data
function clearCard(){
  var card = $('#element-overlay');

  card.find('.atomic-number').empty();
  card.find('.charge').empty();
  card.find('.symbol').empty();
  card.find('.name').empty();
  card.find('.mass-number').empty();
  card.find('.additonal').empty();
};


// populate the info card div
function populateInfoCard(active_element) {
  // grab info card
  var card = $('#element-overlay');

  card.find('.atomic-number').append(active_element['atomic_number']);
  card.find('.charge').append(active_element['charge']);
  card.find('.symbol').append(active_element['symbol']);
  card.find('.name').append(active_element['name']);
  card.find('.mass-number').append(active_element['mass_number']);
  // card.find('.additonal').append(active_element[]);
};
