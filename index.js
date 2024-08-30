const express = require('express');
const app = express();
const port = 3000;

// Define a route for the Hello World response
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Start the server
app.listen(port, () => {
  console.log(`Hello World API running at http://localhost:${port}`);
});
