import argparse
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Default file path
DEFAULT_FILE_PATH = '/Users/ejoliet/Downloads/file.fits'
# Parse command-line arguments
parser = argparse.ArgumentParser(description="Drag and drop file upload using Selenium")
parser.add_argument("file_path",nargs='?',default=DEFAULT_FILE_PATH, help="The path to the file to be uploaded")
args = parser.parse_args()

options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Initialize the WebDriver
driver = webdriver.Chrome(options)

try:
    # Open the target web page
    driver.get("https://irsa.ipac.caltech.edu/irsaviewer/?__action=layout.showDropDown&view=FileUploadDropDownCmd")

    # Allow the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "drop-down"))
    )

    # Locate the file input element if available
    file_input = driver.find_element(By.ID, "upload-file")

    # # Path to the local file to be uploaded
    # file_path = '/Users/ejoliet/Downloads/file.fits'

    # Set the file path to the input element
    file_input.send_keys(args.file_path)

    # Simulate drag-and-drop if necessary (e.g., if there are additional steps required after selecting the file)
    drop_area = driver.find_element(By.ID, "drop-down")
    driver.execute_script("""
        var dropArea = arguments[0];
        var fileInput = arguments[1];
        var file = fileInput.files[0];

        var dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);

        var dragStartEvent = new DragEvent('dragstart', {
            dataTransfer: dataTransfer
        });
        var dropEvent = new DragEvent('drop', {
            dataTransfer: dataTransfer
        });
        var dragEndEvent = new DragEvent('dragend', {
            dataTransfer: dataTransfer
        });

        dropArea.dispatchEvent(dragStartEvent);
        dropArea.dispatchEvent(dropEvent);
        dropArea.dispatchEvent(dragEndEvent);
    """, drop_area, file_input)

    # Keep the browser open
    print("The browser will remain open. Close it manually to end the session.")

    main_window_handle = driver.current_window_handle

    while True:
        if main_window_handle not in driver.window_handles:
            print("The tab was closed.")
            break
        time.sleep(1)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Optionally handle any cleanup if needed
    pass