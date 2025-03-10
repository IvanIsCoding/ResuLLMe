# Base image
FROM ubuntu:22.04

# Working directory, Streamlit does not work at root
WORKDIR /app

# Create logs directory
RUN mkdir -p /app/logs

# Copy the dependencies file to the working directory
COPY requirements.txt packages.txt /app/

# Install Python with a more robust approach to handle hash sum mismatches
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo 'Acquire::Retries "3";' > /etc/apt/apt.conf.d/80retries && \
    echo 'Acquire::http::Pipeline-Depth "0";' >> /etc/apt/apt.conf.d/80retries && \
    echo 'Acquire::CompressionTypes::Order:: "gz";' >> /etc/apt/apt.conf.d/80retries && \
    apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends python3-pip python-dev-is-python3 build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies with retry for pip
RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive xargs apt-get install -y --no-install-recommends < packages.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the current code to the 
COPY . .

# Set proper permissions for logs directory
RUN chmod 777 /app/logs

# Use PYTHONUNBUFFERED to ensure logs are sent to stdout
ENV PYTHONUNBUFFERED=1

# Run ResuLLMe with Streamlit
CMD [ "streamlit", "run", "src/Main.py" ]
