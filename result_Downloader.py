from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import pdfkit
import time

def fetch_results_and_save_as_pdf(roll_number, save_folder, wkhtmltopdf_path):
    # Create a new instance of the Firefox driver (you can use other drivers like Chrome)
    driver = webdriver.Firefox()

    try:
        # Open the webpage
        driver.get('http://14.139.202.226/20batchresult/')

        # Find the roll number input field by name
        roll_number_input = driver.find_element(By.NAME, 'enX')

        # Clear the existing value and enter the roll number
        roll_number_input.clear()
        roll_number_input.send_keys(roll_number)

        # Submit the form (you may need to adjust the form submission method)
        roll_number_input.send_keys(Keys.RETURN)

        # Give some time for the page to load (you may need to adjust this delay)
        time.sleep(5)

        # Check if the form submission was successful (you may need to adjust this check)
        if "404" not in driver.page_source:
            print(f'Form submitted successfully for roll number {roll_number}')

            # Capture the page content
            page_content = driver.page_source

            # Convert HTML content to PDF
            options = {
                'page-size': 'A4',
                'margin-top': '0mm',
                'margin-right': '0mm',
                'margin-bottom': '0mm',
                'margin-left': '0mm',
                'no-images': None,
                'disable-javascript': None,
            }

            # Specify the wkhtmltopdf path manually
            pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
            pdf_content = pdfkit.from_string(page_content, False, options=options, configuration=pdfkit_config)

            # Save the PDF to a file
            pdf_file_path = os.path.join(save_folder, f'result_{roll_number}.pdf')
            with open(pdf_file_path, 'wb') as pdf_file:
                pdf_file.write(pdf_content)

            print(f'PDF saved successfully for roll number {roll_number} at {pdf_file_path}')
        else:
            print(f'Failed to submit form for roll number {roll_number}. Page not found.')

    finally:
        # Close the browser window
        driver.quit()

# Create a folder to save downloaded PDFs
pdf_save_folder = 'downloaded_pdfs'
os.makedirs(pdf_save_folder, exist_ok=True)

# Specify the wkhtmltopdf path manually
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Use the correct path

# Read roll numbers from a text file in the same folder
roll_numbers_file_path = 'roll_no.txt'
with open(roll_numbers_file_path, 'r') as file:
    roll_numbers = file.read().splitlines()

# Iterate through roll numbers and fetch the results as PDFs
for roll_number in roll_numbers:
    fetch_results_and_save_as_pdf(roll_number, pdf_save_folder, wkhtmltopdf_path)
