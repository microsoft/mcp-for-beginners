import './tools/index.js';
// Log to stderr: stdout carries the JSON-RPC messages of the stdio transport
console.error("Registering tools...");
import {start} from './server.js';

start();

process.on('SIGINT', () => {
  console.error('\nShutting down...');
  process.exit(0);
});
