# Following imports from https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/9
from gpiozero import Button
import time
import math
import bme280_sensor
import wind_direction_byo
import statistics
import ds18b20_therm

# Imports from mcap: https://mcap.dev/guides/python/json
from mcap.mcap0.writer import Writer
from mcap.mcap0.well_known import SchemaEncoding, MessageEncoding

def main():
  print("Testing")
# weather_data = []

# with open(args.output, "wb") as f:
#   writer = Writer(f)
#   writer.start()


  
#   schema_id = writer.register_schema(
#     name="weather",
#     encoding=SchemaEncoding.JSONSchema,
#     data=weather_data,
#   )
#   channel_id = writer.register_channel(
#     topic="weather_stuff",
#     message_encoding=MessageEncoding.JSON,
#     schema_id=schema_id,
#   )

#   pointcloud["timestamp"] = {
#       "sec": int(base_timestamp.timestamp()),
#       "nsec": base_timestamp.microsecond * 1000,
#   }
  
#   writer.add_message(
#       channel_id,
#       log_time=int(base_timestamp.timestamp() * 1e9),
#       data=json.dumps(pointcloud).encode("utf-8"),
#       publish_time=int(base_timestamp.timestamp() * 1e9),
#   )
#   writer.finish()
