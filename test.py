from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pdfkit
import time

def convert_html_to_pdf(url, save_folder, wkhtmltopdf_path):
    # Create a new instance of the Firefox driver (you can use other drivers like Chrome)
    driver = webdriver.Chrome()

    try:
        # Open the webpage
        driver.get(url)

        # Give some time for the page to load (you may need to adjust this delay)
        time.sleep(5)

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
        pdf_file_path = os.path.join(save_folder, 'result.pdf')
        with open(pdf_file_path, 'wb') as pdf_file:
            pdf_file.write(pdf_content)

        print(f'PDF saved successfully at {pdf_file_path}')

    finally:
        # Close the browser window
        driver.quit()

# Create a folder to save the downloaded PDF
pdf_save_folder = 'downloaded_pdfs'
os.makedirs(pdf_save_folder, exist_ok=True)

# Specify the wkhtmltopdf path manually
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Use the correct path

# URL of the webpage to convert to PDF
url_to_convert = 'https://github.com/vinayiet'

# Call the function to convert HTML to PDF
convert_html_to_pdf(url_to_convert, pdf_save_folder, wkhtmltopdf_path)
