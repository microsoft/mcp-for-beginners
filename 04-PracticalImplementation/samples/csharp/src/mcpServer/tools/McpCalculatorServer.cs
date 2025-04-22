

using System.ComponentModel;
using ModelContextProtocol.Server;

namespace Calculator.Tools;

/// <summary>
/// Sample MCP Calculator Server implementation in C#.
/// 
/// This class demonstrates how to create a simple MCP server with calculator tools
/// that can perform basic arithmetic operations (add, subtract, multiply, divide).
/// </summary>
[McpServerToolType]
public class McpCalculatorServer
{
    [McpServerTool, Description("Calculates the sum of two numbers")]
    public double Add(double numberA, double numberB)
    {
        return numberA + numberB;
    }

    [McpServerTool, Description("Calculates the difference of two numbers")]
    public double Subtract(double numberA, double numberB)
    {
        return numberA - numberB;
    }

    [McpServerTool, Description("Calculates the product of two numbers")]
    public double Multiply(double numberA, double numberB)
    {
        return numberA * numberB;
    }
    
    [McpServerTool, Description("Calculates the quotient of two numbers")]
    public double Divide(double numberA, double numberB)
    {
        if (numberB == 0)
        {
            throw new ArgumentException("Cannot divide by zero");
        }
        return numberA / numberB;
    }
}