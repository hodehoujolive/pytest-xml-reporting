# GenerateXMLTestReport

## Description
This test automation project showcases the integration of pytest and Selenium to build a robust and scalable testing framework. It specifically focuses on utilizing the pytest-xml library to generate detailed test reports, providing comprehensive insights into test execution and results.
## Prerequisites
- Python 3.6 or higher installed on your system
- Homebrew (for macOS users)
- Latest version of WebDriver for the browser you want to use
- Git installed on your system

## Setup
1. Clone the repository using the following command:
    ```
    git clone https://github.com/hodehoujolive/GenerateXMLTestReport.git
    ```
2. Navigate to the cloned directory:
    ```
    cd GenerateXMLTestReport
    ```
3. Install pipenv using Homebrew:
    ```
    brew install pipenv
    ```
4. Create a Pipfile to track your project's dependencies:
    ```
    pipenv install --dev
    ```
    This will install the latest stable versions of Pytest and Selenium packages.

5. Install the latest version of WebDriver for the browser you want to use. You can download the WebDriver for the following commonly used browsers:
    - Firefox: GeckoDriver
    - Chrome: ChromeDriver
    - Opera: OperaDriver
    - Edge: Microsoft Edge WebDriver
    Make sure you have the correct version for your browser, otherwise it won't work.
    
6. To generate an XML report using pytest, you can use the pytest-xml plugin:
    ```
    pipenv install pytest-xml
    ```
    This plugin will generate an XML file containing the test results, which can be read by other tools for further analysis.

7. Run your pytest tests with the `--junitxml` flag to specify the path of the XML file where the results will be saved:
    ```
    pipenv run python -m pytest -v --junitxml="path/to/report.xml"
    ```
    This will generate an XML file containing the test results, which can be read by other tools for further analysis.
