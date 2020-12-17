FROM jjanzic/docker-python3-opencv

MAINTAINER eric <er@iex.ec>

RUN apt-get update && apt-get install -y wget zip libgtk2.0

# Set the working directory to /app
WORKDIR /

# Install any needed packages
RUN pip install scikit-learn matplotlib

# Add program file and data management
COPY src/app.py /app.py

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
