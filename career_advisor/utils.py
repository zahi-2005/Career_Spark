

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime

def get_timezone_info(location_name):
    geolocator = Nominatim(user_agent="career_advisor_app")
    location = geolocator.geocode(location_name)
    if not location:
        return None

    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
    if not timezone_str:
        return None

    tz = pytz.timezone(timezone_str)
    local_time = datetime.now(tz)
    return timezone_str, local_time.strftime('%Y-%m-%d %H:%M:%S')
