import device
def collect_diagnostics(p_device: device.Device):
    print("Connecting to diagnostics server.")
    p_device.status_update()
    return None

