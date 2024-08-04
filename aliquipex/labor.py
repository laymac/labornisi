import pyautogui

# Get the position and size of the window
window_x, window_y, window_width, window_height = pyautogui.getwindowgeometry(window_title)

# Take a screenshot of the window
screenshot = pyautogui.screenshot(region=(window_x, window_y, window_width, window_height))

# Save the screenshot as an image file
screenshot.save('window_screenshot.png')
