$(".menuBtn").click(function(){
  
    $(".menuDiv").toggleClass("slideClose");
    if ($(".menuDiv").hasClass("slideClose")) {
      $(".slideDiv").animate({ left: "0px"}, 'slow');  
      $(".allDiv").animate({ left: "300px", width: '80%'}, 'slow');          
    } else { 
        $(".slideDiv").animate({ left: "-300px"}, 'slow');  
        $(".allDiv").animate({ left: "0px", width: '100%'}, 'slow');          
    }
});

$(".userBtn").click(function(){
  
    $(".dropdownDiv").toggleClass("dropdownClose");

    if ($(".dropdownDiv").hasClass("dropdownClose")) {
        $(".dropdownDiv").css("display", "block");
    } else{ 
        $(".dropdownDiv").css("display", "none");        
    }
});