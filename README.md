# ImportCZ 📊

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.3.17-green)](https://www.sqlalchemy.org/)
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.0.3-yellow)](https://openpyxl.readthedocs.io/)

A Python-based project for importing and processing data from various Excel files and HTML tables into a SQL database.

## 🌟 Features

- Import data from Excel files (.xlsx, .xlsm) and HTML tables
- Support for multiple data formats and configurations
- Flexible column mapping and data type handling
- Database integration using SQLAlchemy
- Configurable import settings

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/RicardoR-M/ImportCZ.git
   cd ImportCZ
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your database connection:
   Create a `.env` file in the project root and add your database connection string:
   ```
   DB_CONN=your_database_connection_string_here
   ```

5. Configure the import settings:
   Edit the `config.ini` file to set the folder path for your input files:
   ```ini
   [config]
   bases_folder_path = path/to/your/input/files
   ```

## 📘 Usage

1. Place your input files (Excel or HTML) in the configured `bases_folder_path`.

2. Run the main script:
   ```
   python app.py
   ```

3. The script will process all compatible files in the input folder and import the data into the specified database tables.

## 🛠️ Configuration

The project uses various configuration files to define import settings for different data sources:

- `config/adm.py`: Administrative data import settings
- `config/at_izo.py`: AT IZO data import settings
- `config/feedback.py`: Feedback data import settings
- `config/post.py`: Post data import settings
- `config/tec.py`: Technical data import settings
- `config/web_*.py`: Web-based data import settings for different categories

Each configuration file defines the database table, column mappings, and data types for the respective import process.

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.