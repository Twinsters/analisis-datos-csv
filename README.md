Análisis de Datos Reales con Pandas
Es una aplicación de consola desarrollada en Python que permite explorar, filtrar, agrupar y exportar datos desde un archivo CSV.

Características
- Limpieza automática de datos (`dropna`, `drop_duplicates`)
- Exploración de columnas dinámicas
- Filtro por cabecera y valor ingresado
- Agrupación con conteo por categoría
- Exportación a Excel (`openpyxl`)
- Interfaz de texto interactiva en consola

Tecnologías utilizadas
- Python 3
- Pandas
- OpenPyXL (para exportar a Excel)

Estructura del proyecto
```
Analisis de Datos con Pandas/
│
├── Recursos/
│ └── netflix_titles_CLEANED.csv
│
├── Analisis_de_datos_Pandas.py
├── README.md
└── .gitignore
```
Ejecución
1. Instala las dependencias necesarias:
   ```bash
   pip install pandas openpyxl

2.Ejecuta el programa
```
     python Analisis_de_datos_Pandas.py
```
3.Navega por el menú en consola
```
        1 - Ver Cabeceras
        2 - Filtrar por Cabecera
        3 - Agrupar por Cabecera
        4 - Exportar a Excel
        0 - Salir
```
Autor
Creado por Claudio Herrera  — proyecto personal de práctica en análisis de datos con Pandas.
