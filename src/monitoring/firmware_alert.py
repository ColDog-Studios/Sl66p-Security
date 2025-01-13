def check_firmware_version(device):
    # Placeholder function to check the firmware version of a device
    # In a real implementation, this would query the device and return the version
    return "1.0.0"  # Example version


def alert_outdated_firmware(device, current_version, latest_version):
    if current_version < latest_version:
        print(f"Alert: Device {device} has outdated firmware (Current: {current_version}, Latest: {latest_version})")


def monitor_firmware(devices, latest_firmware_versions):
    for device in devices:
        current_version = check_firmware_version(device)
        latest_version = latest_firmware_versions.get(device)
        if latest_version:
            alert_outdated_firmware(device, current_version, latest_version)