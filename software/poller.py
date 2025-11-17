import time
import yaml
from pymodbus.client import ModbusSerialClient

def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def connect_client(cfg):
    client = ModbusSerialClient(
        port=cfg["modbus"]["port"],
        baudrate=cfg["modbus"]["baudrate"],
        parity=cfg["modbus"]["parity"],
        stopbits=cfg["modbus"]["stopbits"],
        bytesize=cfg["modbus"]["bytesize"],
        timeout=1,
    )
    if not client.connect():
        raise RuntimeError("Modbus connection failed")
    return client

def read_power_32bit(client, unit_id, reg, scale):
    rr = client.read_holding_registers(address=reg, count=2, unit=unit_id)
    if rr.isError():
        raise RuntimeError(f"Modbus error on reg {reg}: {rr}")
    raw = (rr.registers[0] << 16) | rr.registers[1]
    if raw & 0x80000000:
        raw = raw - 0x100000000
    return raw * scale

def main():
    cfg = load_config()
    client = connect_client(cfg)
    addr = cfg["modbus"]["unit_id"]
    interval = cfg["logging"]["interval_seconds"]
    channels = cfg["channels"]

    while True:
        try:
            p_mains_l1 = read_power_32bit(client, addr,
                                          channels["mains_l1"]["register_power"],
                                          channels["mains_l1"]["scale"])
            p_mains_l2 = read_power_32bit(client, addr,
                                          channels["mains_l2"]["register_power"],
                                          channels["mains_l2"]["scale"])
            p_solar = read_power_32bit(client, addr,
                                       channels["solar_pv"]["register_power"],
                                       channels["solar_pv"]["scale"])

            p_mains_total = p_mains_l1 + p_mains_l2
            p_grid = p_mains_total
            p_load = p_solar + p_grid

            print(f"Solar: {p_solar:.1f} W | Load: {p_load:.1f} W | Grid: {p_grid:.1f} W")
        except Exception as e:
            print("Error in poll loop:", e)

        time.sleep(interval)

if __name__ == "__main__":
    main()