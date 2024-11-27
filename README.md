# Data Analysis Project

This repository contains code and analysis for exploring disc golf flight numbers and their relationship to physical characteristics of a disc

## Project Overview

In this paper I consider the flying discs used in the sport of disc golf, specifically exploring the relationship between their physical characteristics and the way manufacturers market and classify these discs. Using technical specification and manufacturer data, I find strong correlations between the dimensions of a disc's rim to flight numbers.

See [flight_numbers.html](notebooks/02_presentation/flight_numbers.html) for full analysis.

## Project Structure

```
.
├── README.md
├── _quarto.yml
├── config.toml
├── requirements.txt
├── LICENSE
├── data
│   ├── interim
│   ├── processed
│   └── raw
├── docs
├── flight_numbers
│   ├── __init__.py
│   ├── get_data.py
│   ├── make_plots.py
│   └── train_models.py
└── notebooks
    ├── 01_exploration
    └── 02_presentation
```

## Setup Instructions

### Prerequisites

- Python 3.9+
- virtualenv

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/kevinhav/d607_final_project
cd d607_final_project
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

1. Update `CONFIG_PATH` in `get_data.py` to point to the `config.toml` file. This is a workaround until I can figure out how to get Quarto to play nice with local module imports.

## Usage

### Data Processing

1. Run `get_data()` from `make_data.py` to load the data as a Pandas dataframe
2. Optionally, write data locally to `/data/`

### Analysis & Modeling

1. Use functions in `train_models.py` to train models

## Contact

Kevin Havis - kevin.havis@gmail.com

## License

MIT Open Source - See [LICENSE](LICENSE)