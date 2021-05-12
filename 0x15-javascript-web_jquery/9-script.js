$('document').ready(function get_document() {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function get_hello(hello) {
      $('DIV#hello').text(hello.hello);
    });
  });