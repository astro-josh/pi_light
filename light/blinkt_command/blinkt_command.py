"""Represents singleton instance of a Blinkt LED commander.

    File: blinkt_command.py
    Package: blinkt_command
"""
import logging
# from blinkt import set_pixel, set_brightness, show, clear


class BlinktCommand:
    __instance = None

    def __init__(self):
        """Initializes a singleton instance of BlinktCommand."""
        if BlinktCommand.__instance is None:
            BlinktCommand.__instance = self
        else:
            logging.getLogger("BlinktCommand").warning("Singleton already activated, use get instance")

    @staticmethod
    def get_instance():
        """Retrieves the singleton instance of the BlinktCommand."""
        if BlinktCommand.__instance is None:
            BlinktCommand.__instance = BlinktCommand()

        return BlinktCommand.__instance
