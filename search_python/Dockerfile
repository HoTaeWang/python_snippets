# Base Image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents in the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
