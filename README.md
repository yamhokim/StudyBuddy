# Study Buddy

A real-time chat application built with Django, designed to function similarly to Discord, allowing users to communicate through chat rooms in real-time.

## Features

- User authentication (Sign up, Login, Logout)
- Real-time messaging using WebSockets
- Multiple chat rooms where users can join and chat
- Responsive UI for both desktop and mobile

## Tech Stack

- **Backend**: Django, Django Channels (WebSockets)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (can be replaced with PostgreSQL for production)
- **WebSocket**: Powered by Django Channels
- **Other Tools**: Redis (for WebSocket management)

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Redis (for WebSockets)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-chat-platform.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the Redis server:

    ```bash
    redis-server
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and visit `http://127.0.0.1:8000/` to access the chat platform.
