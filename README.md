# EdTech Web App Test Automation

This project contains automated UI tests for the EdTech web application using Selenium WebDriver and pytest.

## Features

- Cross-browser testing support (Chrome, Firefox, Edge, Safari)
- Headless mode support for faster test execution (except Safari)
- Page Object Model (POM) design pattern for maintainable and reusable test code
- Explicit waits using Selenium’s `WebDriverWait` and expected conditions
- Generates HTML test reports with pytest-html

## Prerequisites

- Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari browser installed
- `pip` package manager

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/edtech-webapp-automation.git
   cd edtech-webapp-automation
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

## Running Tests

Run tests on the default Chrome browser and generate an HTML report:
```bash
    pytest -v --html=Reports/report.html

