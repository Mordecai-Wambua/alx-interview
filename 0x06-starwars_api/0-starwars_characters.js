#!/usr/bin/node
const request = require("request");
const movie_id = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/";

request(url + movie_id, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const output = JSON.parse(body).characters;
  const characters = output.map(
    (url) =>
      new Promise((resolve, response) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      })
  );

  Promise.all(characters)
    .then((names) => console.log(names.join("\n")))
    .catch((errors) => console.log(errors));
});
