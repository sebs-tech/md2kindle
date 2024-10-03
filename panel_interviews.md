To convert an HTML file with an external CSS file into a PDF using Python, you can use a library called **`pdfkit`**, which is a Python wrapper for **wkhtmltopdf**. This tool allows you to generate PDF files from HTML documents while preserving styles from the linked CSS.

Here’s a step-by-step guide on how to do this:

### Step 1: Install the Required Tools



### Step 2: Write the Python Script

Once the necessary tools are installed, you can use the following Python script to convert an HTML file with an external CSS file into a PDF:

~~~python
import pdfkit

# Path to your HTML file and CSS file
html_file = 'example.html'
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
~~~

### Step 3: Prepare Your HTML and CSS

Ensure that your HTML and CSS files are in the same directory or provide absolute paths to the files. Here's an example structure:

- `example.html`
- `style.css`
- `convert_to_pdf.py`

For example, `example.html` could look like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello, PDF!</h1>
    <p>This is an example of converting HTML with CSS into a PDF using Python.</p>
</body>
</html>
```

And `style.css` could look like this:

```css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 20px;
}

h1 {
    color: #2c3e50;
}
```

### Step 4: Run the Python Script

After preparing the HTML, CSS, and Python script, run the script:

```bash
python convert_to_pdf.py
```

This will generate `output.pdf` with the styles from `style.css` applied to the HTML content.

### Step 5: View the PDF

Once the script runs successfully, you should find `output.pdf` in the same directory. You can open it using any PDF viewer to check the result.

### Optional: Convert HTML from URL or String

If you want to convert HTML content from a URL or string instead of a file, you can use the following methods:

1. **Convert HTML from URL**:
   ```python
   pdfkit.from_url('https://example.com', 'output.pdf')
   ```

2. **Convert HTML from String**:
   ```python
   html_string = """
   <html><head><link rel="stylesheet" href="style.css"></head>
   <body><h1>Test</h1><p>This is a test</p></body></html>
   """
   pdfkit.from_string(html_string, 'output.pdf', css='style.css')
   ```

With this approach, you can easily convert HTML files with CSS styling into PDF using Python.