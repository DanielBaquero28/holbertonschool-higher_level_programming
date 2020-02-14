#!/usr/bin/node
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(content, contentStatus) {
  $('DIV#hello').text(content.hello);
});
