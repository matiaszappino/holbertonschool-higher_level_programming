$.get('https://swapi-api.hbtn.io/api/films/?format=json', function get_movies(movies) {
    $('UL#list_movies').append(movies.results.map(movie => `<li>${movie.title}</li>`));
});