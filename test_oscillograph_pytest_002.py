import numpy as np
import pytest

def generate_sine_wave(frequency, amplitude, duration, sample_rate=1000):
    """
    Generate a sine wave signal.
    
    Parameters:
    - frequency: Frequency of the sine wave in Hz.
    - amplitude: Amplitude of the sine wave.
    - duration: Duration of the signal in seconds.
    - sample_rate: Number of samples per second (default is 1000).
    
    Returns:
    - A numpy array containing the sine wave signal.
    """
    # Generate time values from 0 to duration with the specified sample rate
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Calculate the sine wave values
    return amplitude * np.sin(2 * np.pi * frequency * time)

def record_signal(signals, signal):
    """
    Record an electrical signal into the signals list.
    
    Parameters:
    - signals: List to store recorded signals.
    - signal: The signal to record (numpy array).
    """
    signals.append(signal)  # Append the new signal to the list

def get_last_signal(signals):
    """
    Retrieve the last recorded signal.
    
    Parameters:
    - signals: List containing recorded signals.
    
    Returns:
    - The last recorded signal or None if no signals are recorded.
    """
    return signals[-1] if signals else None  # Return the last signal or None if empty

def clear_signals(signals):
    """
    Clear all recorded signals.
    
    Parameters:
    - signals: List containing recorded signals.
    """
    signals.clear()  # Clear the list of recorded signals

# Test Functions

def test_record_signal():
    """Test the recording of signals."""
    signals = []  # Initialize an empty list to store signals
    # Generate a sine wave signal
    sine_wave = generate_sine_wave(frequency=5, amplitude=1, duration=1)
    # Record the generated signal
    record_signal(signals, sine_wave)
    
    # Check if the signal is recorded correctly
    assert len(signals) == 1  # Expect one signal recorded
    np.testing.assert_array_equal(signals[0], sine_wave)  # Check the recorded signal

def test_get_last_signal():
    """Test retrieval of the last recorded signal."""
    signals = []  # Initialize an empty list to store signals
    # Generate and record two sine wave signals
    sine_wave1 = generate_sine_wave(frequency=5, amplitude=1, duration=1)
    record_signal(signals, sine_wave1)

    sine_wave2 = generate_sine_wave(frequency=10, amplitude=0.5, duration=1)
    record_signal(signals, sine_wave2)

    # Retrieve the last recorded signal
    last_signal = get_last_signal(signals)
    
    # Check if the last signal is the most recent one recorded
    np.testing.assert_array_equal(last_signal, sine_wave2)

def test_clear_signals():
    """Test clearing recorded signals."""
    signals = []  # Initialize an empty list to store signals
    # Generate and record a sine wave signal
    sine_wave = generate_sine_wave(frequency=5, amplitude=1, duration=1)
    record_signal(signals, sine_wave)

    # Clear all recorded signals
    clear_signals(signals)
    
    # Check if the signals list is empty
    assert len(signals) == 0  # Expect no signals recorded

def test_good_signals():
    """Test that generated signals have amplitudes within the acceptable range."""
    signals = []  # Initialize an empty list to store signals
    
    # Generate 5 sine wave signals with random amplitudes uniformly distributed from (0.5, 2.5)
    for _ in range(5):
        amplitude = np.random.uniform(0.5, 2.5)  # Generate a random amplitude
        sine_wave = generate_sine_wave(frequency=5, amplitude=amplitude, duration=1)
        record_signal(signals, sine_wave)  # Record the generated signal

        # Check if the amplitude is within the acceptable range (0.55, 2.45)
        assert 0.55 <= amplitude <= 2.45, f"Amplitude {amplitude} is out of the acceptable range."

# Entry point for running the tests
if __name__ == '__main__':
    pytest.main()  # Run the tests using pytest