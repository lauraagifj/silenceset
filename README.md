# SilenceSet

SilenceSet is a Python script designed to customize sound profiles and mute unwanted system noises on Windows devices. It allows users to mute all system sounds temporarily and restore them back to their original state.

## Features

- Mute all system sounds on Windows.
- Restore original system sound volume.

## Requirements

- Python 3.x
- Windows OS
- pywin32 package

## Installation

1. Ensure you have Python 3.x installed on your Windows device.
2. Install the required package using pip:

   ```bash
   pip install pywin32
   ```

3. Download the `silence_set.py` script to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `silence_set.py`.
3. Run the script using Python:

   ```bash
   python silence_set.py
   ```

4. The script will mute all system sounds. Press Enter to restore the original volume.

## Note

This script is intended for use on Windows systems only and requires the pywin32 package to interact with system audio settings.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests if you find bugs or want to contribute to the development of SilenceSet.