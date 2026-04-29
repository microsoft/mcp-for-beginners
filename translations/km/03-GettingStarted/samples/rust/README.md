# លំនាំ

នេះជាលំនាំ Rust សម្រាប់ម៉ាស៊ីនមេ MCP

នេះគឺជាផ្នែកគណនាករដូចខាងក្រោម៖

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

## ដំឡើង

រត់ពាក្យបញ្ជាដូចខាងក្រោម៖

```bash
cargo build
```

## រត់

```bash
cargo run
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ដោយផ្តោតទៅលើភាពត្រឹមត្រូវ យើងសូមជម្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការមិនត្រឹមត្រូវខ្លះៗ។ ឯកសារដើមនៅក្នុងភាសាម្ចាស់របស់វាជាភស្តុតាងដែលមានសក្តានុពល។ សម្រាប់ព័ត៌មានសំខាន់ៗ គ្រាន់តែផ្ដល់អភិបាលការបកប្រែដោយអ្នកជំនាញមនុស្សគឺមានលទ្ធផលល្អបំផុត។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតឡើងពីការពឹងផ្អែកលើការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->