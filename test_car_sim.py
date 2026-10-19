import csv
import subprocess
import pytest
from pathlib import Path
@pytest.mark.parametrize(
    "speed, steps, expected_x",
    [
        (2, 5, 10),
        (3, 4, 12),
        (0, 5, 0),
    ]
)
def test_car_moves_forward(speed, steps, expected_x):
    csv_path = Path("trajectory.csv")
    csv_path.unlink(missing_ok=True)

    result = subprocess.run(
        ["./car_sim", str(speed), str(steps)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, result.stderr
    assert csv_path.is_file()

    with open("trajectory.csv", "r", newline="") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == steps+1

    actual_x = float(rows[-1]["x_m"])
    assert actual_x==expected_x
    for i, row in enumerate(rows):
        actual_time = float(row["time_s"])
        actual_x = float(row["x_m"])

        expected_time = i
        expected_position = speed * i

        assert actual_time == pytest.approx(expected_time)
        assert actual_x == pytest.approx(expected_position)    

    # TODO 1：断言实际时间等于预期时间
    # TODO 2：断言实际 X 坐标等于预期位置
@pytest.mark.parametrize(
    "speed, steps",
    [
        	("abc", "5"),
		("-1", "5"),
		("31", "5"),
		("2", "0"),
		("2", "1001"),
		("2", "5abc"),
		("2abc", "5"),
		("nan", "5"),
		("1e309", "5"),
        
        # TODO: 在这里补充其他八组异常输入
    ]
)
def test_invalid_parameters(speed, steps):
    result = subprocess.run(
        ["./car_sim", speed, steps],
        capture_output=True,
        text=True
    )

    # TODO: 用 assert 检查退出码是否不等于 0
    assert result.returncode == 1, result.stderr
    assert result.stderr.strip() != ""

    # TODO：自己编写断言，验证 actual_x == 10.0