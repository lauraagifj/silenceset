import os
import ctypes
from ctypes import wintypes

class SilenceSet:
    def __init__(self):
        self.original_volume = None

    def get_system_volume(self):
        # Function to get the current system volume
        try:
            import win32api
            import win32con
            
            mixer = ctypes.windll.winmm.waveOutGetVolume
            volume = ctypes.c_ulong()
            mixer(0, ctypes.byref(volume))
            return (volume.value & 0xffff) / 0xffff
        except ImportError:
            raise EnvironmentError("This function requires the pywin32 package")

    def set_system_volume(self, volume_level):
        # Function to set the system volume
        try:
            import win32api
            import win32con
            
            mixer = ctypes.windll.winmm.waveOutSetVolume
            volume = int(volume_level * 0xffff)
            mixer(0, volume | (volume << 16))
        except ImportError:
            raise EnvironmentError("This function requires the pywin32 package")

    def mute_system_sounds(self):
        # Function to mute all system sounds
        self.original_volume = self.get_system_volume()
        self.set_system_volume(0)

    def restore_system_sounds(self):
        # Function to restore the original system volume
        if self.original_volume is not None:
            self.set_system_volume(self.original_volume)

if __name__ == '__main__':
    silence_set = SilenceSet()
    print("Muting system sounds...")
    silence_set.mute_system_sounds()
    input("System sounds are muted. Press Enter to restore original volume...")
    silence_set.restore_system_sounds()
    print("Original system volume restored.")