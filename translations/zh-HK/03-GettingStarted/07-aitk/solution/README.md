# 📘 作業解答：為你的計算器 MCP 伺服器新增平方根工具

## 概覽
在這次作業中，你為計算器 MCP 伺服器新增了一個可以計算平方根的工具。這個新增功能讓你的 AI 代理能夠處理更進階的數學問題，例如「16 的平方根是多少？」或「計算 √49」，並且能用自然語言指令來操作。

## 🛠️ 實作平方根工具
要新增這個功能，你在 server.py 檔案中定義了一個新的工具函式。以下是實作內容：

```python
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP
import math

server = FastMCP("calculator")

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@server.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@server.tool()
def sqrt(a: float) -> float:
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)
```

## 🔍 運作原理

- **匯入 `math` 模組**：為了執行基本算術以外的數學運算，Python 提供了內建的 `math` 模組。這個模組包含多種數學函式和常數。透過 `import math` 匯入後，你可以使用像是 `math.sqrt()` 這類計算平方根的函式。
- **函式定義**：使用 `@server.tool()` 裝飾器將 `sqrt` 函式註冊為 AI 代理可使用的工具。
- **輸入參數**：函式接受一個 `float` 型態的參數 `a`。
- **錯誤處理**：若 `a` 為負數，函式會拋出 `ValueError`，避免使用 `math.sqrt()` 計算負數平方根，因為該函式不支援負數輸入。
- **回傳值**：對於非負數輸入，函式會使用 Python 內建的 `math.sqrt()` 方法回傳 `a` 的平方根。

## 🔄 重新啟動伺服器
新增 `sqrt` 工具後，務必重新啟動 MCP 伺服器，確保代理能識別並使用這個新功能。

## 💬 測試新工具的範例指令
以下是一些可以用來測試平方根功能的自然語言指令：

- 「25 的平方根是多少？」
- 「計算 81 的平方根。」
- 「找出 0 的平方根。」
- 「2.25 的平方根是多少？」

這些指令會觸發代理呼叫 `sqrt` 工具並回傳正確結果。

## ✅ 總結
完成這次作業後，你已經：

- 為計算器 MCP 伺服器新增了 `sqrt` 工具。
- 讓 AI 代理能透過自然語言指令處理平方根計算。
- 練習了新增工具並重新啟動伺服器以整合新功能。

歡迎繼續嘗試新增更多數學工具，例如次方或對數函式，持續提升你的代理能力！

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。