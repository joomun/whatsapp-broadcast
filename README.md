# WhatsApp Broadcast Message Automation

## Main.py

`Main.py` is the main script that drives the automation process. It uses Selenium to interact with the WhatsApp Web interface and send messages to your recent chats.

### Usage

1. **Setup**:  
  Ensure you have met all the prerequisites mentioned above.

2. **Configuration**:  
  Define your message and other configurations in the script.

3. **Run the Script**:  
  Execute the script using Python:
  ```bash
  python Main.py
  ```

### Code Overview

- **Initialization**:  
  The script initializes the Selenium WebDriver and navigates to WhatsApp Web.

- **Login**:  
  You will need to scan the QR code with your phone to log in.

- **Message Sending**:  
  The script iterates through your recent chats and sends the predefined message.

- **Scrolling**:  
  It handles scrolling to ensure all chats are processed.

### Example

Here's an example of how to define your message in the script:
```python
message = "Hello! This is a broadcast message."
```

### Notes

- Ensure your browser (Microsoft Edge) is up to date.
- The script may need adjustments based on changes to the WhatsApp Web interface.

### Contributing

If you would like to contribute to this project, please request contributor access. Once granted, you can update the code and submit pull requests.

### Maintenance

Please note that the script may require updates if the WhatsApp Web interface changes. Ensure to check for any updates to the web interface and adjust the script accordingly.

This project is a Python script to automate sending broadcast messages to all your recent WhatsApp chats using Selenium and a web browser (Microsoft Edge). It iteratively sends a predefined message to each chat and handles scrolling through the chat list to include all chats.
