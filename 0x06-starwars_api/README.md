# 0x06. Star Wars API

## Algorithm | API | JavaScript

### Concepts Needed:

- HTTP Requests in JavaScript:

Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.

- Working with APIs:

Understanding the basics of RESTful APIs and how to interact with them.
Parsing JSON data returned by APIs.

- Asynchronous Programming:

Managing asynchronous operations with callbacks, promises, and async/await syntax.
Handling API response data asynchronously.

- Command Line Arguments in Node.js:

Using the `process.argv` array to access command-line arguments passed to a Node.js script.

- Array Manipulation and Iteration:

Iterating over arrays and manipulating data structures to format and display character names.

##### By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on `Ubuntu 20.04 LTS` using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. `Rules of Standard` + `semicolons on top`. Also as reference: `AirBnB style`
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## More Info

### Install Node 10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

```bash
$ sudo npm install semistandard --global
```

### Install `request` module and use it

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name per line in the same order as the “characters” list in the /films/ endpoint
- You must use the Star wars API
- You must use the request module

```bash
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

Repo:

- GitHub repository: `alx-interview`
- Directory: `0x06-starwars_api`
- File: `0-starwars_characters.js`
