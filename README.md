# kurs_dolara

A simple TUI application to check the current USD exchange rate from the Central Bank of Bosnia and Herzegovina.

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