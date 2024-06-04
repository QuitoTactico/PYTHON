from math import floor

def format_duration(seconds):
    if not seconds:
        return 'now'

    minutes = floor(seconds/60)
    seconds = seconds%60

    hours = floor(minutes/60)
    minutes = minutes%60
    
    days = floor(hours/24)
    hours = hours%24
    
    years = floor(days/365)
    days = days%365

    # -----------------------------------------------------------

    seconds_plural = '' if seconds == 1 else 's'
    seconds_str = f'{seconds} second{seconds_plural}' if seconds != 0 else ''

    minutes_plural = '' if minutes == 1 else 's'
    minutes_str = f'{minutes} minute{minutes_plural}' if minutes != 0 else ''

    hours_plural = '' if hours == 1 else 's'
    hours_str = f'{hours} hour{hours_plural}' if hours != 0 else ''

    days_plural = '' if days == 1 else 's'
    days_str = f'{days} day{days_plural}' if days != 0 else ''

    years_plural = '' if years == 1 else 's'
    years_str = f'{years} year{years_plural}' if years != 0 else ''

    complete_str = ', '.join([time for time in [years_str, days_str, hours_str, minutes_str, seconds_str] if time != ''])

    last_comma = complete_str.rfind(',')
    if last_comma != -1:
        complete_str = f'{complete_str[:last_comma]} and{complete_str[last_comma+1:]}'

    #return f'{years}, {days}, {hours}, {minutes}, {seconds}'
    #return f'{years_str}{days_str}{hours_str}{minutes_str}{seconds_str}'
    return complete_str


print(format_duration(242062374))
print(format_duration(242062374-53))
print(format_duration(242062374-54))

    