# Group-Results-Collector

### This Python program automates the retrieval and conversion of result pages into PDF format for a list of roll numbers from a specified webpage. It utilizes Selenium for web automation and pdfkit for HTML to PDF conversion.

### Requirements:
### - Python 3.x
### - Selenium
### - pdfkit
### - Firefox WebDriver (or other compatible drivers like Chrome WebDriver)
### - wkhtmltopdf

# Instructions for Use:
### 1. Ensure you have Python installed on your system.
### 2. Install the required Python packages using pip:
###     ```
###     pip install selenium pdfkit
###     ```
### 3. Download and install the Firefox WebDriver from Mozilla's GeckoDriver page and ensure it's in your system PATH, or specify the path to the WebDriver in the code.
### 4. Install wkhtmltopdf from wkhtmltopdf's website and ensure the path to the executable is correctly specified in the code.
### 5. Create a text file named `roll_no.txt` in the same directory as the script containing the roll numbers, each on a new line.
### 6. Run the Python script.

# How It Works:
### 1. The program reads a list of roll numbers from the `roll_no.txt` file.
### 2. It navigates to a specific webpage (`http://14.139.202.226/20batchresult/`) where results can be obtained.
### 3. For each roll number:
###     - Enters the roll number into the appropriate field.
###     - Submits the form.
###     - Captures the resulting page content.
###     - Converts the HTML content to PDF using wkhtmltopdf and saves it to a specified folder (`downloaded_pdfs`) with the naming convention `result_roll_number.pdf`.

# Notes:
### - Adjustments may be necessary for form submission methods, page loading delays, and form submission success checks depending on the specific website structure.
### - Ensure proper installation and configuration of dependencies for seamless execution.
### - This script assumes compatibility with Firefox WebDriver; adjustments might be necessary for other browsers.
### - Ensure the correct path to wkhtmltopdf executable is provided (`wkhtmltopdf_path`).
### - Customize the folder paths and WebDriver paths as per your system configuration.

### Feel free to reach out for any assistance or further clarification.
