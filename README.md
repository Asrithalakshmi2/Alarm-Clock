# Simple Python Alarm Clock

A graphical alarm clock application built using Python's Tkinter library. This alarm clock allows users to set an alarm time, choose a custom alarm tone (MP3 or WAV), and snooze the alarm for a short period.

## Features

* **Set Alarm Time**: Easily set an alarm using a `HH:MM:SS` format.
* **Custom Alarm Tone**: Choose your preferred alarm sound file (`.mp3` or `.wav`). If no custom tone is selected, it defaults to an `alarm.mp3` file (which you would need to provide in the same directory as the script).
* **Snooze Functionality**: Option to snooze the alarm for 5 minutes after it triggers.
* **Stop Alarm**: Manually stop the alarm at any time.
* **Multi-threading**: Uses threading to check the alarm time in the background, preventing the UI from freezing.
* **User-Friendly Interface**: Built with Tkinter for a simple and intuitive graphical user interface.

## Requirements

Before running the application, you need to install the following Python libraries:

* `tkinter` (usually comes pre-installed with Python)
* `pygame` (for playing audio files)

You can install `pygame` using pip:

```bash
pip install pygame
How to Run
Clone the repository (or download the alarm_clock.py file):

Bash

git clone [https://github.com/YourUsername/your-alarm-clock-repo.git](https://github.com/YourUsername/your-alarm-clock-repo.git)
cd your-alarm-clock-repo
(Remember to replace YourUsername and your-alarm-clock-repo with your actual GitHub username and repository name.)

Optional: Add a default alarm tone.
If you don't choose a custom tone, the application will look for a file named alarm.mp3 in the same directory as alarm_clock.py. You can place your preferred default alarm sound file here.

Run the application:

Bash

python alarm_clock.py
Usage
Set Alarm Time: Enter the desired alarm time in the "Set Alarm (HH:MM:SS):" field (e.g., 14:30:00 for 2:30 PM).
Choose Alarm Tone: Click the "Choose Alarm Tone" button to select an .mp3 or .wav file from your computer. The selected file name will appear below the button.
Set Alarm: Click "Set Alarm". A status message will confirm the alarm is set.
Alarm Trigger: When the set time is reached, the chosen alarm tone will play, and a "Snooze for 5 minutes?" message box will appear.
Snooze/Stop:
Click "Yes" on the snooze prompt to set the alarm for another 5 minutes.
Click "No" on the snooze prompt, or click the "Stop Alarm" button at any time, to stop the alarm sound and clear the alarm.
Project Structure
alarm_clock.py: The main Python script containing the AlarmClock class and application logic.
(Optional) alarm.mp3: A default alarm sound file (if you choose to include one for users who don't set a custom tone).
Dependencies
tkinter: Standard Python GUI library.
datetime: For handling time objects.
time: For time-related operations (e.g., time.sleep).
threading: To run the alarm check in a separate thread.
os: For path manipulation (e.g., os.path.basename, os.path.abspath).
pygame: Essential for playing audio files.
Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page (create this link if you want) or create a pull request.

Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.
License
This project is open-source and available under the [e.g., MIT License].
(Remember to create a LICENSE file in your repository and specify the license you choose, e.g., MIT, Apache 2.0, etc.)


Sources
