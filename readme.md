# Sentiment Analysis API using FastAPI and Transformers

## How to Run

Follow these steps to set up and run the Sentiment Analysis API using FastAPI and Transformers.

### Prerequisites

1. Install [Python](https://www.python.org/) (version 3.8 or higher).
2. Install [Git](https://git-scm.com/).

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- [Transformers](https://huggingface.co/transformers/): A library by Hugging Face that provides general-purpose architectures for natural language understanding (NLU) and natural language generation (NLG) with pre-trained models.
- [Pydantic](https://pydantic-docs.helpmanual.io/): A data validation and settings management library for Python.


### Clone the Repository
- git clone https://github.com/raghav-singh-wizard/twitter_sent
- Install the requirements using pip install -r requirements.txt
- Then run uvicorn api:app --reload
- Then go to the  http://127.0.0.1:8000/docs to test with inputs