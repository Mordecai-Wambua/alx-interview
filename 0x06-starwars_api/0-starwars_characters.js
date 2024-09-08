#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + movieId, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const output = JSON.parse(body).characters;
  const characters = output.map(
    (url) =>
      new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      })
  );

  Promise.all(characters)
    .then((names) => console.log(names.join('\n')))
    .catch((errors) => console.log(errors));
});
