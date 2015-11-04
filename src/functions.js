// for element json
$.ajax({
  url: "elements.json",
  // print ech element name to console
  success: function(result){
    for (var i in result.periodictable.element) {
      var element = result.periodictable.element[i].name;
      $('.' + element.toLowerCase()).append(result.periodictable.element[i].symbol);
    }
  }
});
