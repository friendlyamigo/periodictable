$.ajax({
  url: 'elements.json', // get element json
  success: function(result){
    for (var i = 0; i < result.element.length; i++){ // for element in element json
      element = result.element[i];
      $('.' + element.symbol.toLowerCase()).append(element.symbol); // put element symbol in its div
      console.log(element.name, element.charge); // console.log element and its charge(s)
    };
  }
});
