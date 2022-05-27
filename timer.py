import time

def timer(minutes, seconds):
    total = 60 * minutes + seconds
    current = 0
    while current != total:
        time.sleep(1)
        current += 1
        time_left = total - current
        minutes = time_left // 60
        seconds = time_left - 60 * minutes
        print(minutes, "minutes left and", seconds, "seconds left")
        
        
timer(3, 0)
