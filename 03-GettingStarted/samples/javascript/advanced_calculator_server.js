// advanced_mcp_calculator_server.js - Advanced MCP Calculator Server implementation in JavaScript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod"; 

// Create an MCP server
const server = new McpServer({
  name: "Advanced Calculator MCP Server",
  version: "2.0.0"
});

// Basic arithmetic operations
server.tool(
  "add",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.tool(
  "subtract",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a - b) }]
  })
);

server.tool(
  "multiply",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a * b) }]
  })
);

server.tool(
  "divide",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => {
    if (b === 0) {
      return {
        content: [{ type: "text", text: "Error: Cannot divide by zero" }],
        isError: true
      };
    }
    return {
      content: [{ type: "text", text: String(a / b) }]
    };
  }
);

// Advanced mathematical operations
server.tool(
  "power",
  {
    base: z.number(),
    exponent: z.number()
  },
  async ({ base, exponent }) => ({
    content: [{ type: "text", text: String(Math.pow(base, exponent)) }]
  })
);

server.tool(
  "square_root",
  {
    number: z.number()
  },
  async ({ number }) => {
    if (number < 0) {
      return {
        content: [{ type: "text", text: "Error: Cannot calculate square root of negative number" }],
        isError: true
      };
    }
    return {
      content: [{ type: "text", text: String(Math.sqrt(number)) }]
    };
  }
);

server.tool(
  "factorial",
  {
    n: z.number().int().min(0)
  },
  async ({ n }) => {
    if (n === 0 || n === 1) return { content: [{ type: "text", text: "1" }] };
    
    let result = 1;
    for (let i = 2; i <= n; i++) {
      result *= i;
    }
    return {
      content: [{ type: "text", text: String(result) }]
    };
  }
);

server.tool(
  "logarithm",
  {
    number: z.number().positive(),
    base: z.number().positive().default(10)
  },
  async ({ number, base }) => ({
    content: [{ type: "text", text: String(Math.log(number) / Math.log(base)) }]
  })
);

// Trigonometric functions (input in degrees, converted to radians)
server.tool(
  "sine",
  {
    angle_degrees: z.number()
  },
  async ({ angle_degrees }) => ({
    content: [{ type: "text", text: String(Math.sin(angle_degrees * Math.PI / 180)) }]
  })
);

server.tool(
  "cosine",
  {
    angle_degrees: z.number()
  },
  async ({ angle_degrees }) => ({
    content: [{ type: "text", text: String(Math.cos(angle_degrees * Math.PI / 180)) }]
  })
);

server.tool(
  "tangent",
  {
    angle_degrees: z.number()
  },
  async ({ angle_degrees }) => ({
    content: [{ type: "text", text: String(Math.tan(angle_degrees * Math.PI / 180)) }]
  })
);

// Statistical operations
server.tool(
  "mean",
  {
    numbers: z.array(z.number())
  },
  async ({ numbers }) => {
    if (numbers.length === 0) {
      return {
        content: [{ type: "text", text: "Error: Cannot calculate mean of empty array" }],
        isError: true
      };
    }
    const sum = numbers.reduce((acc, num) => acc + num, 0);
    return {
      content: [{ type: "text", text: String(sum / numbers.length) }]
    };
  }
);

server.tool(
  "median",
  {
    numbers: z.array(z.number())
  },
  async ({ numbers }) => {
    if (numbers.length === 0) {
      return {
        content: [{ type: "text", text: "Error: Cannot calculate median of empty array" }],
        isError: true
      };
    }
    
    const sorted = [...numbers].sort((a, b) => a - b);
    const mid = Math.floor(sorted.length / 2);
    
    if (sorted.length % 2 === 0) {
      return {
        content: [{ type: "text", text: String((sorted[mid - 1] + sorted[mid]) / 2) }]
      };
    } else {
      return {
        content: [{ type: "text", text: String(sorted[mid]) }]
      };
    }
  }
);

server.tool(
  "standard_deviation",
  {
    numbers: z.array(z.number()).min(2)
  },
  async ({ numbers }) => {
    const mean = numbers.reduce((acc, num) => acc + num, 0) / numbers.length;
    const variance = numbers.reduce((acc, num) => acc + Math.pow(num - mean, 2), 0) / (numbers.length - 1);
    return {
      content: [{ type: "text", text: String(Math.sqrt(variance)) }]
    };
  }
);

// Unit conversions
server.tool(
  "celsius_to_fahrenheit",
  {
    celsius: z.number()
  },
  async ({ celsius }) => ({
    content: [{ type: "text", text: String((celsius * 9/5) + 32) }]
  })
);

server.tool(
  "fahrenheit_to_celsius",
  {
    fahrenheit: z.number()
  },
  async ({ fahrenheit }) => ({
    content: [{ type: "text", text: String((fahrenheit - 32) * 5/9) }]
  })
);

server.tool(
  "kilometers_to_miles",
  {
    kilometers: z.number()
  },
  async ({ kilometers }) => ({
    content: [{ type: "text", text: String(kilometers * 0.621371) }]
  })
);

server.tool(
  "miles_to_kilometers",
  {
    miles: z.number()
  },
  async ({ miles }) => ({
    content: [{ type: "text", text: String(miles * 1.60934) }]
  })
);

server.tool(
  "kilograms_to_pounds",
  {
    kilograms: z.number()
  },
  async ({ kilograms }) => ({
    content: [{ type: "text", text: String(kilograms * 2.20462) }]
  })
);

server.tool(
  "pounds_to_kilograms",
  {
    pounds: z.number()
  },
  async ({ pounds }) => ({
    content: [{ type: "text", text: String(pounds * 0.453592) }]
  })
);

// Financial calculations
server.tool(
  "simple_interest",
  {
    principal: z.number(),
    rate: z.number(),
    time_years: z.number()
  },
  async ({ principal, rate, time_years }) => ({
    content: [{ type: "text", text: String(principal * rate * time_years) }]
  })
);

server.tool(
  "compound_interest",
  {
    principal: z.number(),
    rate: z.number(),
    time_years: z.number(),
    compounds_per_year: z.number().int().positive().default(1)
  },
  async ({ principal, rate, time_years, compounds_per_year }) => {
    const amount = principal * Math.pow(1 + rate/compounds_per_year, compounds_per_year * time_years);
    return {
      content: [{ type: "text", text: String(amount - principal) }]
    };
  }
);

server.tool(
  "monthly_payment",
  {
    principal: z.number(),
    annual_rate: z.number(),
    years: z.number().int().positive()
  },
  async ({ principal, annual_rate, years }) => {
    const monthly_rate = annual_rate / 12 / 100;
    const num_payments = years * 12;
    
    if (monthly_rate === 0) {
      return {
        content: [{ type: "text", text: String(principal / num_payments) }]
      };
    }
    
    const payment = principal * (monthly_rate * Math.pow(1 + monthly_rate, num_payments)) / 
                   (Math.pow(1 + monthly_rate, num_payments) - 1);
    
    return {
      content: [{ type: "text", text: String(payment) }]
    };
  }
);

// Utility functions
server.tool(
  "round_number",
  {
    number: z.number(),
    decimals: z.number().int().min(0).default(2)
  },
  async ({ number, decimals }) => ({
    content: [{ type: "text", text: String(Number(number.toFixed(decimals))) }]
  })
);

server.tool(
  "percentage",
  {
    part: z.number(),
    whole: z.number()
  },
  async ({ part, whole }) => {
    if (whole === 0) {
      return {
        content: [{ type: "text", text: "Error: Whole cannot be zero" }],
        isError: true
      };
    }
    return {
      content: [{ type: "text", text: String((part / whole) * 100) }]
    };
  }
);

server.tool(
  "percentage_of",
  {
    percentage: z.number(),
    whole: z.number()
  },
  async ({ percentage, whole }) => ({
    content: [{ type: "text", text: String((percentage / 100) * whole) }]
  })
);

server.tool(
  "get_server_info",
  {},
  async () => ({
    content: [{ 
      type: "text", 
      text: JSON.stringify({
        name: "Advanced Calculator MCP Server",
        version: "2.0.0",
        description: "Advanced mathematical operations, statistics, and unit conversions",
        features: [
          "Basic arithmetic",
          "Advanced mathematics",
          "Trigonometric functions",
          "Statistical operations",
          "Unit conversions",
          "Financial calculations",
          "Utility functions"
        ]
      }, null, 2)
    }]
  })
);

// Connect the server using stdio transport
const transport = new StdioServerTransport();
server.connect(transport).catch(console.error);

console.log("Advanced Calculator MCP Server started");
