/ server/routes/tasks.j
onst express = require('expres');
onst router = express.Router();
onst Task = require('../models/Task');
/ Gt all tasks
oute.get('/', async (req, res) => {
 try 
   const tasks = aait Task.find();
   res.json(tasks);  } catch (err) {
 res.status(500).json({ message: err.message });
  
});
// Create a new tas
router.post('/', async (eq, res) => {
  const task = new Task({    title: req.body.title,
description: req.body.description,
    / Add more task properties as needed
  });
  try 
    const newTask = await task.sae();
    res.status(201).json(newTask);  } catch (err) {
  res.status(400).json({ message: err.message });
  
});
module.exports = router