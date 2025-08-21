# Gemini Code Assistant Context

## Project Overview

This project is a simple Python Textual CLI/TUI application called `kurs-dolara`. Its purpose is to fetch and display the current USD exchange rate from the Central Bank of Bosnia and Herzegovina. The application uses the `requests` library to fetch the data and `textual` to build the TUI.

## Building and Running

The project is managed using `rye`. The main application logic is in `src/kurs_dolara/main.py`.

### Installation

```bash
pip install kurs-dolara
```

### Running the Application

```bash
kurs_dolara
```

### Command-line Options

*   `--light`: Use a light theme for the application.
*   `--version`: Show the version of the application.
*   `--cli`: Display the rate in the console and exit.

### Development

To run the application in a development environment:

1.  Install dependencies:
    ```bash
    rye sync
    ```
2.  Run the application:
    ```bash
    rye run kurs_dolara
    ```

### Testing

Tests are run using `pytest`:

```bash
rye test
```

## Development Conventions

*   **Project Management:** The project uses `rye` for dependency management and running scripts.
*   **Testing:** The project uses `pytest` for testing. The test workflow is defined in `.github/workflows/test.yml` and is triggered on every push to the `master` branch.
*   **Publishing:** The project is published to PyPI using a GitHub Actions workflow defined in `.github/workflows/publish.yml`. The workflow is triggered on every push of a tag with the format `v*.*.*`.
