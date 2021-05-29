(function (window) {
  SHP = {}
  SHP.consumer_number = ko.observable('');
  SHP.bill_number = ko.observable('');
  SHP.net_payable_amount = ko.observable('');

  SHP.getCookie = function (name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };


  SHP.billImageUpload = function(data,e){
    var formdata = new FormData();
    var csrftoken = SHP.getCookie('csrftoken');
    if ($("#imageAdd").val() != "") {
      bill_image = $("#imageAdd")[0].files[0]
      formdata.append("bill_image", bill_image)
    }
    $.ajax({
      method: "POST",
      url: "/appriafy/api/bill/details/get/",
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function (xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
      },
    })
    .done(function (d, textStatus, jqXHR) {
      SHP.consumer_number(d.consumer_number)
      SHP.bill_number(d.bill_number)
      SHP.net_payable_amount(d.net_payable_amount)
      alert("Image Uploaded Successfully")
      $('#tableDiv1').show()
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      console.log(jqXHR.responseText)
    })
  }

})(this);

function init() {
if (document.readyState == "interactive") {
    $('#tableDiv1').hide()
    ko.applyBindings(SHP);
}
}
document.onreadystatechange = init;