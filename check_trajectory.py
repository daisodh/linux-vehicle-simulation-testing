import csv
import subprocess
import sys
result = subprocess.run(
    ["./car_sim", "2", "5"],
    capture_output=True,
    text=True
)
if result.returncode != 0:
    # 打印 C++ 的错误信息
    
    print(result.stderr)
    sys.exit(1)
   
    # 终止本次测试，不能继续读取旧 CSV
with open("trajectory.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
   
    rows = list(reader)
print("Data rows:", len(rows))
last_row = rows[-1]
actual_x = float(last_row["x_m"])
print(actual_x)
expected_x = 10.0
if actual_x==expected_x:
	print("pass")
else:
	print("fail")
	sys.exit(1)