# Python Example: Technical Support Assistant
import asyncio
from datetime import datetime
from mcp_client import McpClient, RootContextManager

class TechnicalAssistant:
    def __init__(self, server_url, api_key=None):
        self.client = McpClient(server_url=server_url, api_key=api_key)
        self.context_manager = RootContextManager(self.client)
        print("🤖 Technical Assistant initialized")

    async def create_support_session(self, session_name, user_info=None):
        """Create a personalized technical support session"""
        metadata = {
            "session_type": "technical_support",
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }
        
        # Personalize with user information
        if user_info:
            metadata.update({f"user_{k}": v for k, v in user_info.items()})
            
        # Create the support context
        context = await self.context_manager.create_root_context(session_name, metadata)
        print(f"📞 Created support session '{session_name}' (ID: {context.id})")
        return context.id

    async def send_support_message(self, context_id, message, tools=None):
        """Send a message with optional tool access"""
        options = {"root_context_id": context_id}
        
        # Add specialized tools for technical support
        if tools:
            options["allowed_tools"] = tools
        
        # Send message within the support context
        response = await self.client.send_prompt(message, options)
        
        # Track conversation progress
        await self._update_session_progress(context_id, message)
        
        return response
    
    async def _update_session_progress(self, context_id, message):
        """Update session metadata with conversation progress"""
        timestamp = datetime.now().timestamp()
        await self.context_manager.update_context_metadata(context_id, {
            f"interaction_{int(timestamp)}": message[:30] + "...",
            "last_interaction": datetime.now().isoformat(),
            "total_messages": await self._count_messages(context_id)
        })

    async def get_session_info(self, context_id):
        """Get comprehensive session information"""
        context_info = await self.context_manager.get_context_info(context_id)
        messages = await self.client.get_context_messages(context_id)
        
        return {
            "session_info": {
                "id": context_info.id,
                "name": context_info.name,
                "created": context_info.created_at,
                "status": context_info.metadata.get("status", "unknown")
            },
            "conversation": {
                "message_count": len(messages),
                "messages": messages
            }
        }
    
    async def _count_messages(self, context_id):
        """Count total messages in the session"""
        messages = await self.client.get_context_messages(context_id)
        return len(messages)

    async def end_support_session(self, context_id):
        """End support session with summary and resolution status"""
        # Generate comprehensive session summary
        summary_response = await self.client.send_prompt(
            "Please provide a technical summary of our troubleshooting session, "
            "including the problem, steps taken, and final resolution.",
            {"root_context_id": context_id}
        )
        
        # Store final session data
        final_metadata = {
            "technical_summary": summary_response.generated_text,
            "session_ended": datetime.now().isoformat(),
            "status": "resolved",
            "resolution_provided": "yes"
        }
        
        await self.context_manager.update_context_metadata(context_id, final_metadata)
        
        # Archive the completed session
        await self.context_manager.archive_context(context_id)
        
        return {
            "status": "session_completed",
            "summary": summary_response.generated_text,
            "context_id": context_id
        }

# Demonstration: Complete technical support workflow
async def demo_technical_support():
    print("🛠️  Starting Technical Support Demo\n")
    assistant = TechnicalAssistant("https://mcp-server-example.com")
    
    try:
        # 1. Create personalized support session
        context_id = await assistant.create_support_session(
            "Cloud Auto-Scaling Support",
            {
                "name": "Alex Chen", 
                "technical_level": "advanced", 
                "product": "Cloud Platform",
                "department": "DevOps"
            }
        )
        
        print("\n🔧 Starting troubleshooting...")
        
        # 2. Initial problem report
        response1 = await assistant.send_support_message(
            context_id, 
            "I'm having trouble with auto-scaling. Instances aren't scaling up during traffic spikes.",
            ["documentation_search", "diagnostic_tool", "log_analyzer"]
        )
        print(f"🤖 Assistant: {response1.generated_text[:80]}...")
        
        # 3. Follow-up with more details
        response2 = await assistant.send_support_message(
            context_id,
            "I've checked the scaling policies and thresholds. CPU is hitting 85% but no new instances launch."
        )
        print(f"🤖 Assistant: {response2.generated_text[:80]}...")
        
        # 4. Get session information
        session_info = await assistant.get_session_info(context_id)
        print(f"\n📊 Session Status: {session_info['conversation']['message_count']} messages exchanged")
        
        # 5. Resolve and close session
        resolution = await assistant.end_support_session(context_id)
        print(f"\n✅ Session resolved!")
        print(f"📝 Summary: {resolution['summary'][:100]}...")
        
    except Exception as error:
        print(f"❌ Support session failed: {error}")

# Run the technical support demonstration
if __name__ == "__main__":
    asyncio.run(demo_technical_support())