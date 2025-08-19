# Python script to generate 1000 pages and the index.html page with links

# Create individual pages (page1.html to page1000.html)
for i in range(1, 1001):
    page_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page {i}</title>
    </head>
    <body>
        <h1>Welcome to Page {i}</h1>
        <p>This is the content of Page {i}.</p>
        <a href="index.html">Go back to Index Page</a>
    </body>
    </html>
    """
    with open(f'page{i}.html', 'w') as file:
        file.write(page_content)

# Create the index.html page with links to all 1000 pages
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index Page</title>
</head>
<body>
    <h1>Welcome to the Index Page</h1>
    <p>Click any of the links below to open a page:</p>
    <ul>
"""

# Add links to all pages (page1.html to page1000.html)
for i in range(1, 1001):
    html_content += f'        <li><a href="page{i}.html">Page {i}</a></li>\n'

# Close the HTML tags
html_content += """
    </ul>
</body>
</html>
"""

# Write the index.html page to a file
with open("index.html", "w") as file:
    file.write(html_content)

print("All pages and index.html generated successfully.")
