$( function() {
        $(".accordion").accordion();
        $(".slider").slider({
          animate: "slow",
          range: "min",    
          values: 5,
          max: 10,
          slide : function(event, ui) {
            $(".slider-result").text(ui.value);
          }
        });
        $(".tabs").tabs();
});