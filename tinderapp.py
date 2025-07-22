 #LOGGING
import logging
import time

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='a')

try:
    year = int(input("Date Of Birth (Year): "))   
    if 2025 - year < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Welcome to Tinder Dating App! Searching matches😅.........." )
        time.sleep(4)
        print("Meet Shannice, a 20-year-old from New York. She loves hiking and photography.")

except Exception as e:
    logging.error("An error occurred: %s", e)
    print("An error occurred. Please try again Later.")
    
