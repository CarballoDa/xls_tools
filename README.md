# XLS Tools

A Python library to simplify Excel file manipulation: reading, writing, and modifying rows, columns, and data. Ideal for automating repetitive tasks, saving time on data analysis and comparison, and improving spreadsheet productivity.

## Goals

- Learn best practices for Python programming.
- Develop a modular and scalable library.
- Implement version control with Git and GitHub.
- Implement automated tests with `pytest`.
- Document and structure code correctly.

## Technologies

- [Python 3.10+](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)
- [pytest](https://docs.pytest.org/)
- [black](https://black.readthedocs.io/) + [flake8](https://flake8.pycqa.org/) code style

## Installation
```bash
git clone https://github.com/tu-usuario/excel-tools.git
cd excel-tools
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt

## Structure

```bash
excel_tools/
├── excel_tools/         # Code
│   ├── reader.py
│   ├── writer.py
│   └── utils.py
├── tests/               # Tests
├── examples/            # Examples
├── requirements.txt
├── README.md
└── .gitignore

## Running Tests

```bash
pytest tests/

## Project Status

Work in progress

## License

MIT License