const express = require('express');
const app = express();

app.use(express.json());

app.post('/hello', (req, res) => {
  res.send('Hello from the server!');
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
