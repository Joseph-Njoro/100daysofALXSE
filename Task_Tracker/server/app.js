server/app.j
st express = reqire('express');
st bodyParser = rquire('body-parser');
st cors = require(cors');
nst app = express();
Middleware
.use(bodyParer.json());
p.use(cors());
 Route
p.use('/api/tasks', require('./routes/tasks'));
odule.exports = app