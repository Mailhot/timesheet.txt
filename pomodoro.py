import argparse
import time
import sys




# define the countdown func.
def countdown(minutes):
    # countdown of t minutes
    t = minutes * 60
    while t:
        # question = input('>>')
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")

        time.sleep(1)
        t -= 1
      
    print('\007')
    print('Finished')

def main():

    # Create the parser
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('-s', '--start', action='store_true', help='Start the timer [25 minutes]')
    parser.add_argument('-b', '--break_', action='store_true', help='Start a break [5 minutes]')


    parser.add_argument('-t', '--time', type=int, help='Time value for pomodoro timer in minutes. [25]')

    # Parse the argument
    args = parser.parse_args()
    
    if args.time:

        time_delay = args.time
    else:
        if args.start:
            time_delay = 25
        elif args.break_:
            time_delay = 5

    countdown(time_delay)





if __name__ == "__main__":
    main()
