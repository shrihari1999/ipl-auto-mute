# IPL Auto Mute

Automatically mute advertisements during cricket matches on streaming platforms using computer vision and machine learning.

## Overview

This tool uses a trained deep learning model to detect when advertisements are playing during cricket matches (IPL, World Cup, Test matches) and automatically mutes your system audio. When the match resumes, audio is restored automatically.

### How It Works

- **Real-time Screen Monitoring**: Captures a specific region of your screen at ~10 FPS
- **ML-Powered Detection**: Uses a TensorFlow/Keras CNN model to classify frames as "logo" (match content) or "ads"
- **Smart Muting**: Automatically controls system volume based on predictions
- **Noise Filtering**: Uses a sliding window of 3 consecutive predictions to avoid audio chatter

### Supported Platforms & Events

| Platform | IPL | World Cup | Test Matches |
|----------|-----|-----------|--------------|
| Hotstar  | ✓   | ✓         | -            |
| JIO      | ✓   | -         | ✓            |

## Prerequisites

1. **Python 3.7+ (64-bit)** - This program uses TensorFlow. See [TensorFlow installation requirements](https://www.tensorflow.org/install/pip#system-requirements) for details.
2. **pipenv** - Python virtual environment manager
3. **Operating System**:
   - Windows: Uses `SetVol.exe` (included) for volume control
   - Linux: Requires `pactl` for audio control

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shrihari1999/ipl-auto-mute.git
   cd ipl-auto-mute
   ```

2. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

3. Install dependencies (first time only):
   ```bash
   pipenv install
   ```

## Usage

### Basic Usage

Run the program with your streaming platform and event type:

```bash
python run.py <platform> <event>
```

### Examples

```bash
# Watch IPL on JIO
python run.py jio ipl

# Watch Test match on JIO
python run.py jio test

# Watch IPL on Hotstar
python run.py hotstar ipl

# Watch World Cup on Hotstar
python run.py hotstar wc
```

### Runtime Controls

While the program is running, you can control it using keyboard inputs:

- **`p`** - Pause the automation (stops muting/unmuting)
- **`r`** - Resume the automation

## Key Features

- **Cross-Platform Support**: Works on Windows and Linux
- **Adaptive Scaling**: Automatically adjusts to your screen resolution
- **Minimal CPU Usage**: Only monitors a small region of the screen
- **Manual Override**: Pause and resume automation as needed
- **Smart Prediction**: Filters noise to prevent rapid audio toggling

## Technologies Used

- **TensorFlow/Keras 2.8.0** - Deep learning model
- **OpenCV 4.5.5** - Image processing
- **MSS 6.1.0** - Screen capture
- **NumPy 1.21.5** - Numerical operations

## How to Contribute

Contributions are welcome! Areas for improvement:
- Adding support for more streaming platforms
- Training data for better accuracy
- Support for additional cricket events
- Platform-specific optimizations

## License

This project is licensed under the MIT License - see below for details.

```
MIT License

Copyright (c) 2026 Shrihari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments

Created for cricket fans who want to enjoy matches without advertisement interruptions.
