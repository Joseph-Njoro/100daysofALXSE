/ server/app.j
onst express = reqire('express');
onst bodyParser = rquire('body-parser');
onst cors = require(cors');
const app = express();
// Middleware
app.use(bodyParer.json());
app.use(cors());
// Route
app.use('/api/tasks', require('./routes/tasks'));
module.exports = app