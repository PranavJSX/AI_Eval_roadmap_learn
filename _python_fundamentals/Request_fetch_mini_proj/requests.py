import httpx


def fetch_data(url):
    """
    Fetch data from the given URL using an HTTP GET request.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        dict: The JSON response from the server if the request is successful.
        None: If the request fails or the response is not JSON.
    """
    try:
        response = httpx.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  # Return the JSON content of the response
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {url}: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except ValueError:
        print("Response content is not valid JSON.")

    return None
