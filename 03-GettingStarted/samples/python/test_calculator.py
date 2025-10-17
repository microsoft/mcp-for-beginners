#!/usr/bin/env python3
"""
Test script for the MCP Calculator Server.

This script tests the calculator functions to ensure they work correctly
before running the MCP server.
"""

import sys
import os

# Add the current directory to the path so we can import the calculator server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_calculator_functions():
    """Test all calculator functions."""
    # Import the functions from the calculator server
    from mcp_calculator_server import add, subtract, multiply, divide
    
    print("Testing calculator functions...")
    
    # Test addition
    result = add(5, 3)
    assert result == 8, f"Expected 8, got {result}"
    print("✓ Addition test passed")
    
    # Test subtraction
    result = subtract(10, 4)
    assert result == 6, f"Expected 6, got {result}"
    print("✓ Subtraction test passed")
    
    # Test multiplication
    result = multiply(7, 6)
    assert result == 42, f"Expected 42, got {result}"
    print("✓ Multiplication test passed")
    
    # Test division
    result = divide(15, 3)
    assert result == 5, f"Expected 5, got {result}"
    print("✓ Division test passed")
    
    # Test division by zero
    try:
        divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero", f"Expected 'Cannot divide by zero', got '{str(e)}'"
        print("✓ Division by zero test passed")
    
    print("\nAll calculator function tests passed! ✅")

if __name__ == "__main__":
    test_calculator_functions()