import re


def parse_chat(file_name: str) -> list:
    """
    Parse WhatsApp chat text into a list of dictionaries with date, time, sender, and message-text.
    Skips system messages (messages without a sender).

    Args:
        chat_text (str): The raw WhatsApp chat text

    Returns:
        list: List of dictionaries, each containing message details
    """
    # Split the chat into lines
    with open(file_name, encoding='utf-8') as file:
        messages = []

        # Regular expression to match message pattern with a sender
        # Captures: date, time, sender, and message text
        message_regex = r'^(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2} [AP]M) - ([^:]+): (.+)$'
        lines = file.readlines()
        for line in lines:
            line = line[:-1]
            match = re.match(message_regex, line)
            if match:
                # Only process messages that have a sender (non-system messages)
                date, time, sender, message_text = match.groups()
                messages.append({
                    'date': date,
                    'time': time,
                    'sender': sender.strip(),
                    'message-text': message_text
                })

    return messages
