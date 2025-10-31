// Java Example: Financial Analysis Context Setup
package com.example.mcp.contexts;

import com.mcp.client.McpClient;
import com.mcp.client.ContextManager;
import com.mcp.models.RootContext;
import com.mcp.models.McpResponse;
import java.util.HashMap;
import java.util.Map;

public class FinancialAnalysisContext {
    private final McpClient client;
    private final ContextManager contextManager;
    
    public FinancialAnalysisContext(String serverUrl) {
        this.client = new McpClient.Builder()
            .setServerUrl(serverUrl)
            .build();
        this.contextManager = new ContextManager(client);
    }

    public String createAnalysisSession() throws Exception {
        // Prepare metadata for our financial analysis
        Map<String, String> metadata = new HashMap<>();
        metadata.put("projectName", "Q1 2025 Financial Analysis");
        metadata.put("userRole", "Senior Financial Analyst");
        metadata.put("dataSource", "Q1 2025 Financial Reports");
        metadata.put("analysisType", "Technology Division Review");
        
        // Create the root context
        RootContext context = contextManager.createRootContext(
            "Financial Analysis Session", metadata);
        String contextId = context.getId();
        
        System.out.println("📊 Created financial analysis context: " + contextId);
        return contextId;
    }

    public void performInitialAnalysis(String contextId) throws Exception {
        // Ask the first analytical question
        McpResponse response1 = client.sendPrompt(
            "Analyze the trends in Q1 financial data for our technology division. " +
            "Focus on revenue growth and major cost drivers.",
            contextId
        );
        
        System.out.println("📈 Initial Analysis:");
        System.out.println(response1.getGeneratedText());
        
        // Store key findings in context metadata
        contextManager.addContextMetadata(contextId, 
            Map.of("initialFinding", "Technology division showing strong revenue growth"));
    }

    public void performDeepDive(String contextId) throws Exception {
        // Update context with discovered trend
        contextManager.addContextMetadata(contextId, 
            Map.of("identifiedTrend", "Increasing cloud infrastructure costs"));
        
        // Follow-up question that builds on previous analysis
        McpResponse response2 = client.sendPrompt(
            "What's driving the increase in cloud infrastructure costs? " +
            "How does this compare to industry benchmarks?",
            contextId
        );
        
        System.out.println("🔍 Deep Dive Analysis:");
        System.out.println(response2.getGeneratedText());
    }

    public void generateExecutiveSummary(String contextId) throws Exception {
        // Generate a comprehensive summary
        McpResponse summaryResponse = client.sendPrompt(
            "Based on our entire analysis, create an executive summary " +
            "with 3-5 key findings and actionable recommendations.",
            contextId
        );
        
        // Store the summary for future reference
        contextManager.addContextMetadata(contextId, Map.of(
            "executiveSummary", summaryResponse.getGeneratedText(),
            "analysisComplete", "true"
        ));
        
        System.out.println("📋 Executive Summary:");
        System.out.println(summaryResponse.getGeneratedText());
    }

    public void finalizeAnalysis(String contextId) throws Exception {
        // Get comprehensive context information
        RootContext updatedContext = contextManager.getRootContext(contextId);
        
        System.out.println("\n📊 Final Context Information:");
        System.out.println("├─ Created: " + updatedContext.getCreatedAt());
        System.out.println("├─ Last Updated: " + updatedContext.getLastUpdatedAt());
        System.out.println("└─ Status: Analysis Complete");
        
        // Archive the completed analysis
        contextManager.archiveContext(contextId);
        System.out.println("\n🗄️ Financial analysis context archived successfully");
    }

    public void runCompleteAnalysis() throws Exception {
        String contextId = createAnalysisSession();
        performInitialAnalysis(contextId);
        performDeepDive(contextId);
        generateExecutiveSummary(contextId);
        finalizeAnalysis(contextId);
    }

    public static void main(String[] args) {
        try {
            FinancialAnalysisContext example = new FinancialAnalysisContext("https://mcp-server-example.com");
            example.runCompleteAnalysis();
            System.out.println("✅ Financial analysis demonstration completed!");
        } catch (Exception e) {
            System.err.println("❌ Error running analysis: " + e.getMessage());
            e.printStackTrace();
        }
    }
}