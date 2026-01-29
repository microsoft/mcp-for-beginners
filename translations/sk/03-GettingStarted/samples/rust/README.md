# Ukážka

Toto je ukážka Rust kódu pre MCP Server

Takto vyzerá časť kalkulačky:

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

## Inštalácia

Spustite nasledujúci príkaz:

```bash
cargo build
```

## Spustenie

```bash
cargo run
```

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.