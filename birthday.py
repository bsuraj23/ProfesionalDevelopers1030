from datetime import datetime

# Enter your birthday here (YYYY, MM, DD)
birthday = datetime(2003, 3, 30)

# Get today's date
today = datetime.today()

# Find the difference
difference = today - birthday

print("Days from your birthday:", difference.days)

from datetime import datetime

# ENTER your birthday and time here
# format: datetime(YYYY, MM, DD, HH, MM, SS)
birthday = datetime(2003, 3, 30, 10, 15, 0)   # Example: 21 May 2000, 10:30 AM

# Current date and time
now = datetime.now()

# Difference
diff = now - birthday

# Total seconds
total_seconds = diff.total_seconds()

# Convert
days = diff.days
hours = int((total_seconds // 3600) % 24)
minutes = int((total_seconds // 60) % 60)
seconds = int(total_seconds % 60)

print("It's been:")
print(f"{days} days")
print(f"{hours} hours")
print(f"{minutes} minutes")
print(f"{seconds} seconds")

