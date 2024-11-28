import requests

# Define the URL and headers for the request
url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"

# The username or email to initiate the password reset
email_or_username = "instagram"  # Replace with the email or username you want to recover

# Your session cookies (you need to have valid cookies from your browser session)
cookies = {
    'csrftoken': '4QiC-CbnuXCqrH_8gnCUI8',  # Replace with your CSRF token
    'datr': 'UCo4Z4eoMz66aC0r4ocsO23j',  # Replace with your datr cookie value
    'ig_did': 'F222BCA4-0796-41CF-94E9-0BA4D7ECB8E2',  # Replace with your device ID
    'mid': 'ZzgqUAALAAHASXbAZduQfHCtt2TT',  # Replace with your session ID
    'dpr': '1.25',  # Device pixel ratio (may need to adjust based on your screen resolution)
    'wd': '767x730'  # Window size (adjust if necessary)
}

# Define the headers (you can also extract some of these from your browser's dev tools)
headers = {
    'X-Ig-App-Id': '936619743392459',  # Instagram app ID (static value for web requests)
    'X-Instagram-Ajax': '1018258462',  # Instagram AJAX request identifier
    'X-Csrftoken': cookies['csrftoken'],  # CSRF token
    'X-Web-Device-Id': cookies['ig_did'],  # Device ID
    'X-Asbd-Id': '129477',  # Instagram's Asbd ID
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com/accounts/password/reset/?source=fxcal&hl=en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Ch-Ua': 'Not?A_Brand;v="99", "Chromium";v="130"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
}

# Define the payload with the username or email and the flow identifier
payload = {
    'email_or_username': email_or_username,
    'flow': 'fxcal'  # Flow identifier, could be related to a specific recovery method
}

# Make the POST request
response = requests.post(url, headers=headers, cookies=cookies, data=payload)

# Check the response status and content
if response.status_code == 200:
    print("Password reset request successfully sent!")
    print("Response:", response.json())  # Display response content (JSON)
else:
    print(f"Failed to send password reset request. Status code: {response.status_code}")
    print("Response:", response.text)
