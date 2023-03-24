FROM python:3 AS anand

# WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install influxdb
RUN pip3 install numpy
# Copy the application code into the container
COPY . .
# COPY read_fmt_OUT_INFLUX.py .
# # Set the default environment variables
# ENV PORT=8086

# # Expose the application port
# EXPOSE $PORT

FROM anand

CMD ["python3", "read_fmt_OUT_INFLUX.py"]
