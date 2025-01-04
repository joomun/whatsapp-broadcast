from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# New Year message
message = "🎉 Happy New Year! 🎊\nWishing you health, happiness, and success in the coming year! 🥳"

# Path to Edge WebDriver
edge_driver_path = r"C:\Users\joomu\Downloads\edgedriver_win64\msedgedriver.exe"

# Set up the Edge WebDriver using Service
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://web.whatsapp.com")
print("Please scan the QR code to log in to WhatsApp Web.")

# Wait for manual login
input("Press Enter after scanning the QR code...")

def send_to_all_chats():
    chats = driver.find_elements(By.XPATH, '//div[contains(@data-testid, "cell-frame-container")]')
    print(f"Found {len(chats)} chats to process.")
    for chat in chats:
        try:
            # Click on the chat
            chat.click()
            time.sleep(1)  # Wait for the chat to open
            
            # Type and send the message
            message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
            message_box.click()
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)
            print("Message sent to chat")
            
            time.sleep(1)  # Short pause before moving to the next chat
        except Exception as e:
            print(f"Error sending message: {e}")


# Scroll and send messages to all chats
while True:
    send_to_all_chats()
    try:
        # Scroll down to load more chats
        chat_list = driver.find_element(By.XPATH, '//div[@role="region"]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", chat_list)
        time.sleep(2)  # Wait for chats to load
    except Exception as e:
        print("All chats processed or no more chats to load.")
        break


