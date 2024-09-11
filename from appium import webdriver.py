from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
import time

# Desired capabilities
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11.0",  # Replace with your Android version
    "deviceName": "Android Emulator",  # Replace with your device name
    "app": "/path/to/your/app.apk",  # Replace with the path to your .apk file
    "appPackage": "com.example.myapp",  # Replace with your app's package name
    "appActivity": "com.example.myapp.MainActivity",  # Replace with your app's main activity
    "automationName": "UiAutomator2"  # Required for Android
}

# Create WebDriver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
# Get memory usage
memory_usage = driver.get_performance_data("com.example.myapp", "memoryinfo", 5)
print("Memory Usage:", memory_usage)

# Get CPU usage
cpu_usage = driver.get_performance_data("com.example.myapp", "cpuinfo", 5)
print("CPU Usage:", cpu_usage)

# Get network usage
network_usage = driver.get_performance_data("com.example.myapp", "networkinfo", 5)
print("Network Usage:", network_usage)

try:
    # Wait for the app to load
    time.sleep(5)

    # Example: Find an element by its ID and click on it
    element = driver.find_element(AppiumBy.ID, "com.example.myapp:id/button_id")
    element.click()

    # Example: Find a text input field and enter text
    text_field = driver.find_element(AppiumBy.ID, "com.example.myapp:id/text_field_id")
    text_field.send_keys("Hello, Appium!")

    # Example: Press Enter key (if needed)
    text_field.send_keys(Keys.ENTER)

    # Add more actions as needed...

finally:
    # Quit the driver
    driver.quit()
