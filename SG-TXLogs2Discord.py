import time
import requests

# Configuration
log_file_path = '/yourserverlocation/txData/default/logs/fxserver.log'
discord_webhook_url = 'https://discord.com/api/webhooks/example'

def send_to_discord(message):
    data = {
        'content': message
    }
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code != 204:
        print(f'Error sending message to Discord: {response.status_code}, {response.text}')
    else:
        print(f'Message sent: {message}')

def tail_log(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Go to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly
                continue
            print(f'New log entry: {line.strip()}')
            send_to_discord(line.strip())

if __name__ == '__main__':
    print('Starting log monitoring...')
    tail_log(log_file_path)
