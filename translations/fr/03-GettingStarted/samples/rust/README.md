# Exemple

Ceci est un exemple en Rust pour un serveur MCP

Voici à quoi ressemble la partie calculatrice :

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

Exécutez la commande suivante :

```bash
cargo build
```

## Exécution

```bash
cargo run
```

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.