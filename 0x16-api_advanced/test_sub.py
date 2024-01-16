import requests
import sys

def number_of_subscribers(subreddit):
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-main.py <subreddit>")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

