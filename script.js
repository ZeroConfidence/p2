const body = document.querySelector("body");
const toggle = document.querySelector("#toggle");
const sunIcon = document.querySelector(".toggle .bxs-sun");
const moonIcon = document.querySelector(".toggle .bx-moon");

toggle.addEventListener("change", () => {
    dark_enabled = body.classList.toggle("dark");
    sunIcon.className = sunIcon.className == "bx bxs-sun" ? "bx bx-sun" : "bx bxs-sun";
    moonIcon.className = moonIcon.className == "bx bxs-moon" ? "bx bx-moon" : "bx bxs-moon";

    localStorage.setItem("dark_enabled", dark_enabled ? "ye" : "ne");

});


if ( (localStorage.getItem("dark_enabled") || "ne") == "ne") {
  dark_enabled = true;
  dark_enabled = body.classList.toggle("dark");
  localStorage.setItem("dark_enabled", dark_enabled ? "ye" : "ne");

}






$('button.encode, button.decode').click(function(event) {
  event.preventDefault();
});

function previewDecodeImage() {
  var file = document.querySelector('input[name=decodeFile]').files[0];

  previewImage(file, ".decode canvas", function() {
    $(".decode").fadeIn();
  });
}

function previewEncodeImage() {
  var file = document.querySelector("input[name=baseFile]").files[0];

  $(".images .nulled").hide();
  $(".images .message").hide();

  previewImage(file, ".original canvas", function() {
    $(".images .original").fadeIn();
    $(".images").fadeIn();
  });
}

function previewImage(file, canvasSelector, callback) {
  var reader = new FileReader();
  var image = new Image;
  var $canvas = $(canvasSelector);
  var context = $canvas[0].getContext('2d');

  if (file) {
    reader.readAsDataURL(file);
  }

  reader.onloadend = function () {
    image.src = URL.createObjectURL(file);

    image.onload = function() {
      $canvas.prop({
        'width': image.width,
        'height': image.height
      });

      context.drawImage(image, 0, 0);

      callback();
    }
  }
}

function encodeMessage() {
  $(".error").hide();
  $(".binary").hide();

  var text = $("textarea.message").val();

  var $originalCanvas = $('.original canvas');
 
  var $messageCanvas = $('.message canvas');

  var originalContext = $originalCanvas[0].getContext("2d");
 
  var messageContext = $messageCanvas[0].getContext("2d");
  var finalimage

  var width = $originalCanvas[0].width;
  var height = $originalCanvas[0].height;

  var image = $originalCanvas.image;
 
  var b64_image_to_py = image_to_b64(image)

  const User_uploaded_encrypt = {
    b64_image_to_py:b64_image_to_py,
    key:1,
    msg:text,
    stock_num:0,
   }

  $messageCanvas.prop({
    'width': width,
    'height': height
  });
  // Normalize the origiFnal image and draw it
  var original = originalContext.getImageData(0, 0, width, height);
  
  fetch('http://loaclhost:5000/Master_Encrypt',{
    method:'post',
    headers:{'content-type':'application/json'},
    body:JSON.stringify(User_uploaded_encrypt                                         )//size matters do not question.
    }
    
  )
.then(response => {
  return response.json();
})
.then(Website_Package_Py)
{
finalimage = b64_to_image(Website_Package_Py.b64_image)
}
  


  
  messageContext.putImageData(finalimage, 0, 0);

  $(".binary").fadeIn();
  // $(".images .nulled").fadeIn();
  $(".images .message").fadeIn();
};

function previewEncodeImageFromDropdown() {
  var selectedOption = $("#Stockphotos option:selected").val();
  
  if (selectedOption) {
    var img = new Image();
    img.onload = function() {
      $(".loading").hide();

      var canvas = document.createElement('canvas');
      var ctx = canvas.getContext('2d');
      canvas.width = this.width;
      canvas.height = this.height;
      ctx.drawImage(this, 0, 0);
      canvas.toBlob(function(blob) {
        previewImage(blob, ".original canvas", function() {
          $(".images .original").fadeIn();
          $(".images").fadeIn();
        });
      });
    };
    img.onerror = function() {
      $(".loading").hide();
      $(".error")
        .text("Failed to load image")
        .fadeIn();
    };
    img.src = `../folder/Stockphotos/${selectedOption}.png`; 
    $(".loading").fadeIn();
  }
}

function decodeMessage() {
  var $originalCanvas = $('.decode canvas');
  var originalContext = $originalCanvas[0].getContext("2d");

   var Decrypt_this_image = image_to_b64(originalContext)
  const User_uploaded_decrypt = {
    b64_image_to_py:Decrypt_this_image,
    key:1,
   }

   fetch('http://localhost:5000/Master_Decrypt',{
    method:'post',
    headers:{'content-type':'application/json'},
    body:json.stringify(User_uploaded_decrypt            )//medium is premium 
    }
    
  )
.then(response => {
  return response.json();
})
.then(TempName)
{
  output = TempName.msg
}
  
  


  

  $('.binary-decode textarea').text(output);
  $('.binary-decode').fadeIn();
};

function image_to_b64(image){
  //var file = document.querySelector('input[name=baseFile]').files[0];
  var binary_image = image;
  var B64_image_to_py = btoa(binary_image);
  return B64_image_to_py;
}

function b64_to_image(B64_image_to_js){
var binary_image_returned = atob(B64_image_to_js);
var binary_image_returned_data = new Uint8Array(binary_image_returned.length);
for (let i = 0;i<binary_image_returned.length; i++){
  binary_image_returned_data[i] = binary_image_returned.charCodeAt(i);

}
var blob = new blob([binary_image_returned_data],{type:'image/png'});
var url_image = URL.createObjectURL(blob);
var image_returned = new Image();
image_returned.src = url_image;
document.body.appendChild(image_returned);
return image_returned;
}