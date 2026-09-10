package com.example.mcp;

import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class SecurityConfigurationTest {

    private final SecurityConfiguration configuration = new SecurityConfiguration();

    @Test
    void rejectsBlankClientId() {
        assertThrows(
                IllegalArgumentException.class,
                () -> configuration.registeredClientRepository(" ", "local-secret"));
    }

    @Test
    void rejectsBlankClientSecret() {
        assertThrows(
                IllegalArgumentException.class,
                () -> configuration.registeredClientRepository("mcp-client", ""));
    }
}