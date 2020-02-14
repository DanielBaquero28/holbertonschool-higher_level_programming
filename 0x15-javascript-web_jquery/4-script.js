#!/usr/bin/node
const $header = $('header');

$('DIV#toggle_header').click(function() {
  $header.toggleClass('green red');
});
