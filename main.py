import json
from employee_system import employee_factory
from sensor_system import sensor_factory

print("="*60)
print("UTS OOP - RULE, INHERITANCE, POLYMORPHISM, OVERRIDE")
print("="*60)

print("\n=== 1. PROSES DATA EMPLOYEE (30 DATA) ===")
with open('employee.json') as f:
    emp_data = json.load(f)

for item in emp_data['employees']:
    emp = employee_factory(item)
    # ini bukti polymorphism + override
    print(emp.get_details())
    print(f"     Gaji: {emp.base_salary} + Bonus Code {emp.bonus_code} => Total {emp.calculate_total_salary():,.0f}")

print("\n=== 2. PROSES DATA SENSOR_LOGS (30 DATA) ===")
with open('sensor_logs.json') as f:
    sensor_data = json.load(f)

for item in sensor_data['readings']:
    sensor = sensor_factory(item)
    print(sensor.handle()) # polymorphism handle()

print("\n=== SELESAI - SEMUA RULE BERJALAN ===")