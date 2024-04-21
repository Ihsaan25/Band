# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install any needed dependencies specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Run the Django development server on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
