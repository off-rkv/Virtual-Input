# VirtualInput Library - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Core Features](#core-features)
4. [Architecture](#architecture)
5. [Virtual Mouse](#virtual-mouse)
6. [Virtual Keyboard](#virtual-keyboard)
7. [Input Recorder](#input-recorder)
8. [Platform Support](#platform-support)
9. [API Reference](#api-reference)
10. [Examples](#examples)
11. [Advanced Features](#advanced-features)
12. [Troubleshooting](#troubleshooting)

## Overview

VirtualInput is a cross-platform Python library for virtual mouse and keyboard control with advanced features including:

- **Ghost Mouse Technology**: Move cursor to negative coordinates and off-screen areas
- **Bézier Curve Movements**: Human-like curved mouse paths for undetectable automation
- **Cross-Platform Support**: Works on Windows and macOS with automatic platform detection
- **Input Recording & Playback**: Record complex sequences and replay them with variations
- **Kernel-Level Access**: Direct system API calls for maximum compatibility and performance

### Key Advantages
- No coordinate restrictions (supports negative coordinates)
- Human-like movement patterns to avoid detection
- Professional error handling and validation
- Comprehensive recording and macro capabilities
- Clean, intuitive API design

## Installation

### Requirements
- Python 3.6 or higher
- Platform-specific dependencies automatically handled

### Basic Installation
```bash
pip install virtualinput
```

### Platform-Specific Dependencies

**Windows:**
- Uses built-in ctypes (no additional dependencies)

**macOS:**
- Requires pyobjc for Core Graphics access
```bash
pip install virtualinput[macos]
# or manually:
pip install pyobjc
```

### Development Installation
```bash
git clone https://github.com/yourusername/virtualinput
cd virtualinput
pip install -e .
```

## Core Features

### 1. Ghost Mouse Technology
Move mouse cursor to coordinates that normal libraries cannot reach:
- Negative coordinates (off-screen left/top)
- Beyond screen boundaries
- Hidden application areas
- Multi-monitor setups with negative coordinate spaces

### 2. Bézier Curve Movements
Mathematically generated curved paths using quadratic Bézier curves:
```
x(t) = (1 - t)² × x₀ + 2(1 - t) × t × xc + t² × x₁
y(t) = (1 - t)² × y₀ + 2(1 - t) × t × yc + t² × y₁
```
Where t goes from 0 to 1, creating natural human-like movement patterns.

### 3. Human-Like Timing
- Random variations in click duration
- Natural acceleration/deceleration patterns
- Realistic typing speeds with character-based delays
- Pause variations to mimic human behavior

## Architecture

### Project Structure
```
virtualinput/
├── __init__.py              # Main imports and convenience functions
├── mouse.py                 # VirtualMouse main interface
├── keyboard.py              # VirtualKeyboard main interface
├── recorder.py              # InputRecorder and Macro classes
├── core/
│   ├── __init__.py
│   ├── base_classes.py      # Abstract base classes
│   ├── exceptions.py        # Custom exception classes
│   ├── keycodes.py          # Universal key constants
│   └── utils.py             # Shared utility functions
└── platforms/
    ├── windows/
    │   ├── __init__.py
    │   ├── mouse.py         # Windows mouse implementation
    │   ├── keyboard.py      # Windows keyboard implementation
    │   └── utils.py         # Windows-specific utilities
    └── macos/
        ├── __init__.py
        ├── mouse.py         # macOS mouse implementation
        ├── keyboard.py      # macOS keyboard implementation
        └── utils.py         # macOS-specific utilities
```

### Design Patterns
- **Strategy Pattern**: Platform-specific implementations
- **Factory Pattern**: Automatic platform detection
- **Command Pattern**: Recordable actions
- **Template Method**: Base classes with common functionality

## Virtual Mouse

### Basic Usage
```python
from virtualinput import VirtualMouse

mouse = VirtualMouse()

# Basic movement
mouse.move(500, 300)                    # Move to coordinates
mouse.move_relative(50, -25)            # Move relative to current position

# Ghost coordinates
mouse.move(-100, 200)                   # Off-screen left
mouse.move(2000, 400)                   # Beyond screen right

# Clicking
mouse.click()                           # Left click at current position
mouse.click('right')                    # Right click
mouse.double_click()                    # Double-click
```

### Bézier Curve Movements
```python
# Human-like curved movement
mouse.move_bezier(end_x=800, end_y=600, duration=1.5, curve_intensity=0.4)

# Relative curved movement
mouse.move_bezier_relative(dx=200, dy=100, duration=1.0)

# Curved drag operation
mouse.drag_bezier(start_x=100, start_y=100, end_x=500, end_y=300, duration=2.0)
```

### Advanced Mouse Features
```python
# Convenience methods
mouse.click_at(x=400, y=300, use_bezier=True)
mouse.double_click_at(x=500, y=400)

# Stealth operations
mouse.stealth_click(x=600, y=500)  # Moves via ghost area first

# Natural scrolling
mouse.natural_scroll(direction='up', distance=5, speed=0.1)

# Button state management
mouse.press_and_hold('left')
# ... perform operations while holding
mouse.release('left')
```

### Mouse Properties
```python
# Get current position (supports ghost coordinates)
x, y = mouse.get_position()

# Check button states
if mouse.is_button_pressed('left'):
    print("Left button is held down")

# Get screen information
width, height = mouse.get_screen_size()
```

## Virtual Keyboard

### Basic Usage
```python
from virtualinput import VirtualKeyboard
from virtualinput.core.keycodes import KeyCode

keyboard = VirtualKeyboard()

# Basic key operations
keyboard.press('a')                     # Press and release
keyboard.press(KeyCode.ENTER)           # Using constants
keyboard.type("Hello, World!")          # Type text

# Key combinations
keyboard.hotkey('ctrl', 'c')            # Copy
keyboard.hotkey('ctrl', 'shift', 's')   # Save As
keyboard.hotkey('alt', 'tab')           # Alt+Tab
```

### Advanced Keyboard Features
```python
# Text with embedded hotkeys
keyboard.type_with_hotkeys("Hello {ctrl+a} World {ctrl+c}")

# Realistic typing simulation
keyboard.simulate_real_typing("This types at 45 WPM", wpm=45)

# Special character support
keyboard.type_special_chars("Héllo Wörld! 你好 🌍")

# Key state management
keyboard.press_and_hold('shift')
keyboard.press('a')  # Types uppercase A
keyboard.release('shift')

# Check key states
if keyboard.is_pressed('ctrl'):
    print("Ctrl is being held")
```

### Keyboard Constants
```python
from virtualinput.core.keycodes import KeyCode

# Letter keys
KeyCode.A, KeyCode.B, KeyCode.C, ...

# Number keys  
KeyCode.KEY_0, KeyCode.KEY_1, ...

# Function keys
KeyCode.F1, KeyCode.F2, ...

# Special keys
KeyCode.ENTER, KeyCode.SPACE, KeyCode.TAB, KeyCode.ESCAPE
KeyCode.BACKSPACE, KeyCode.DELETE, KeyCode.HOME, KeyCode.END

# Arrow keys
KeyCode.UP, KeyCode.DOWN, KeyCode.LEFT, KeyCode.RIGHT

# Modifier keys
KeyCode.CTRL, KeyCode.ALT, KeyCode.SHIFT, KeyCode.CMD, KeyCode.WIN
```

## Input Recorder

### Recording Actions
```python
from virtualinput import InputRecorder

recorder = InputRecorder()

# Start recording
recorder.start_recording()

# Record various actions
recorder.record_mouse_click(x=100, y=200, button='left')
recorder.record_key_type("Hello World")
recorder.record_hotkey('ctrl', 'c')
recorder.record_pause(1.0)  # 1 second pause

# Stop recording
recorder.stop_recording()
```

### Saving and Loading
```python
# Save recording to file
recorder.save_recording("my_automation.json")

# Load recording from file
recorder.load_recording("my_automation.json")

# Get recording information
print(f"Duration: {recorder.get_recording_duration():.2f} seconds")
print(f"Actions: {recorder.get_action_count()}")
print(f"Summary: {recorder.get_action_summary()}")
```

### Playback and Automation
```python
# Basic playback
recorder.replay_recording()

# Speed control
recorder.replay_recording(speed_multiplier=2.0)    # 2x speed
recorder.replay_recording(speed_multiplier=0.5)    # Half speed

# Enhanced playback with curves
recorder.replay_recording(use_bezier=True)

# Loop playback
recorder.create_loop_recording(loop_count=10, loop_delay=2.0)
recorder.create_loop_recording(loop_count=-1)      # Infinite loop
```

### Macro Creation
```python
# Create reusable macro
macro = recorder.create_macro("LoginSequence")
macro.save_to_file("login_macro.json")

# Load and execute macro
from virtualinput.recorder import Macro
macro = Macro.load_from_file("login_macro.json")
macro.execute(speed_multiplier=1.5)
```

### Recording Optimization
```python
# Optimize recording (remove redundant actions)
recorder.optimize_recording()

# Get detailed statistics
stats = recorder.get_recording_stats()
print(f"Total mouse distance: {stats['total_mouse_distance']:.2f} pixels")
print(f"Actions per second: {stats['average_actions_per_second']:.2f}")
```

## Platform Support

### Windows Support
- **APIs Used**: Win32 API via ctypes
- **Mouse**: SetCursorPos, mouse_event, GetCursorPos
- **Keyboard**: keybd_event, SendInput for Unicode
- **Features**: All ghost coordinates, multi-monitor support

### macOS Support  
- **APIs Used**: Core Graphics (Quartz) and Cocoa frameworks
- **Mouse**: CGEventCreateMouseEvent, CGEventPost
- **Keyboard**: CGEventCreateKeyboardEvent
- **Requirements**: pyobjc package, accessibility permissions

### Platform Detection
The library automatically detects your operating system and loads the appropriate implementation:

```python
# This works on any supported platform
mouse = VirtualMouse()  # Automatically uses WindowsMouse or MacOSMouse
keyboard = VirtualKeyboard()  # Automatically uses WindowsKeyboard or MacOSKeyboard
```

## API Reference

### VirtualMouse Methods

#### Basic Movement
- `move(x: int, y: int) -> bool`: Move to absolute coordinates
- `move_relative(dx: int, dy: int) -> bool`: Move relative to current position
- `get_position() -> Tuple[int, int]`: Get current cursor position

#### Bézier Movement
- `move_bezier(end_x: int, end_y: int, duration: float = 1.0, curve_intensity: float = 0.3) -> bool`
- `move_bezier_relative(dx: int, dy: int, duration: float = 1.0, curve_intensity: float = 0.3) -> bool`

#### Clicking
- `click(button: str = 'left') -> bool`: Single click
- `double_click(button: str = 'left') -> bool`: Double click
- `press_and_hold(button: str = 'left') -> bool`: Press and hold button
- `release(button: str = 'left') -> bool`: Release held button

#### Dragging
- `drag(start_x: int, start_y: int, end_x: int, end_y: int, button: str = 'left') -> bool`
- `drag_bezier(start_x: int, start_y: int, end_x: int, end_y: int, button: str = 'left', duration: float = 1.0) -> bool`

#### Convenience Methods
- `click_at(x: int, y: int, button: str = 'left', use_bezier: bool = True, duration: float = 1.0) -> bool`
- `stealth_click(x: int, y: int, button: str = 'left') -> bool`

#### Scrolling
- `scroll(direction: str, clicks: int = 1) -> bool`
- `natural_scroll(direction: str, distance: int = 3, speed: float = 0.1) -> bool`

### VirtualKeyboard Methods

#### Basic Key Operations
- `press(keycode: str) -> bool`: Press and release key
- `press_and_hold(keycode: str) -> bool`: Press and hold key
- `release(keycode: str) -> bool`: Release held key
- `is_pressed(keycode: str) -> bool`: Check if key is pressed

#### Text Input
- `type(text: str, delay: float = 0.01) -> bool`: Type text with delays
- `type_with_hotkeys(text: str, delay: float = 0.01) -> bool`: Type text with embedded hotkeys
- `simulate_real_typing(text: str, wpm: int = 60) -> bool`: Type at specific WPM

#### Key Combinations
- `hotkey(*keys: str) -> bool`: Press multiple keys simultaneously

#### Utility Methods
- `release_all() -> bool`: Release all held keys
- `get_pressed_keys() -> set`: Get currently pressed keys

### InputRecorder Methods

#### Recording Control
- `start_recording() -> bool`: Start recording input
- `stop_recording() -> bool`: Stop recording input

#### Manual Action Recording
- `record_mouse_move(x: int, y: int) -> bool`
- `record_mouse_click(x: int, y: int, button: str = 'left') -> bool`
- `record_mouse_drag(start_x: int, start_y: int, end_x: int, end_y: int, button: str = 'left') -> bool`
- `record_key_press(keycode: str) -> bool`
- `record_key_type(text: str) -> bool`
- `record_hotkey(*keys: str) -> bool`

#### File Operations
- `save_recording(filename: str) -> bool`: Save to JSON file
- `load_recording(filename: str) -> bool`: Load from JSON file

#### Playback
- `replay_recording(speed_multiplier: float = 1.0, use_bezier: bool = True) -> bool`
- `create_loop_recording(loop_count: int = -1, loop_delay: float = 1.0) -> bool`

#### Analysis
- `get_recording_duration() -> float`: Get total duration
- `get_action_count() -> int`: Get number of actions
- `get_recording_stats() -> Dict[str, Any]`: Get detailed statistics
- `optimize_recording() -> bool`: Remove redundant actions

## Examples

### Example 1: Basic Automation
```python
from virtualinput import VirtualMouse, VirtualKeyboard

mouse = VirtualMouse()
keyboard = VirtualKeyboard()

# Open notepad and type something
mouse.click_at(100, 50)  # Click Start button
keyboard.type("notepad")
keyboard.press("enter")

# Wait for notepad to open
import time
time.sleep(2)

# Type in notepad
keyboard.type("Hello from VirtualInput!")
keyboard.hotkey("ctrl", "s")  # Save
```

### Example 2: Ghost Mouse Stealth Operation
```python
# Hide a window off-screen and interact with it
import subprocess

# Start an application
subprocess.Popen(["notepad.exe"])
time.sleep(2)

# Move the window off-screen (you'd need window management code)
# Then interact with it using ghost coordinates
mouse.move(-100, 100)  # Move to hidden window area
mouse.click()          # Click in hidden window
keyboard.type("This text goes to the hidden window!")
```

### Example 3: Recording and Playback
```python
from virtualinput import InputRecorder

recorder = InputRecorder()

# Record a login sequence
recorder.start_recording()
recorder.record_mouse_click(300, 400)  # Username field
recorder.record_key_type("username")
recorder.record_mouse_click(300, 450)  # Password field
recorder.record_key_type("password")
recorder.record_mouse_click(400, 500)  # Login button
recorder.stop_recording()

# Save for later use
recorder.save_recording("login_sequence.json")

# Replay it 5 times with 2 second delays
recorder.create_loop_recording(loop_count=5, loop_delay=2.0)
```

### Example 4: Complex Automation with Curves
```python
# Natural-looking web form automation
mouse.move_bezier(300, 200, duration=1.0)  # Move to first field naturally
keyboard.type("John Doe")

mouse.move_bezier(300, 250, duration=0.8)  # Next field with curve
keyboard.type("john@email.com")

mouse.move_bezier(300, 300, duration=0.6)  # Phone field
keyboard.type("555-1234")

# Curved movement to submit button
mouse.move_bezier(400, 400, duration=1.2, curve_intensity=0.5)
mouse.click()
```

### Example 5: Game Automation
```python
# Record a gaming sequence
recorder.start_recording()

# Combat sequence
recorder.record_mouse_click(500, 300, 'left')   # Attack
recorder.record_key_press('space')              # Use skill
recorder.record_mouse_click(600, 400, 'right')  # Move
recorder.record_pause(0.5)                      # Wait for cooldown

recorder.stop_recording()

# Loop this combat sequence
recorder.create_loop_recording(loop_count=-1, loop_delay=0.1)
```

## Advanced Features

### Coordinate Systems
- **Standard Coordinates**: (0,0) to (screen_width, screen_height)
- **Ghost Coordinates**: Negative values and beyond screen boundaries
- **Multi-Monitor**: Automatic handling of negative coordinate spaces

### Timing and Delays
- **Random Variations**: All delays include human-like randomization
- **Acceleration Curves**: Bézier movements include realistic acceleration/deceleration
- **Typing Rhythms**: Natural typing patterns with pause variations

### Error Handling
```python
from virtualinput.core.exceptions import VirtualInputError, PlatformNotSupportedError

try:
    mouse = VirtualMouse()
    mouse.move(500, 300)
except PlatformNotSupportedError as e:
    print(f"Platform not supported: {e}")
except VirtualInputError as e:
    print(f"Virtual input error: {e}")
```

### Platform Information
```python
# Get platform details
mouse_info = mouse.get_platform_info()
keyboard_info = keyboard.get_platform_info()

print(f"Mouse implementation: {mouse_info['implementation']}")
print(f"Platform: {mouse_info['platform']}")
print(f"Features: {mouse_info['supported_features']}")
```

### Recording File Format
The library saves recordings in JSON format:
```json
{
  "version": "1.0",
  "total_duration": 5.67,
  "action_count": 15,
  "created_at": 1699123456.789,
  "actions": [
    {
      "action_type": "mouse_move",
      "timestamp": 0.0,
      "data": {"x": 100, "y": 200}
    },
    {
      "action_type": "mouse_click", 
      "timestamp": 1.2,
      "data": {"x": 100, "y": 200, "button": "left"}
    }
  ]
}
```

## Troubleshooting

### Common Issues

#### 1. Permission Errors (macOS)
**Problem**: "Failed to create mouse/keyboard events"
**Solution**: Enable accessibility permissions
```bash
# Open System Preferences > Security & Privacy > Privacy > Accessibility
# Add your Python application or terminal to the list
```

#### 2. Import Errors (macOS)
**Problem**: "No module named 'Quartz'"
**Solution**: Install pyobjc
```bash
pip install pyobjc
# or
pip install virtualinput[macos]
```

#### 3. Coordinates Not Working
**Problem**: Mouse not moving to expected position
**Solution**: Check coordinate system and screen bounds
```python
# Get screen size first
width, height = mouse.get_screen_size()
print(f"Screen size: {width}x{height}")

# Verify current position
x, y = mouse.get_position()
print(f"Current position: ({x}, {y})")
```

#### 4. Recording Playback Issues
**Problem**: Actions not executing correctly during playback
**Solution**: Add delays and use Bézier curves
```python
# Use slower playback for debugging
recorder.replay_recording(speed_multiplier=0.5, use_bezier=True)
```

### Performance Tips

1. **Use Bézier curves for detection avoidance**
2. **Add random delays between actions**
3. **Use ghost coordinates for stealth operations**
4. **Optimize recordings before saving**
5. **Use appropriate speed multipliers for playback**

### Platform-Specific Notes

#### Windows
- No additional setup required
- All features fully supported
- Multi-monitor setups work automatically

#### macOS
- Requires accessibility permissions
- May need to disable System Integrity Protection for some applications
- Some applications may still detect automation

## Contributing

### Development Setup
```bash
git clone https://github.com/yourusername/virtualinput
cd virtualinput
pip install -e ".[dev]"
```

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
- Follow PEP 8
- Use type hints
- Include docstrings for all public methods
- Add unit tests for new features

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Changelog

### Version 1.0.0
- Initial release
- Cross-platform mouse and keyboard control
- Ghost coordinate support
- Bézier curve movements
- Input recording and playback
- Macro creation and management

---

*VirtualInput Library - Professional automation for the modern world*