/ server/app.j
onst express = reqire('express');
onst bodyParser = rquire('body-parser');
onst cors = require(cors');
const app = express();
/ Middleware
pp.use(bodyParer.json());
pp.use(cors());
/ Route
pp.use('/api/tasks', require('./routes/tasks'));
module.exports = app