# Create a new context within the browser with custom options
context = browser.newContext(
    storageState={'cookies': 'path/to/cookies.json'},  # Set the storage state
    extraHTTPHeaders={'Authorization': 'Bearer your-token'}  # Set additional HTTP headers
)
