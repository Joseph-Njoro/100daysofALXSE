/ server/server.j
onst app = require('./app');
onst PORT = process.env.PORT || 5000;
app.listen(PORT, () => 
  console.log(`Server is running on port ${PORT}`)