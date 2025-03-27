import os

# Folder containing the PDFs
docs_folder = "docs"

# Start the HTML structure
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>My PDF Collection</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        a { color: #1a73e8; text-decoration: none; font-size: 18px; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Welcome to My PDF Collection</h1>
    <ul>
"""

# Loop through the files in the "docs" folder
for filename in os.listdir(docs_folder):
    if filename.endswith(".pdf"):  # Only include PDF files
        link = f"{docs_folder}/{filename}"
        html_content += f'        <li><a href="{link}" target="_blank">{filename}</a></li>\n'

# End the HTML structure
html_content += """       </ul>
</body>
</html>
"""

# Write the HTML to a file
with open("index.html", "w") as html_file:
    html_file.write(html_content)

print("index.html updated with links to PDFs in 'docs/' folder.")
