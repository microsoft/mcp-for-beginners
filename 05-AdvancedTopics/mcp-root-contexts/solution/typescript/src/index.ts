// TypeScript Example: Main Entry Point
import { demonstrateContextSession } from './contextSession.js';

/**
 * Main entry point for the TypeScript MCP Root Context demonstration
 */
async function main(): Promise<void> {
  try {
    await demonstrateContextSession();
  } catch (error: unknown) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error occurred';
    console.error('❌ Application failed:', errorMessage);
    process.exit(1);
  }
}

// Check if this module is being run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error: unknown) => {
    const errorMessage = error instanceof Error ? error.message : 'Unhandled error';
    console.error('💥 Unhandled error:', errorMessage);
    process.exit(1);
  });
}