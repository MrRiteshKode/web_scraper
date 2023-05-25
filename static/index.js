function webbtn() {
  $("#load").html("Wait...");
	$.post("/basic",
    {
      url: $(".url").val(),
      type: $(".options").val(),
    },
    function(data,status){
          // alert(status)
      if(data == "[]"){
        $(".code").val("No result found")
      }
      else{
        let anchor = data.split(">,").join("> , "+"\n");
        $(".code").val(anchor)
      }
      $("#load").html("");
    });
}

function webAdbtn() {
  $("#load").html("Wait..."); 
  $.post("/advance",
    {
      url: $(".url").val(),
      type: $(".options").val(),
      id: $("#idName").val(),
      class : $("#className").val(),
    },
    function(data,status){
          // alert(status)

     if(data == "[]"){
        $(".code").val("No result found")
      }
      else{
        let anchor = data.split(",").join("\n");
        $(".code").val(anchor)
      }
        $("#load").html("");
    });
}

function copy(){
    let code = $(".code").val();
    // console.log(typeof code.length)
    if(code.length > 2){
      navigator.clipboard.writeText(code);
        alert("copied");
    }
    
}
