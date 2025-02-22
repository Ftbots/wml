FROM mysterysd/wzmlx:latest
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
# Upgrade setuptools and install build dependencies
RUN pip3 install --upgrade setuptools
RUN apt-get update && apt-get install -y build-essential python3-dev
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .
CMD ["bash", "start.sh"]
