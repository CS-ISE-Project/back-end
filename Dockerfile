# Making a parent image (lightweight Debian with Python installed)
FROM python:3.11-alpine

# Install build dependencies
RUN apk update --update-cache && \
    apk add --no-cache gcc build-base libpq rust cargo && \
    apk add --no-cache libffi-dev openssl-dev


# Create a directory into this operating system
WORKDIR /iseProject
COPY setup.py ./
COPY requirements.txt ./

RUN python -m pip install --upgrade pip && \
    python -m pip install multidict && \    
    python -m pip install -r requirements.txt



RUN python3 -m venv .venv



# Enabling the exposed port 

ENV NAME World

COPY . ./

EXPOSE 8000

# Starting the app inside the IMAGE
CMD . .venv/bin/activate; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

#CMD python3 -m uvicorn main:app --reload --port 4001
