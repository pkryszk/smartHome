import device
def collect_diagnostics(p_device: device.Device):
    # TODO add logic
    print("Connecting to diagnostics server.")
    p_device.status_update()
    return None

