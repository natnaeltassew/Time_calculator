⏱️ Time Calculator – Python Solution

This project contains a Python function that adds a duration to a starting time and returns the new time, including the correct AM/PM format, day of the week (optional), and days passed.
It follows the requirements of the FreeCodeCamp Time Calculator challenge.


---

🚀 Features

Accepts a start time in 12-hour format (AM/PM)

Adds a duration in hours:minutes format

Correctly handles:

Minute overflow (e.g., 50 + 20 → +1 hour)

Hour overflow (switching AM/PM)

Passing over midnight

Multiple days later

Optional day-of-week calculation


Returns a clean, readable formatted result.



---

📂 File Included

time_calculator.py – Contains the implementation and sample test calls.



---

🧠 Example Outputs

add_time("3:54 PM", "4:20")
# Output: "8:14 PM"

add_time("11:59 PM", "24:05")
# Output: "12:04 AM (2 days later)"

add_time("3:30 PM", "2:12", "Monday")
# Output: "5:42 PM, Monday"

add_time("10:10 PM", "3:30")
# Output: "1:40 AM (next day)"


---

🛠️ How to Use

1. Clone the repository:



git clone https://github.com/natnaeltassew/time_calculator.git

2. Run the file:



python time_calculator.py

3. Modify the test cases to try your own values.




---

📘 Function Description

add_time(start, duration, day=None)

Parameters:

Parameter	Type	Description

start	string	Starting time (e.g., "3:00 PM")
duration	string	Duration to add (e.g., "2:30")
day (optional)	string	Day of the week (e.g., "Monday")


Returns:

A formatted string containing the new time, the new day (if provided), and day count if changed.


---

📅 Day Handling

Handles all days of the week

Correctly wraps around after Sunday

Adds tags like:

(next day)

(2 days later)

(N days later)




---

📜 Requirements

Python 3.6 or above



---

🤝 Contributing

Pull requests and improvements are welcome.
Open an issue if you'd like to discuss changes.


---

📄 License

This project is open-source and free to use.
