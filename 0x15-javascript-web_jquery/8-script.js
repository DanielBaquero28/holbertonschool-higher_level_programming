#!/usr/bin/node
$.get('https://swapi.co/api/films/?format=json', function(content, contentStatus) {
  const results = content.results;
  $.each(results, function(index, element) {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  });
});
