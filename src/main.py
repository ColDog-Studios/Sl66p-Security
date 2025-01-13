# Sleep Security - main.py

import sys
from utils.logger import setup_logging
from scanning.network_mapper import scan_network
from monitoring.port_monitor import check_open_ports
from monitoring.firmware_alert import alert_outdated_firmware
from monitoring.config_monitor import monitor_configurations
from monitoring.patch_status_checker import check_patching_status
from hardening.policy_support import load_policies

def main():
    setup_logging()
    
    # Load custom policies
    policies = load_policies('config/default_policies.yaml')
    
    # Scan the network for devices
    devices = scan_network()
    
    # Monitor each device for various security aspects
    for device in devices:
        check_open_ports(device)
        alert_outdated_firmware(device)
        monitor_configurations(device)
        check_patching_status(device)
    
    # Additional features can be added here later
    print("Security monitoring initiated.")

if __name__ == "__main__":
    main()