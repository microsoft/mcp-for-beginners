# Sample

This is a Rust example for an MCP Server

Here's how the calculator section appears:

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[tool_router]
impl Calculator {
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
    }

    #[tool(description = "Subtracts b from a")]
    async fn subtract(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a - b).to_string()
    }

    #[tool(description = "Multiply a with b")]
    async fn multiply(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a * b).to_string()
    }

    #[tool(description = "Divides a by b")]
    async fn divide(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        if b == 0.0 {
            "Error: Division by zero".to_string()
        } else {
            (a / b).to_string()
        }
    }
}
```

## Installation

Execute the following command:

```bash
cargo build
```

## Execution

```bash
cargo run
```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.