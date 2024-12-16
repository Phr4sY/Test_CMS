import requests

# WordPress REST API credentials
WORDPRESS_URL = "http://wordpress/wp-json/wp/v2/posts"
JWT_AUTH_URL = "http://wordpress/wp-json/jwt-auth/v1/token"

USERNAME = "admin"  # Replace with your WordPress username
PASSWORD = "admin"  # Replace with your WordPress password

def get_jwt_token():
    """
    Obtain a JWT token using the username and password.
    """
    data = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(JWT_AUTH_URL, json=data)

    if response.status_code == 200:
        token = response.json().get("token")
        print("JWT Token obtained successfully!")
        return token
    else:
        print(f"Failed to obtain JWT token: {response.status_code} - {response.text}")
        return None


def create_post(title, content):
    """
    Create a new post using the JWT token for authentication.
    """
    # Get the JWT token
    token = get_jwt_token()
    if not token:
        print("Cannot proceed without a valid JWT token.")
        return

    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "title": title,
        "content": content,
        "status": "publish"  # Set to "publish" to make it live immediately
    }

    response = requests.post(WORDPRESS_URL, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Post '{title}' created successfully!")
    else:
        print(f"Failed to create post: {response.status_code} - {response.text}")