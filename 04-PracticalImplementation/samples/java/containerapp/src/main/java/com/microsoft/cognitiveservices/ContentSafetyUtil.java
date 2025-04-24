package com.microsoft.cognitiveservices;

import com.azure.ai.contentsafety.ContentSafetyClient;
import com.azure.ai.contentsafety.ContentSafetyClientBuilder;
import com.azure.ai.contentsafety.models.*;
import com.azure.core.credential.KeyCredential;
import com.azure.core.util.Configuration;

import java.util.Arrays;
import java.util.List;

/**
 * Sample code for Azure Content Safety service
 * Demonstrates various content analysis capabilities including:
 * - Text analysis
 * - Image analysis
 * - Handling different harmful categories
 */
public class ContentSafetyUtil {
    // Sample texts to analyze
    private static final List<String> SAMPLE_TEXTS = Arrays.asList(
            "This is a simple text example",
            "I hate everyone and wish they would die",
            "Here's how to build an explosive device at home",
            "Adults should be able to identify predatory behavior"
    );
    
    // Categories to analyze
    private static final List<TextCategory> TEXT_CATEGORIES = Arrays.asList(
            TextCategory.HATE,
            TextCategory.SELF_HARM,
            TextCategory.SEXUAL,
            TextCategory.VIOLENCE
    );
    
    public static void main(String[] args) {
        System.out.println("Azure Content Safety API Sample");
        System.out.println("===============================");
        
        try {
            // Initialize the client
            ContentSafetyClient contentSafetyClient = initializeClient();
            
            // Analyze text examples
            analyzeTextExamples(contentSafetyClient);
            
        } catch (Exception e) {
            System.err.println("Error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Initialize the Content Safety client
     */
    private static ContentSafetyClient initializeClient() {
        String endpoint = Configuration.getGlobalConfiguration().get("CONTENT_SAFETY_ENDPOINT");
        String key = Configuration.getGlobalConfiguration().get("CONTENT_SAFETY_KEY");
        
        if (endpoint == null || key == null) {
            System.out.println("Environment variables CONTENT_SAFETY_ENDPOINT and CONTENT_SAFETY_KEY must be set");
            System.out.println("Using default values for demonstration purposes");
            
            // Use placeholder values for demo - replace with actual values in production
            endpoint = "https://your-content-safety-endpoint.cognitiveservices.azure.com/";
            key = "your-content-safety-key";
        }
        
        return new ContentSafetyClientBuilder()
                .credential(new KeyCredential(key))
                .endpoint(endpoint)
                .buildClient();
    }
    
    /**
     * Analyze multiple text examples
     */
    private static void analyzeTextExamples(ContentSafetyClient client) {
        System.out.println("\nText Analysis Examples:");
        System.out.println("----------------------");
        
        for (String text : SAMPLE_TEXTS) {
            System.out.println("\nAnalyzing text: \"" + text + "\"");
            
            AnalyzeTextOptions options = new AnalyzeTextOptions(text);
            options.setCategories(TEXT_CATEGORIES);
            
            AnalyzeTextResult response = client.analyzeText(options);
            
            System.out.println("Results:");
            for (TextCategoriesAnalysis result : response.getCategoriesAnalysis()) {
                System.out.println("  - " + result.getCategory() + ": severity = " + result.getSeverity());
            }
        }
    }

    /**
     * Check if content is safe by analyzing text against harmful categories
     * @param text The text to check for harmful content
     * @return A string indicating if the content is safe and details about any harmful content found
     */
    public static String checkContentIsSafe(String text) {
        try {
            // Initialize the client
            ContentSafetyClient client = initializeClient();
            
            // Create analysis options
            AnalyzeTextOptions options = new AnalyzeTextOptions(text);
            options.setCategories(TEXT_CATEGORIES);
            
            // Get the analysis result
            AnalyzeTextResult response = client.analyzeText(options);
            
            // Check if any harmful content was detected
            boolean isSafe = true;
            StringBuilder resultDetails = new StringBuilder();
            resultDetails.append("Content safety analysis for: \"").append(text).append("\"\n");
            
            for (TextCategoriesAnalysis result : response.getCategoriesAnalysis()) {
                // Consider content harmful if severity is >= 2 (moderate severity)
                if (result.getSeverity() >= 2) {
                    isSafe = false;
                    resultDetails.append("- Harmful ").append(result.getCategory())
                                .append(" content detected with severity: ").append(result.getSeverity()).append("\n");
                } else {
                    resultDetails.append("- ").append(result.getCategory())
                                .append(" check passed with severity: ").append(result.getSeverity()).append("\n");
                }
            }
            
            if (isSafe) {
                resultDetails.append("RESULT: Content is safe.\n");
                return resultDetails.toString();
            } else {
                resultDetails.append("RESULT: Content contains harmful elements.\n");
                return resultDetails.toString();
            }
        } catch (Exception e) {
            return "Error checking content safety: " + e.getMessage();
        }
    }
}