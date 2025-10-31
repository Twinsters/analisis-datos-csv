## Purpose

This file gives focused, actionable instructions for AI coding agents working on this small Pandas-based project.
Keep changes minimal and preserve the project's Spanish naming / CLI style unless refactoring intentionally.

## Big picture

- Single-script CLI data explorer: `Analisis_de_datos_Pandas.py` reads `./Recursos/netflix_titles_CLEANED.csv`, cleans rows, and offers interactive commands to view headers, filter, group, and export results to Excel.
- Data lives in `Recursos/` and outputs (Excel) are written back to `./Recursos/`.
- The project is organized as a single pedagogical script rather than a package. Expect imperative flow and global state (`inicio`, `tabla`, `tabla_acciones`).

## How to run (developer workflow)

1. Ensure dependencies are installed. The script imports `pandas`. Excel export may require `openpyxl`.

   Example (PowerShell):

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install pandas openpyxl
   python .\Analisis_de_datos_Pandas.py
   ```

2. Run from the project root so the relative path `./Recursos/netflix_titles_CLEANED.csv` resolves correctly.
3. The script is interactive: use the console (not a non-interactive runner). You'll be prompted to choose options by entering numbers and text (Spanish prompts).

## Important, discoverable patterns & conventions

- Variable and function names are Spanish (e.g., `tabla`, `ver_cabeceras`, `filtrar_por_cabecera`). Keep this convention when adding new symbols.
- The header mapping is created via `cabeceras = tabla.head(0)` and `dic_cabeceras = dict(enumerate(cabeceras))`. When referencing headers, the code expects the user to input the header index (integer).
- Console clearing uses `print("\033c", end="")` — this is a cross-platform attempt but may behave differently on Windows PowerShell. If you modify console clearing, test interactively.
- Exports: `exportar_Excel(tabla_exportar, nombre='Resultado.xlsx')` writes to `./Recursos/{nombre}` using `pandas.DataFrame.to_excel()`.

## Examples for agents (what good edits look like)

- Small fix: If adding a dependency, update README or add `requirements.txt` with `pandas` and `openpyxl`.
- Small feature: Add a non-interactive CLI flag (e.g., `--export-only path`) near the top; keep existing interactive flow unchanged by default.
- Safe refactor: Encapsulate grouped logic into functions but preserve Spanish names and the `tabla_acciones` dispatch mapping.

## Known pitfalls to avoid

- Do not change the CSV path semantics; the script assumes `./Recursos/` exists and contains `netflix_titles_CLEANED.csv`.
- Avoid converting the interactive flow to a background job without adding CLI flags; tests and manual runs depend on input() prompts.
- Excel export may fail if `openpyxl` isn't installed — handle by adding it to project deps or catch and surface a clear message.

## Key files to reference

- `Analisis_de_datos_Pandas.py` — primary script (interactive CLI). Refer here for all core behavior.
- `Recursos/netflix_titles_CLEANED.csv` — sample data; used by the script and expected to be present.

## When in doubt

- Run the script locally and exercise each menu option to observe behavior before making changes.
- Preserve Spanish naming and prompts unless converting the project to an English interface — that is a larger scope and should be isolated in a new file.

---
If any of these items are unclear or you want the doc to be in Spanish instead, tell me which sections to revise.
