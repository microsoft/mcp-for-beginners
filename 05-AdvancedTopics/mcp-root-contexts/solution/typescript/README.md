````markdown
# TypeScript Root Context Example

This example demonstrates how to implement MCP root contexts in a TypeScript/Node.js application with full type safety for customer support scenarios.

## Prerequisites

- Node.js 18.0 or later
- npm 9.0 or later
- TypeScript 5.0 or later
- A modern code editor (VS Code recommended)

## Setup

1. **Navigate to the project directory:**
   ```bash
   cd solution/typescript
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure your MCP server URL:**
   Edit `src/contextSession.ts` and update the server URL:
   ```typescript
   const session = new ContextSession('YOUR_MCP_SERVER_URL');
   ```

## Running the Example

### Development Mode (recommended):
```bash
npm run dev
```

### Build and Run:
```bash
npm run build
npm start
```

### Type Checking:
```bash
npm run type-check
```

## Project Structure

```
typescript/
├── src/
│   ├── index.ts           # Main entry point
│   ├── contextSession.ts  # Core implementation
│   └── types.d.ts         # Type definitions
├── dist/                  # Compiled JavaScript (after build)
├── package.json           # Dependencies and scripts
├── tsconfig.json          # TypeScript configuration
└── README.md             # This file
```

## What the Example Demonstrates

- ✅ **Type Safety**: Full TypeScript type coverage with interfaces and generics
- 💬 **Contextual Messaging**: Strongly-typed message options and responses
- 🧠 **Insight Storage**: Type-safe metadata storage and retrieval
- 📊 **Context Monitoring**: Structured context information with type definitions
- 📝 **Smart Summaries**: Promise-based summary generation with error handling
- 🗄️ **Graceful Archival**: Type-safe archival operations with result types

## Expected Output

```
🚀 Starting TypeScript Context Session Demo

✅ Created 'Product Support - Database Performance' with ID: [context-id]

📞 Starting customer support conversation...
🤖 AI: [AI response about database performance]...
💡 Stored 2 insights
🤖 AI: [AI response about index configuration]...
💡 Stored 1 insights

📊 Context Summary: {
  name: 'Product Support - Database Performance',
  messages: 2,
  created: '[timestamp]'
}

📝 Final Summary: [AI-generated summary of the conversation]

✅ Support session completed and archived!
📦 Archive Status: archived
```

## Key TypeScript Features

### Strong Type Definitions
```typescript
interface ContextMetadata {
  [key: string]: string | number | boolean;
  createdAt?: string;
  status?: 'active' | 'archived' | 'suspended';
}

interface MessageOptions {
  temperature?: number;
  allowedTools?: string[];
  storeInsights?: boolean;
}
```

### Type-Safe Error Handling
```typescript
try {
  const result = await session.createConversationContext(name, metadata);
  return result;
} catch (error: unknown) {
  const errorMessage = error instanceof Error ? error.message : 'Unknown error';
  console.error('❌ Error:', errorMessage);
  throw error;
}
```

### Generic Method Signatures
```typescript
async createConversationContext(
  sessionName: string, 
  metadata: ContextMetadata = {}
): Promise<string>
```

### Strict Null Checks
```typescript
const response = await this.client.sendPrompt(message, {
  rootContextId: contextId,
  temperature: options.temperature ?? 0.7,  // Nullish coalescing
  allowedTools: options.allowedTools ?? []   // Default values
});
```

## API Reference

### ContextSession Class

#### Constructor
```typescript
constructor(serverUrl: string, apiKey?: string)
```

#### Methods
```typescript
createConversationContext(sessionName: string, metadata?: ContextMetadata): Promise<string>
sendMessage(contextId: string, message: string, options?: MessageOptions): Promise<MessageResponse>
getContextInfo(contextId: string): Promise<ContextInfo>
generateContextSummary(contextId: string): Promise<string>
archiveContext(contextId: string): Promise<ArchiveResult>
```

## Development Scripts

### Build Commands:
```bash
npm run build          # Compile TypeScript to JavaScript
npm run clean          # Remove compiled files
npm run type-check     # Check types without compilation
```

### Development Commands:
```bash
npm run dev            # Watch mode with automatic restart
npm start              # Run compiled JavaScript
```

### Code Quality:
```bash
npm run lint           # ESLint type checking
npm run format         # Prettier code formatting
npm test               # Run Jest tests
```

## Configuration Files

### TypeScript Configuration (`tsconfig.json`)
- **Target**: ES2022 for modern JavaScript features
- **Module System**: ESNext with Node resolution
- **Strict Mode**: Full TypeScript strict mode enabled
- **Source Maps**: Enabled for debugging
- **Declaration Files**: Generated for library usage

### Package Configuration (`package.json`)
- **Type**: Module (ESM)
- **Scripts**: Comprehensive development and build scripts
- **Dependencies**: MCP client with TypeScript support
- **Dev Dependencies**: Full TypeScript toolchain

## Type Safety Benefits

1. **Compile-time Error Detection**: Catch errors before runtime
2. **IntelliSense Support**: Rich autocomplete and documentation
3. **Refactoring Safety**: Rename and restructure with confidence
4. **Interface Contracts**: Clear API boundaries and expectations
5. **Generic Type Support**: Flexible yet type-safe implementations

## Integration Examples

### Express.js with TypeScript
```typescript
import express, { Request, Response } from 'express';
import { ContextSession, MessageOptions } from './contextSession.js';

interface MessageRequest {
  contextId: string;
  message: string;
  options?: MessageOptions;
}

const app = express();
const session = new ContextSession(process.env.MCP_SERVER_URL!);

app.post('/support/message', async (req: Request<{}, {}, MessageRequest>, res: Response) => {
  try {
    const { contextId, message, options } = req.body;
    const response = await session.sendMessage(contextId, message, options);
    res.json(response);
  } catch (error: unknown) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown error';
    res.status(500).json({ error: errorMessage });
  }
});
```

### React Hook with TypeScript
```typescript
import { useState, useCallback } from 'react';
import { ContextSession, MessageResponse } from './contextSession';

interface UseContextSessionReturn {
  sendMessage: (contextId: string, message: string) => Promise<MessageResponse>;
  loading: boolean;
  error: string | null;
}

export const useContextSession = (): UseContextSessionReturn => {
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  
  const session = new ContextSession(process.env.REACT_APP_MCP_SERVER_URL!);
  
  const sendMessage = useCallback(async (contextId: string, message: string): Promise<MessageResponse> => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await session.sendMessage(contextId, message);
      return response;
    } catch (err: unknown) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [session]);
  
  return { sendMessage, loading, error };
};
```

## Environment Configuration

Create a `.env` file for type-safe environment variables:
```bash
MCP_SERVER_URL=https://your-mcp-server.com
API_KEY=your-api-key
NODE_ENV=development
```

Add environment type definitions:
```typescript
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      MCP_SERVER_URL: string;
      API_KEY?: string;
      NODE_ENV: 'development' | 'production' | 'test';
    }
  }
}
```

## Next Steps

- Add comprehensive unit tests with Jest and TypeScript
- Implement WebSocket support with typed event handlers
- Create API documentation with TypeDoc
- Add authentication middleware with type-safe JWT handling
- Deploy to cloud platforms with proper TypeScript build pipeline
- Implement monitoring with structured logging types
- Add rate limiting with configurable type-safe options

## Troubleshooting

### Common TypeScript Issues

**Import Errors:**
```bash
# Install missing type definitions
npm install --save-dev @types/node

# Update tsconfig.json for proper module resolution
```

**Build Errors:**
```bash
# Clean and rebuild
npm run clean
npm run build

# Check for type errors
npm run type-check
```

**Runtime Errors:**
```bash
# Ensure compiled JavaScript exists
npm run build

# Check source maps for debugging
node --enable-source-maps dist/index.js
```
````