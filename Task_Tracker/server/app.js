 server/app.j
nst express = reqire('express');
nst bodyParser = rquire('body-parser');
nst cors = require(cors');
onst app = express();
 Middleware
p.use(bodyParer.json());
p.use(cors());
 Route
p.use('/api/tasks', require('./routes/tasks'));
odule.exports = app