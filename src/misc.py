import requests

def fetch_image(topic, api_key):
    # Construct the correct API URL
    api_url = f"https://api.pexels.com/v1/search?query={topic}&per_page=1"  # Replace with the correct endpoint for Pexels API
    headers = {
        'Authorization': f'Bearer {api_key}'  # Correctly format the API key in the headers
    }

    # Make the API request
    response = requests.get(api_url, headers=headers)

    # Debugging: print status code and response text
    print("Status Code:", response.status_code)  # Check the status code of the response
    print("Response Text:", response.text)       # Print the raw response text

    # Attempt to parse the JSON response
    try:
        data = response.json()
        print("JSON Data:", data)  # Optional: Print the parsed JSON data
    except requests.exceptions.JSONDecodeError:
        print("Error: Unable to decode JSON response. Response might be empty or malformed.")
        data = None  # Handle this case appropriately

    # Return the processed data
    return data

# Example call to fetch_image function
if __name__ == "__main__":
    topic = input("Enter the topic for image search: ")
    api_key = 'Yo7K8dSk4ORv09UsZGrHEXjzCZVVu1fyWjfRNFDDlsLcUlL8ct4gCiqI'  # Your actual API key
    fetch_image(topic, api_key)
