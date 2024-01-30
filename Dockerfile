# Use Python 3.10 as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add current directory code to /app in container
ADD . /app


RUN pip install pipenv
RUN pipenv install --system --deploy --dev

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
ENTRYPOINT ["flask", "run" , "--host=0.0.0.0"]