from datetime import datetime

def format_time(process, start_time, end_time):
    print(f"{process} took {end_time - start_time:.2f} seconds.")

def get_current_time():
    return f"{datetime.now().time().hour}:{datetime.now().time().minute}"