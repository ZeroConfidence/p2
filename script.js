const body = document.querySelector("body");
const toggle = document.querySelector("#toggle");
const sunIcon = document.querySelector(".toggle .bxs-sun");
const moonIcon = document.querySelector(".toggle .bx-moon");

toggle.addEventListener("change", () => {
    
    body.classList.toggle("dark");
    sunIcon.className = sunIcon.className == "bx bxs-sun" ? "bx bx-sun" : "bx bxs-sun";
    moonIcon.className = moonIcon.className == "bx bxs-moon" ? "bx bx-moon" : "bx bxs-moon";

});

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
  var $nulledCanvas = $('.nulled canvas');
  var $messageCanvas = $('.message canvas');

  var originalContext = $originalCanvas[0].getContext("2d");
  var nulledContext = $nulledCanvas[0].getContext("2d");
  var messageContext = $messageCanvas[0].getContext("2d");

  var width = $originalCanvas[0].width;
  var height = $originalCanvas[0].height;

  // Check if the image is big enough to hide the message
  if ((text.length * 8) > (width * height * 3)) {
    $(".error")
      .text("Text too long for chosen image....")
      .fadeIn();

    return;
  }

  $nulledCanvas.prop({
    'width': width,
    'height': height
  });

  $messageCanvas.prop({
    'width': width,
    'height': height
  });
  // Normalize the original image and draw it
  var original = originalContext.getImageData(0, 0, width, height);
  var pixel = original.data;
  for (var i = 0, n = pixel.length; i < n; i += 4) {
    for (var offset =0; offset < 3; offset ++) {
      if(pixel[i + offset] %2 != 0) {
        pixel[i + offset]--;
      }
    }
  }
  nulledContext.putImageData(original, 0, 0);

  // Convert the message to a binary string
  var binaryMessage = "";
  for (i = 0; i < text.length; i++) {
    var binaryChar = text[i].charCodeAt(0).toString(2);

    // Pad with 0 until the binaryChar has a lenght of 8 (1 Byte)
    while(binaryChar.length < 8) {
      binaryChar = "0" + binaryChar;
    }

    binaryMessage += binaryChar;
  }
  $('.binary textarea').text(binaryMessage);

  // Apply the binary string to the image and draw it
  var message = nulledContext.getImageData(0, 0, width, height);
  pixel = message.data;
  counter = 0;
  for (var i = 0, n = pixel.length; i < n; i += 4) {
    for (var offset =0; offset < 3; offset ++) {
      if (counter < binaryMessage.length) {
        pixel[i + offset] += parseInt(binaryMessage[counter]);
        counter++;
      }
      else {
        break;
      }
    }
  }
  messageContext.putImageData(message, 0, 0);

  $(".binary").fadeIn();
  $(".images .nulled").fadeIn();
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
    img.src = `https://cs-23-sw-2-08.p2datsw.cs.aau.dk/Stockphotos/${selectedOption}.png`; // replace example.com with your image URL

    $(".loading").fadeIn();
  }
}

function decodeMessage() {
  var $originalCanvas = $('.decode canvas');
  var originalContext = $originalCanvas[0].getContext("2d");

  var original = originalContext.getImageData(0, 0, $originalCanvas.width(), $originalCanvas.height());
  var binaryMessage = "";
  var pixel = original.data;
  for (var i = 0, n = pixel.length; i < n; i += 4) {
    for (var offset =0; offset < 3; offset ++) {
      var value = 0;
      if(pixel[i + offset] %2 != 0) {
        value = 1;
      }

      binaryMessage += value;
    }
  }

  var output = "";
  for (var i = 0; i < binaryMessage.length; i += 8) {
    var c = 0;
    for (var j = 0; j < 8; j++) {
      c <<= 1;
      c |= parseInt(binaryMessage[i + j]);
    }

    output += String.fromCharCode(c);
  }

  $('.binary-decode textarea').text(output);
  $('.binary-decode').fadeIn();
};

