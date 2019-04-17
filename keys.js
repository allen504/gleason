document.onkeyup = function(e) {
  if (e.which == 39) {
    document.getElementById("next").click();
  }
  if (e.which == 37) {
    document.getElementById("previous").click();
  }
  if (e.which == 49) {
    document.getElementById("one").click();
  }
  if (e.which == 50) {
    document.getElementById("two").click();
  }
  if (e.which == 51) {
    document.getElementById("three").click();
  }
  if (e.which == 52) {
    document.getElementById("four").click();
  }
  if (e.which == 53) {
    document.getElementById("five").click();
  }
};