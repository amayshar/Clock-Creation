import datetime
import time
import sys

def set_alarm():
    print("--- Python Alarm Clock ---")
    
    # 1. Get a valid alarm time from the user
    while True:
        user_input = input("Enter alarm time in 24-hour format (HH:MM or HH:MM:SS): ").strip()
        
        # Normalize input to HH:MM:SS if user only typed HH:MM
        if len(user_input) == 5:
            user_input += ":00"
            
        try:
            # Validate format
            datetime.datetime.strptime(user_input, "%H:%M:%S")
            alarm_time = user_input
            break
        except ValueError:
            print("❌ Invalid time format! Please use HH:MM:SS (e.g., 07:30:00 or 14:15).")

    print(f"\n🔔 Alarm successfully set for {alarm_time}")
    print("⏰ Clock is running... Press Ctrl+C to cancel.")
    
    # 2. Main clock loop
    try:
        while True:
            # Get current system time formatted as HH:MM:SS
            now = datetime.datetime.now().strftime("%H:%M:%S")
            
            # Print a live ticking clock status in the console
            sys.stdout.write(f"\rCurrent Time: {now}")
            sys.stdout.flush()
            
            # 3. Check if current time matches the alarm time
            if now == alarm_time:
                print("\n\n🚨 WAKE UP! Time's up! 🚨")
                
                # Ring the alarm sound 5 times
                for _ in range(5):
                    sys.stdout.write("\a") # Trigger system alert bell
                    sys.stdout.flush()
                    time.sleep(1)
                break
                
            time.sleep(1) # Wait 1 second before checking again
            
    except KeyboardInterrupt:
        print("\n\n🛑 Alarm cancelled by user. Goodbye!")

if __name__ == "__main__":
    set_alarm()
