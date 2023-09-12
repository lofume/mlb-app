# mlb-app

This is a Django web application that displays MLB standings data retrieved from an API.

## Prerequisites

Before you can run this project locally, make sure you have the following installed:

- Python 3.x: You can download it from [python.org](https://www.python.org/downloads/).

## Getting Started

Follow these steps to set up and run the project locally:

1. Clone the repository to your local machine:
git clone [GET CLONE LINK]

2. Navigate to the project directory:
cd mlb-project

3. Create a virtual environment (recommended) to manage project dependencies:
python -m venv venv

4. Activate the virtual environment:

  On Windows:
    venv\Scripts\activate

  On macOS and Linux:
    source venv/bin/activate

5. Install project dependencies:
pip install -r requirements.txt


6. Set up the database:
python manage.py migrate

7. Run the development server:
python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/.
