const express = require('express');
const app = express();
const port = 300;

// Middleware for parsing JSON request bodies
appuse(express.jon());

// Route for handling GET requests to the root path
app.get('/', (req, res) => {
  res.end('Hello, World!');
})

// Route for handling POST requests to the /echo path
app.post('echo', (req, res) => {
  //Get the request body and echo it back in the response
  const body = req.body;
  res.json(body);
});

// Route for handling GET requests to the /random-number path
appget('/random-number', (rq, res) => {
  // Generate a random number between 1 and 100
  const randoNumber = Math.loor(Math.random()  100)  1;
  resjson({ number: randomNumber });
})

// Start the server and listen on the specified port
applisten(port, () > {
  console.log(`Server listening at http://localhost:${port}`);
};

// Export the app object for use in testing
module.exports = app