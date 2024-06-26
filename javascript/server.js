const express = require('express');
const app = express();
const port = 3000;

// Middleware for parsing JSON request bodies
app.use(express.json());

// Route for handling GET requests to the root path
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Route for handling POST requests to the /echo path
app.post('/echo', (req, res) => {
  // Get the request body and echo it back in the response
  const body = req.body;
  res.json(body);
});

// Route for handling GET requests to the /random-number path
app.get('/random-number', (req, res) => {
  // Generate a random number between 1 and 100
  const randomNumber = Math.floor(Math.random() * 100) + 1;
  res.json({ number: randomNumber });
});

// Start the server and listen on the specified port
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

// Export the app object for use in testing
module.exports = app;