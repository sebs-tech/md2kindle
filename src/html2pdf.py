import pdfkit

# Path to your HTML file and CSS file
html_file = 'output_with_css.html'
css_file = 'style.css'
output_pdf = 'output.pdf'

# Define options for wkhtmltopdf
options = {
    'encoding': 'UTF-8',  # Set character encoding
    'no-outline': None,   # Disable outline in the PDF
    'enable-local-file-access': None  # Enable local file access for CSS
}

# Convert HTML file to PDF with CSS
pdfkit.from_file(html_file, output_pdf, options=options, css=css_file)

print(f'HTML with CSS has been converted to {output_pdf}')
