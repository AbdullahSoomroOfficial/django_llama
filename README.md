# Django Llama Project

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. Clone the repository

```bash
git clone <repository-url>
cd django_llama
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
```

3. Install required packages

```bash
pip install -r requirements.txt
```

### Running the Project

1. Apply database migrations

```bash
python manage.py migrate
```

2. Start the development server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/chat`
