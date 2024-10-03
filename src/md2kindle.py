import markdown

# Define the path to your CSS file
css_file = "style.css"

# Read the markdown file
with open("panel_interviews.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content)

# Add the external CSS link to the HTML
html_with_css = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to HTML</title>
    <link rel="stylesheet" href="{css_file}">
</head>
<body>
    {html_content}
</body>
</html>
"""

# Save the output as an HTML file
with open("output_with_css.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_with_css)

print("Markdown has been converted to HTML with external CSS and saved as output_with_css.html")