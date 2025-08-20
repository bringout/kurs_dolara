# kurs_dolara

[![PyPI version](https://badge.fury.io/py/kurs-dolara.svg)](https://badge.fury.io/py/kurs-dolara)

A simple TUI application to check the current USD exchange rate from the Central Bank of Bosnia and Herzegovina.

## Screenshot

![Application Screenshot](app_screenshot.png)

## Installation

```bash
pip install kurs_dolara
```

## Usage

```bash
kurs_dolara
```

## Development

This project uses `rye` for project management.

1. Install `rye`:
   ```bash
   curl -sSf https://rye-up.com/get | bash
   ```
2. Install dependencies:
   ```bash
   rye sync
   ```
3. Run the application:
   ```bash
   rye run kurs_dolara
   ```
4. Run tests:
   ```bash
   rye test
   ```