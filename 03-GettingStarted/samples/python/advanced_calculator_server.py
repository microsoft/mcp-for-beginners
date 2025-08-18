#!/usr/bin/env python3
"""
Advanced MCP Calculator Server implementation in Python.

This module demonstrates how to create an advanced MCP server with extended calculator tools
that can perform mathematical operations, statistics, and unit conversions.
"""

import asyncio
import math
import statistics
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
from mcp.server.transports.stdio import serve_stdio

# Create a FastMCP server
mcp = FastMCP(
    name="Advanced Calculator MCP Server",
    version="2.0.0"
)

# Basic arithmetic operations
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Advanced mathematical operations
@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return math.pow(base, exponent)

@mcp.tool()
def square_root(number: float) -> float:
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)

@mcp.tool()
def logarithm(number: float, base: float = 10) -> float:
    """Calculate the logarithm of a number with specified base (default: 10)."""
    if number <= 0 or base <= 0:
        raise ValueError("Both number and base must be positive")
    return math.log(number, base)

# Trigonometric functions
@mcp.tool()
def sine(angle_degrees: float) -> float:
    """Calculate the sine of an angle in degrees."""
    return math.sin(math.radians(angle_degrees))

@mcp.tool()
def cosine(angle_degrees: float) -> float:
    """Calculate the cosine of an angle in degrees."""
    return math.cos(math.radians(angle_degrees))

@mcp.tool()
def tangent(angle_degrees: float) -> float:
    """Calculate the tangent of an angle in degrees."""
    return math.tan(math.radians(angle_degrees))

# Statistical operations
@mcp.tool()
def mean(numbers: List[float]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return statistics.mean(numbers)

@mcp.tool()
def median(numbers: List[float]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    return statistics.median(numbers)

@mcp.tool()
def standard_deviation(numbers: List[float]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    if len(numbers) < 2:
        raise ValueError("Need at least 2 numbers to calculate standard deviation")
    return statistics.stdev(numbers)

@mcp.tool()
def variance(numbers: List[float]) -> float:
    """Calculate the variance of a list of numbers."""
    if len(numbers) < 2:
        raise ValueError("Need at least 2 numbers to calculate variance")
    return statistics.variance(numbers)

# Unit conversions
@mcp.tool()
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

@mcp.tool()
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

@mcp.tool()
def kilometers_to_miles(kilometers: float) -> float:
    """Convert distance from kilometers to miles."""
    return kilometers * 0.621371

@mcp.tool()
def miles_to_kilometers(miles: float) -> float:
    """Convert distance from miles to kilometers."""
    return miles * 1.60934

@mcp.tool()
def kilograms_to_pounds(kilograms: float) -> float:
    """Convert weight from kilograms to pounds."""
    return kilograms * 2.20462

@mcp.tool()
def pounds_to_kilograms(pounds: float) -> float:
    """Convert weight from pounds to kilograms."""
    return pounds * 0.453592

# Financial calculations
@mcp.tool()
def simple_interest(principal: float, rate: float, time_years: float) -> float:
    """Calculate simple interest given principal, annual rate, and time in years."""
    return principal * rate * time_years

@mcp.tool()
def compound_interest(principal: float, rate: float, time_years: float, 
                     compounds_per_year: int = 1) -> float:
    """Calculate compound interest with specified compounding frequency."""
    return principal * (1 + rate/compounds_per_year)**(compounds_per_year * time_years) - principal

@mcp.tool()
def monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly mortgage payment."""
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    if monthly_rate == 0:
        return principal / num_payments
    return principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

# Utility functions
@mcp.tool()
def round_number(number: float, decimals: int = 2) -> float:
    """Round a number to specified decimal places."""
    return round(number, decimals)

@mcp.tool()
def percentage(part: float, whole: float) -> float:
    """Calculate what percentage part is of whole."""
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

@mcp.tool()
def percentage_of(percentage: float, whole: float) -> float:
    """Calculate what amount is the given percentage of whole."""
    return (percentage / 100) * whole

@mcp.tool()
def get_server_info() -> Dict[str, Any]:
    """Get information about the MCP server."""
    return {
        "name": "Advanced Calculator MCP Server",
        "version": "2.0.0",
        "description": "Advanced mathematical operations, statistics, and unit conversions",
        "features": [
            "Basic arithmetic",
            "Advanced mathematics",
            "Trigonometric functions",
            "Statistical operations",
            "Unit conversions",
            "Financial calculations",
            "Utility functions"
        ]
    }

if __name__ == "__main__":
    # Start the server with stdio transport
    asyncio.run(serve_stdio(mcp))
