#!/usr/bin/node

const filmId = process.argv[2];
const request = require('request');

const api = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

request(api, (error, response, body) => {
  if (error) console.log(error);
  const data = JSON.parse(body);
  const chars = data.characters;

  for (let i = 0; i < chars.length; i++) {
    request(chars[i], (error, response, actors) => {
      if (error) console.log(error);
      const actor = JSON.parse(actors);
      console.log(actor.name);
    });
  }
});
