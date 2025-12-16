from datetime import datetime
import pytz
def find_timezone():
    local_time = datetime.now()
    
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)

        current_time_in_tz = datetime.now(timezone)

        if local_time.strftime('%Y-%m-%d %H:%M') == current_time_in_tz.strftime('%Y-%m-%d %H:%M'):
            return f"Your device is likely in the '{tz} timezone."
    
    return "Could not determine the timezone."
 
your_current_time_zone = find_timezone()
print(your_current_time_zone)