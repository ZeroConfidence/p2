const body = document.querySelector("body");
const toggle = document.querySelector("#toggle");
const sunIcon = document.querySelector(".toggle .bxs-sun");
const moonIcon = document.querySelector(".toggle .bx-moon");

var blob
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
  var file = document.querySelector("input[name=Base_File]").files[0];

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
const enurl = 'http://127.0.0.1:5000/api/Master_Encrypt';
const deurl = 'http://127.0.0.1:5000/api/Master_Decrypt';
const form = document.querySelector('#encodeform');
const encode_butt = form.querySelector('button[type="submit"]');

encode_butt.addEventListener('click',(event)=>{
  event.preventDefault();

  const formdata = new FormData(form);
  const canvas = document.querySelector('canvas[name = "message"]')  

 
  fetch(enurl,{
    method:'POST',
    body:formdata
    }
    
   )
    .then(response => response.blob())
    .then(Website_Package_Py =>{
    const returned_image = new Image();
    returned_image.src = URL.createObjectURL(Website_Package_Py)
    
    returned_image.onload =()=>
    {
      canvas.width =returned_image.width;
      canvas.height =returned_image.height;
      const ctx = canvas.getContext('2d')
      ctx.drawImage(returned_image,0,0)
    }
    
  
   }
  ).catch(error => 
  {console.error(error);});
   $(".images .message").fadeIn();
})

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


const Decodeform = document.querySelector('#decodeform');
const decode_butt = Decodeform.querySelector('[type="submit"]');

decode_butt.addEventListener('click',(event)=>{
  event.preventDefault();

  const formdata1 = new FormData(decodeform);
  

   fetch(deurl,{
    method:'post',
    body:formdata1//medium is premium 
    }
    
  )
.then(response => response.json())
.then(output => 
{
  
  $('.binary-decode textarea').text(output);
  $('.binary-decode').fadeIn();
  
})
})

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
blob = new Blob([binary_image_returned_data],{type:'image/png'});
var url_image = URL.createObjectURL(blob);
var image_returned = new Image();
image_returned.src = url_image;
document.body.appendChild(image_returned);
return image_returned;
}