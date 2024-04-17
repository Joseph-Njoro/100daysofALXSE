/ server/server.j
onst app = require('./app');
onst PORT = process.env.PORT || 5000;
pp.listen(PORT, () => 
 console.log(`Server is running on port ${PORT}`)