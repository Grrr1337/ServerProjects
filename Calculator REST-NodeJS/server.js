
/*
In Node.js, you don't typically use a virtual environment as you would in Python. 
Instead, you use the node_modules directory to manage your project's dependencies. 
Each Node.js project can have its own node_modules folder, and you don't need a virtual environment to isolate dependencies.
*/

// to create package.json
// npm init -y
// npm install express axios
// node server.js 
// node client.js 

const express = require('express');
const app = express();
const port = 8000;

app.get('/', (req, res) => {
  res.json({ Hello: 'World' });
});

app.get('/add', (req, res) => {
  const { x, y } = req.query;
  res.json({ result: parseFloat(x) + parseFloat(y) });
});

app.get('/subtract', (req, res) => {
  const { x, y } = req.query;
  res.json({ result: parseFloat(x) - parseFloat(y) });
});

app.get('/multiply', (req, res) => {
  const { x, y } = req.query;
  res.json({ result: parseFloat(x) * parseFloat(y) });
});

app.get('/divide', (req, res) => {
  const { x, y } = req.query;
  if (parseFloat(y) !== 0) {
    res.json({ result: parseFloat(x) / parseFloat(y) });
  } else {
    res.json({ error: 'Cannot divide by zero' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

/*
> node server.js
Server running at http://localhost:8000
*/
