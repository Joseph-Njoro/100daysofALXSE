// server/routes/tasks.j
const express = require('expres');
const router = express.Router();
const Task = require('../models/Task');
// Gt all tasks
route.get('/', async (req, res) => {
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