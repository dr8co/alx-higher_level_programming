#!/usr/bin/node
/*
A script that prints all characters of a Star Wars movie:
  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
  Display one character name by line in the same order of the list “characters” in the /films/ response
*/

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    printChars(data, 0);
  }
});

function printChars (data, index) {
  request(data[index], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < data.length) {
        printChars(data, index + 1);
      }
    }
  });
}
