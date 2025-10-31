# JavaScript Root Context Example

This example demonstrates how to implement MCP root contexts in a JavaScript/Node.js application for customer support scenarios.

## Prerequisites

- Node.js 18.0 or later
- npm 9.0 or later
- A modern code editor (VS Code recommended)

## Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd solution/javascript
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure your MCP server URL:**
   Edit `contextSession.js` and update the server URL:
   ```javascript
   const session = new ContextSession('YOUR_MCP_SERVER_URL');
   ```

## Running the Example

### Quick Start:
```bash
npm start
```

### Development Mode (with auto-restart):
```bash
npm run dev
```

### Run with Node directly:
```bash
node contextSession.js
```

## What the Example Demonstrates

- ✅ **Context Creation**: Creating conversation contexts with rich metadata
- 💬 **Contextual Messaging**: Sending messages that build on previous interactions
- 🧠 **Insight Storage**: Automatically capturing important conversation points
- 📊 **Context Monitoring**: Real-time session information and statistics
- 📝 **Smart Summaries**: AI-generated conversation summaries
- 🗄️ **Graceful Archival**: Proper cleanup with summary preservation

## Expected Output

```
🚀 Starting Context Session Demo

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
```

## Project Structure

```
javascript/
├── contextSession.js    # Main implementation file
├── package.json         # Node.js project configuration
├── README.md           # This file
└── .gitignore          # Git ignore patterns
```

## Key Features

### ContextSession Class
- **Modular Design**: Clean class-based architecture
- **Error Handling**: Comprehensive try-catch blocks
- **Async/Await**: Modern JavaScript async patterns
- **ES6 Modules**: Uses import/export syntax

### Smart Features
- **Automatic Insight Detection**: Scans conversations for important keywords
- **Metadata Enrichment**: Automatically adds timestamps and status information
- **Context Continuity**: Maintains conversation state across multiple interactions
- **Production Ready**: Includes error handling and logging

## API Reference

### ContextSession Methods

#### `createConversationContext(sessionName, metadata)`
Creates a new root context for conversation tracking.

#### `sendMessage(contextId, message, options)`
Sends a message within an existing context with optional configurations.

#### `storeConversationInsights(contextId, userMessage, aiResponse)`
Automatically extracts and stores important conversation insights.

#### `getContextInfo(contextId)`
Retrieves comprehensive context information and statistics.

#### `generateContextSummary(contextId)`
Generates an AI-powered summary of the entire conversation.

#### `archiveContext(contextId)`
Archives a completed context with final summary preservation.

## Configuration Options

### Client Configuration
```javascript
const session = new ContextSession('server-url', {
  apiKey: 'your-api-key',
  timeout: 30000,
  retries: 3
});
```

### Message Options
```javascript
await session.sendMessage(contextId, message, {
  temperature: 0.7,
  allowedTools: ['search', 'calculator'],
  storeInsights: true
});
```

## Development

### Code Formatting:
```bash
npm run format
```

### Linting:
```bash
npm run lint
```

### Testing:
```bash
npm test
```

## Integration Examples

### Express.js Integration
```javascript
import express from 'express';
import { ContextSession } from './contextSession.js';

const app = express();
const session = new ContextSession(process.env.MCP_SERVER_URL);

app.post('/support/message', async (req, res) => {
  try {
    const { contextId, message } = req.body;
    const response = await session.sendMessage(contextId, message);
    res.json(response);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

### React.js Integration
```javascript
import { ContextSession } from './contextSession.js';

const useContextSession = () => {
  const session = new ContextSession(process.env.REACT_APP_MCP_SERVER_URL);
  
  const sendMessage = async (contextId, message) => {
    return await session.sendMessage(contextId, message);
  };
  
  return { sendMessage };
};
```

## Environment Variables

Create a `.env` file for configuration:
```bash
MCP_SERVER_URL=https://your-mcp-server.com
API_KEY=your-api-key
NODE_ENV=development
```

## Next Steps

- Add unit tests with Jest or Mocha
- Implement WebSocket support for real-time updates
- Add authentication middleware
- Create a web interface with React or Vue.js
- Deploy to cloud platforms (Vercel, Netlify, AWS)
- Add monitoring and analytics
- Implement rate limiting and security measures