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

    [McpServerTool, Description("Finds the next 5 prime numbers after the given number")]
    public List<long> NextFivePrimeNumbers(long startNumber)
    {
        var result = new List<long>(5);
        long number = startNumber;
        
        while (result.Count < 5)
        {
            number++;
            if (IsPrime(number))
            {
                result.Add(number);
            }
        }
        
        return result;
    }
    
    // Helper method to efficiently check if a number is prime
    private bool IsPrime(long number)
    {
        if (number <= 1) return false;
        if (number <= 3) return true;
        if (number % 2 == 0 || number % 3 == 0) return false;
        
        // Check divisibility using the 6k±1 optimization
        for (long i = 5; i * i <= number; i += 6)
        {
            if (number % i == 0 || number % (i + 2) == 0)
            {
                return false;
            }
        }
        
        return true;
    }
}