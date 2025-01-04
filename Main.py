# Developed Date: 2025/01/04
# Version: 1.0
# Author: Joomun Muddathir

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

# New Year message (replace emojis with plain text)
message = (
    "Happy New Year! 🎉🎊\nWishing you health, happiness, and success in the coming year! 🥳\n"
    "This is a broadcast message I just created. If you are in my recent chat, I think we had "
    "something or some moments we created for this year 2024.\nIf not, we say hello again in 2025."
)

# Remove unsupported emojis from the message
def clean_message(text):
    # Regex to remove non-BMP characters (e.g., emojis)
    return re.sub(r"[^\u0000-\uFFFF]", "", text)

cleaned_message = clean_message(message)

# Path to Edge WebDriver
edge_driver_path = r"C:\Users\joomu\Downloads\edgedriver_win64\msedgedriver.exe"

# Set up the Edge WebDriver using Service
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Please scan the QR code to log in to WhatsApp Web.")

# Wait for manual login
input("Press Enter after scanning the QR code...")

# Function to send a message to a chat
def send_message():
    try:
        # Locate the message input box
        message_box = driver.find_element(By.XPATH, '//p[@class="selectable-text copyable-text x15bjb6t x1n2onr6"]')
        message_box.click()
        message_box.send_keys(cleaned_message)
        print("Message typed.")
        
        # Locate and click the send button
        send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send"]')
        send_button.click()
        print("Message sent.")
    except Exception as e:
        print(f"Error sending message: {e}")

# Function to load and send messages to all chats
def send_to_all_chats():
    processed_chats = set()  # Keep track of chats already processed
    last_scroll_position = 0

    while True:
        # Find all visible chats
        chats = driver.find_elements(By.XPATH, '//div[@role="listitem"]')
        print(f"Found {len(chats)} visible chats.")

        for chat in chats:
            try:
                chat_id = chat.get_attribute("data-id")  # Unique identifier for chats
                if chat_id in processed_chats:
                    continue  # Skip already processed chats

                chat.click()  # Open the chat
                time.sleep(2)  # Wait for the chat to load
                
                send_message()  # Send the message
                processed_chats.add(chat_id)  # Mark chat as processed
                time.sleep(1)  # Short pause before moving to the next chat
            except Exception as e:
                print(f"Error processing chat: {e}")

        # Scroll to load more chats
        chat_list = driver.find_element(By.XPATH, '//div[@role="region"]')
        driver.execute_script("arguments[0].scrollTop += 500", chat_list)
        time.sleep(2)  # Wait for chats to load

        # Check if scrolling has reached the end
        current_scroll_position = driver.execute_script("return arguments[0].scrollTop", chat_list)
        if current_scroll_position == last_scroll_position:
            print("Reached the end of the chat list.")
            break
        last_scroll_position = current_scroll_position

# Start sending messages
send_to_all_chats()

# Close the browser
driver.quit()
