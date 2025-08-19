import webbrowser

# Get the default browser
browser = webbrowser.get()

# Open the page in the same tab (reuse the existing tab)
channel = 1  # Example channel
browser.open(f"http://127.0.0.1:5500/web_page/page{channel}.html", new=0)
