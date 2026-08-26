#!/usr/bin/env python3
"""
Test script for the MCP Calculator Server.

This script tests the calculator functions to ensure they work correctly
before running the MCP server.
"""

import sys
import os
import json
import subprocess

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


def request_server(method, params=None):
    """Send one version-less JSON-RPC request to a fresh server."""
    server = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_calculator_server.py")
    request = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params is not None:
        request["params"] = params
    process = subprocess.run(
        [sys.executable, server],
        input=json.dumps(request) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
        check=True,
    )
    return json.loads(process.stdout.splitlines()[0])["result"]


def test_protocol_discovery():
    """Test draft discovery and default version negotiation."""
    discovery = request_server("server/discover")
    assert "2026-07-28" in discovery["supportedVersions"]
    assert "2025-11-25" in discovery["supportedVersions"]
    assert discovery["capabilities"]["tools"] is not None
    assert discovery["resultType"] == "complete"
    assert discovery["ttlMs"] >= 0
    assert discovery["cacheScope"] in {"public", "private"}

    tools = request_server("tools/list")
    assert {tool["name"] for tool in tools["tools"]} == {
        "add",
        "subtract",
        "multiply",
        "divide",
    }

    initialized = request_server(
        "initialize",
        {
            "protocolVersion": "2025-11-25",
            "capabilities": {},
            "clientInfo": {"name": "calculator-test", "version": "1.0"},
        },
    )
    assert initialized["protocolVersion"] == "2025-11-25"


if __name__ == "__main__":
    test_calculator_functions()
    test_protocol_discovery()