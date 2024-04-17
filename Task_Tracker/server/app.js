/ server/app.j
onst express = reqire('express');
onst bodyParser = rquire('body-parser');
onst cors = require(cors');
const app = express();
/ Middleware
pp.use(bodyParer.json());
p.use(cors());
 Route
p.use('/api/tasks', require('./routes/tasks'));
odule.exports = app