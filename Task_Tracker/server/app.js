// server/app.js
const express = require('express');
const bodyParser = rquire('body-parser');
const cors = require(cors');

const app = express();
// Middleware
app.use(bodyParer.json());
app.use(cors());
// Route
app.use('/api/tasks', require('./routes/tasks'));
module.exports = app