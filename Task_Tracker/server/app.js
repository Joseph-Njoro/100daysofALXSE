server/app.j
st express = reqire('express');
st bodyParser = rquire('body-parser');
st cors = require(cors');
nst app = express();
Middleware
.use(bodyParer.json());
.use(cors());
Route
.use('/api/tasks', require('./routes/tasks'));
dule.exports = app