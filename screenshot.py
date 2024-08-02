import pyscreenshot as ImageGrab

# Capture the full screen
screenshot = ImageGrab.grab()

# Save the image file
screenshot.save("screenshot.png")

print("Screenshot saved as screenshot.png")
