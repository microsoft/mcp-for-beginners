# 🧮 Servidor MCP de Calculadora Avanzada (JavaScript)

## Descripción

Este es un servidor MCP avanzado implementado en JavaScript que proporciona una amplia gama de herramientas matemáticas, estadísticas y conversiones de unidades. Demuestra cómo crear servidores MCP robustos usando el SDK de JavaScript con validación de tipos usando Zod.

## Características

### 🔢 Operaciones Aritméticas Básicas
- **add(a, b)**: Suma dos números
- **subtract(a, b)**: Resta b de a
- **multiply(a, b)**: Multiplica dos números
- **divide(a, b)**: Divide a entre b (con validación de división por cero)

### 🧮 Matemáticas Avanzadas
- **power(base, exponent)**: Eleva base al exponente
- **square_root(number)**: Calcula la raíz cuadrada (con validación para números negativos)
- **factorial(n)**: Calcula el factorial de un número entero no negativo
- **logarithm(number, base)**: Calcula el logaritmo con base especificada (por defecto 10)

### 📐 Funciones Trigonométricas
- **sine(angle_degrees)**: Calcula el seno de un ángulo en grados
- **cosine(angle_degrees)**: Calcula el coseno de un ángulo en grados
- **tangent(angle_degrees)**: Calcula la tangente de un ángulo en grados

### 📊 Operaciones Estadísticas
- **mean(numbers)**: Calcula la media aritmética de un array de números
- **median(numbers)**: Calcula la mediana de un array de números
- **standard_deviation(numbers)**: Calcula la desviación estándar (mínimo 2 números)

### 🔄 Conversiones de Unidades
- **celsius_to_fahrenheit(celsius)**: Convierte Celsius a Fahrenheit
- **fahrenheit_to_celsius(fahrenheit)**: Convierte Fahrenheit a Celsius
- **kilometers_to_miles(kilometers)**: Convierte kilómetros a millas
- **miles_to_kilometers(miles)**: Convierte millas a kilómetros
- **kilograms_to_pounds(kilograms)**: Convierte kilogramos a libras
- **pounds_to_kilograms(pounds)**: Convierte libras a kilogramos

### 💰 Cálculos Financieros
- **simple_interest(principal, rate, time_years)**: Calcula interés simple
- **compound_interest(principal, rate, time_years, compounds_per_year)**: Calcula interés compuesto
- **monthly_payment(principal, annual_rate, years)**: Calcula pago mensual de hipoteca

### 🛠️ Funciones de Utilidad
- **round_number(number, decimals)**: Redondea un número a decimales específicos
- **percentage(part, whole)**: Calcula qué porcentaje es parte del total
- **percentage_of(percentage, whole)**: Calcula qué cantidad es el porcentaje dado del total
- **get_server_info()**: Obtiene información del servidor en formato JSON

## Instalación

1. Asegúrate de tener Node.js 18+ instalado
2. Instala las dependencias:
```bash
npm install @modelcontextprotocol/sdk zod
```

## Uso

### Ejecutar el Servidor
```bash
node advanced_calculator_server.js
```

### Ejemplo de Configuración MCP
Crea un archivo `mcp-config.json`:
```json
{
  "mcpServers": {
    "advanced-calculator-js": {
      "command": "node",
      "args": ["path/to/advanced_calculator_server.js"],
      "env": {}
    }
  }
}
```

## Validación de Tipos con Zod

Este servidor utiliza Zod para validación de tipos en tiempo de ejecución:

```javascript
// Ejemplo de validación
server.tool(
  "factorial",
  {
    n: z.number().int().min(0)  // Solo números enteros no negativos
  },
  async ({ n }) => {
    // La función solo se ejecuta si la validación pasa
  }
);
```

## Manejo de Errores

El servidor incluye manejo de errores robusto:

```javascript
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
        isError: true  // Marca la respuesta como error
      };
    }
    return {
      content: [{ type: "text", text: String(a / b) }]
    };
  }
);
```

## Ejemplos de Uso

### Operaciones Básicas
```javascript
// Suma
const result = await add({ a: 5, b: 3 });  // "8"

// Multiplicación
const result = await multiply({ a: 4, b: 7 });  // "28"

// División con manejo de errores
const result = await divide({ a: 10, b: 2 });  // "5"
const error = await divide({ a: 10, b: 0 });   // Error: Cannot divide by zero
```

### Matemáticas Avanzadas
```javascript
// Potencia
const result = await power({ base: 2, exponent: 8 });  // "256"

// Raíz cuadrada
const result = await square_root({ number: 16 });  // "4"

// Factorial
const result = await factorial({ n: 5 });  // "120"
```

### Estadísticas
```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const mean_value = await mean({ numbers });  // "5.5"
const median_value = await median({ numbers });  // "5.5"
const std_dev = await standard_deviation({ numbers });  // "3.0276503540974917"
```

### Conversiones
```javascript
// Temperatura
const fahrenheit = await celsius_to_fahrenheit({ celsius: 25 });  // "77"
const celsius = await fahrenheit_to_celsius({ fahrenheit: 98.6 });  // "37"

// Distancia
const miles = await kilometers_to_miles({ kilometers: 100 });  // "62.1371"
const kilometers = await miles_to_kilometers({ miles: 50 });  // "80.467"
```

### Cálculos Financieros
```javascript
// Interés simple
const interest = await simple_interest({ principal: 1000, rate: 0.05, time_years: 2 });  // "100"

// Pago mensual de hipoteca
const payment = await monthly_payment({ principal: 200000, annual_rate: 4.5, years: 30 });  // "1013.37"
```

## Ventajas de esta Implementación

1. **Validación Robusta**: Uso de Zod para validación de tipos en tiempo de ejecución
2. **Manejo de Errores**: Respuestas de error estructuradas con `isError: true`
3. **Async/Await**: Todas las funciones son asíncronas para mejor rendimiento
4. **Tipado Fuerte**: Validación de tipos para prevenir errores en tiempo de ejecución
5. **Modularidad**: Código bien organizado y fácil de extender

## Extensibilidad

Para agregar nuevas funciones:

```javascript
server.tool(
  "nueva_funcion",
  {
    parametro1: z.number(),
    parametro2: z.string().optional()
  },
  async ({ parametro1, parametro2 }) => {
    // Lógica de la función
    return {
      content: [{ type: "text", text: "resultado" }]
    };
  }
);
```

## Contribuciones

Este servidor es un ejemplo de cómo implementar servidores MCP robustos en JavaScript. Puedes contribuir:

1. Agregando nuevas funciones matemáticas
2. Implementando más conversiones de unidades
3. Mejorando el manejo de errores
4. Agregando pruebas unitarias
5. Optimizando el rendimiento

## Licencia

Este código está bajo la misma licencia que el proyecto principal MCP for Beginners.

## Autor

Contribución de la comunidad para el proyecto MCP for Beginners de Microsoft.
