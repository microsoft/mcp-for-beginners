# 🧮 Servidor MCP de Calculadora Avanzada

## Descripción

Este es un servidor MCP avanzado que proporciona una amplia gama de herramientas matemáticas, estadísticas y conversiones de unidades. Es una extensión del servidor básico de calculadora que demuestra cómo crear herramientas MCP más complejas y útiles.

## Características

### 🔢 Operaciones Aritméticas Básicas
- **add(a, b)**: Suma dos números
- **subtract(a, b)**: Resta b de a
- **multiply(a, b)**: Multiplica dos números
- **divide(a, b)**: Divide a entre b

### 🧮 Matemáticas Avanzadas
- **power(base, exponent)**: Eleva base al exponente
- **square_root(number)**: Calcula la raíz cuadrada
- **factorial(n)**: Calcula el factorial de un número
- **logarithm(number, base)**: Calcula el logaritmo con base especificada

### 📐 Funciones Trigonométricas
- **sine(angle_degrees)**: Calcula el seno de un ángulo en grados
- **cosine(angle_degrees)**: Calcula el coseno de un ángulo en grados
- **tangent(angle_degrees)**: Calcula la tangente de un ángulo en grados

### 📊 Operaciones Estadísticas
- **mean(numbers)**: Calcula la media aritmética
- **median(numbers)**: Calcula la mediana
- **standard_deviation(numbers)**: Calcula la desviación estándar
- **variance(numbers)**: Calcula la varianza

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
- **get_server_info()**: Obtiene información del servidor

## Instalación

1. Asegúrate de tener Python 3.8+ instalado
2. Instala las dependencias:
```bash
pip install mcp-server-fastmcp
```

## Uso

### Ejecutar el Servidor
```bash
python advanced_calculator_server.py
```

### Ejemplo de Configuración MCP
Crea un archivo `mcp-config.json`:
```json
{
  "mcpServers": {
    "advanced-calculator": {
      "command": "python",
      "args": ["path/to/advanced_calculator_server.py"],
      "env": {}
    }
  }
}
```

## Ejemplos de Uso

### Operaciones Básicas
```python
# Suma
result = add(5, 3)  # 8.0

# Multiplicación
result = multiply(4, 7)  # 28.0

# División
result = divide(10, 2)  # 5.0
```

### Matemáticas Avanzadas
```python
# Potencia
result = power(2, 8)  # 256.0

# Raíz cuadrada
result = square_root(16)  # 4.0

# Factorial
result = factorial(5)  # 120
```

### Estadísticas
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean_value = mean(numbers)  # 5.5
median_value = median(numbers)  # 5.5
std_dev = standard_deviation(numbers)  # 3.0276503540974917
```

### Conversiones
```python
# Temperatura
fahrenheit = celsius_to_fahrenheit(25)  # 77.0
celsius = fahrenheit_to_celsius(98.6)  # 37.0

# Distancia
miles = kilometers_to_miles(100)  # 62.1371
kilometers = miles_to_kilometers(50)  # 80.467
```

### Cálculos Financieros
```python
# Interés simple
interest = simple_interest(1000, 0.05, 2)  # 100.0

# Pago mensual de hipoteca
payment = monthly_payment(200000, 4.5, 30)  # 1013.37
```

## Manejo de Errores

El servidor incluye validación de entrada y manejo de errores apropiado:

- **División por cero**: Se lanza `ValueError`
- **Raíz cuadrada de números negativos**: Se lanza `ValueError`
- **Factorial de números negativos**: Se lanza `ValueError`
- **Logaritmo de números no positivos**: Se lanza `ValueError`
- **Listas vacías para estadísticas**: Se lanza `ValueError`

## Contribuciones

Este servidor es un ejemplo de cómo extender las capacidades básicas de MCP. Puedes contribuir:

1. Agregando nuevas funciones matemáticas
2. Implementando más conversiones de unidades
3. Mejorando el manejo de errores
4. Agregando documentación adicional
5. Creando pruebas unitarias

## Licencia

Este código está bajo la misma licencia que el proyecto principal MCP for Beginners.

## Autor

Contribución de la comunidad para el proyecto MCP for Beginners de Microsoft.
