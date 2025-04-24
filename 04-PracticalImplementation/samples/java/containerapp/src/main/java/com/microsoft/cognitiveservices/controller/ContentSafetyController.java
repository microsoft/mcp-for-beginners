package com.microsoft.cognitiveservices.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.microsoft.cognitiveservices.model.PromptRequest;
import com.microsoft.cognitiveservices.service.ContentSafetyService;

import java.util.Map;

@Controller
public class ContentSafetyController {

    @Autowired
    private ContentSafetyService contentSafetyService;

    @GetMapping("/")
    public String showForm(Model model) {
        model.addAttribute("promptRequest", new PromptRequest());
        return "index";
    }

    @PostMapping("/submit")
    public String submitPrompt(@ModelAttribute PromptRequest promptRequest, Model model) {
        // Process the prompt through content safety and bot
        Map<String, String> result = contentSafetyService.processPrompt(promptRequest.getPrompt());
        
        // Add results to the model
        model.addAttribute("prompt", promptRequest.getPrompt());
        model.addAttribute("safetyResult", result.get("safetyResult"));
        model.addAttribute("botResponse", result.get("botResponse"));
        model.addAttribute("isSafe", result.get("isSafe"));
        
        // Add bot response safety check result if available
        if (result.containsKey("botResponseSafetyResult")) {
            model.addAttribute("botResponseSafetyResult", result.get("botResponseSafetyResult"));
        }
        
        // Add any error message if present
        if (result.containsKey("error")) {
            model.addAttribute("error", result.get("error"));
        }
        
        return "result";
    }
    
    @PostMapping("/process")
    public String processPrompt(@ModelAttribute PromptRequest promptRequest, Model model) {
        // Reuse the same logic as submitPrompt
        return submitPrompt(promptRequest, model);
    }
}