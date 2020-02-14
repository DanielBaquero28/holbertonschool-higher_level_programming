#!/usr/bin/node
window.onload = function() {
  $('INPUT#btn_translate').click(function() {
    const language = $('INPUT#language_code');
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + language, function(content, contentStatus) {
      $('DIV#hello').text(content.hello);
    });
  });
};
