from netmiko import ConnectHandler

# Device connection details
device = {
    "device_type": "cisco_xe",  # Device type for Cisco IOS XE
    "ip": "devnetsandboxiosxe.cisco.com",  # Public URL
    "username": "admin",  # Username
    "password": "C1sco12345",  # Password
    "port": 22,  # SSH port
}

# Establish connection
try:
    print("Connecting to the device...")
    net_connect = ConnectHandler(**device)

    # Send command and retrieve output
    output = net_connect.send_command("show ip int brief")
    print("\nOutput of 'show ip int brief':")
    print(output)

    # Disconnect from the device
    net_connect.disconnect()
    print("\nDisconnected from the device.")

except Exception as e:
    print(f"An error occurred: {e}")
