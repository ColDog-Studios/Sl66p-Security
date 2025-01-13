# patch_status_checker.py

import os
import subprocess
import logging

class PatchStatusChecker:
    def __init__(self, device_ip):
        self.device_ip = device_ip
        self.logger = logging.getLogger(__name__)

    def check_patch_status(self):
        try:
            # Example command to check patch status (this will vary based on the device)
            command = f"ssh admin@{self.device_ip} 'sudo apt list --upgradable'"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return self.parse_patch_output(result.stdout)
            else:
                self.logger.error(f"Error checking patch status: {result.stderr}")
                return None
        except Exception as e:
            self.logger.exception("Exception occurred while checking patch status.")
            return None

    def parse_patch_output(self, output):
        patches = []
        for line in output.splitlines()[1:]:
            if line:
                patches.append(line.split()[0])  # Extract package name
        return patches

    def alert_if_outdated(self, patches):
        if patches:
            self.logger.warning(f"Outdated patches found on {self.device_ip}: {', '.join(patches)}")
            # Here you could implement further alerting mechanisms (e.g., email, SMS)

# Example usage:
# checker = PatchStatusChecker("192.168.1.1")
# outdated_patches = checker.check_patch_status()
# checker.alert_if_outdated(outdated_patches)