(function (window) {
  SHP = {}
  SHP.search_term = ko.observable('');
  SHP.categoryList = ko.observableArray([]);
  SHP.pages_list = ko.observableArray([]);
  SHP.date_sort_order = ko.observable('ascending');
  SHP.no_of_date_sort = ko.observable('false');
  SHP.current_page = ko.observable(1);
  SHP.page_count = ko.observable();


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


  SHP.ticketImageUpload = function(data){

    alert('ok')
  }

})(this);

function init() {
if (document.readyState == "interactive") {
    alert(88)
    ko.applyBindings(SHP);
}
}
document.onreadystatechange = init;