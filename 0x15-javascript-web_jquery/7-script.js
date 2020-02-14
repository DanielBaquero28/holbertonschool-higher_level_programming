#!/usr/bin/node
$.get('https://swapi.co/api/people/5/?format=json', function(content, textStatus) {
  $('DIV#character').text(content.name);
});
