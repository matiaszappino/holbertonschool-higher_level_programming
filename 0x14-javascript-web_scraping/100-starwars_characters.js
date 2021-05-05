#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movie = `${process.argv[2]}/`;

request(url + movie, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const characterslist = JSON.parse(body).characters;
  characterslist.forEach(character => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
