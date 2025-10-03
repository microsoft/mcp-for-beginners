import './tools/index.js';
console.log("Registering tools...");
import {start} from './server.js';

start();

process.on('SIGINT', () => {
  console.log('\nShutting down...');
  process.exit(0);
});
