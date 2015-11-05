$.ajax({
  url: 'elements.json',
  success: function(result){
    for (var i = 0; i < result.element.length; i++){
      element = result.element[i];
      $('.' + element.symbol.toLowerCase()).append(element.symbol);
    }
  }
});
