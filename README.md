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


