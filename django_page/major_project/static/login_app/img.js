/* To get an image from the user and display it as a background */
function inputimg1(){
const imageInput = document.querySelector("#xrayImage1");
let uploadedImage = "";

imageInput.addEventListener("change", function () {
  const file = this.files[0];

  if (file) {
    const reader = new FileReader();

    reader.addEventListener("load", () => {
      uploadedImage = reader.result;
      const imgField = document.querySelector(".imgfield1");

      if (imgField) {
        imgField.style.backgroundImage = `url(${uploadedImage})`;
        imgField.style.backgroundSize = "cover";
        imgField.style.backgroundPosition = "center";
      }
    });

    reader.readAsDataURL(file);
  } else {
    console.error("No file selected or invalid file type.");
  }
  remove1();

});

}

function inputimg2(){
const imageInput1 = document.querySelector("#xrayImage");
let uploadedImage1 = "";

imageInput1.addEventListener("change", function () {
  const file = this.files[0];

  if (file) {
    const reader = new FileReader();

    reader.addEventListener("load", () => {
      uploadedImage1 = reader.result;
      const imgField = document.querySelector(".imgfield");

      if (imgField) {
        imgField.style.backgroundImage = `url(${uploadedImage1})`;
        imgField.style.backgroundSize = "cover";
        imgField.style.backgroundPosition = "center";
      }
    });

    reader.readAsDataURL(file);
  } else {
    console.error("No file selected or invalid file type.");
  }
  remove2();

});

}

/*to remove plus icon and choose an image txt*/

function remove1(){
  var elements= document.getElementById("pic");
  elements.classList.remove("icon1"); // Remove mystyle class from DIV
  elements.classList.add("plus-icon5"); // Add newone class to DIV
} 

/*to remove plus icon and choose an image txt*/

function remove2(){
    var elements= document.getElementById("pic1");
    elements.classList.remove("icon2"); // Remove mystyle class from DIV
    elements.classList.add("plus-icon5"); // Add newone class to DIV
  } 