from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
from pymodbus.register_read_message import ReadHoldingRegistersResponse
client = ModbusClient('192.168.101.105', port=10502, framer=ModbusFramer)
success = client.connect()


client.write_register(0x12,28,unit=1)    


read = client.read_holding_registers(0x12, unit=1)
print(read)
try:
    print(read.registers)
except:
    print('no way bitch')

