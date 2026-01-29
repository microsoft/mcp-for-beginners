# Зразок

Це приклад на Rust для MCP Server

Ось як виглядає частина калькулятора:

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

## Встановлення

Запустіть наступну команду:

```bash
cargo build
```

## Запуск

```bash
cargo run
```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.