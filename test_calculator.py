from pywinauto import Desktop, Application

def test_calculator_addition(calculator):
    calculator.type_keys("1")
    calculator.type_keys("{+}")
    calculator.type_keys("2")
    calculator.type_keys("=")
    result = get_result(calculator)
    assert result == "3", f"Addition test failed: expected 3, got {result}"
    print("Addition test passed.")
    calculator.type_keys("C")

def test_calculator_subtraction(calculator):
    calculator.type_keys("5")
    calculator.type_keys("-")
    calculator.type_keys("2")
    calculator.type_keys("=")
    result = get_result(calculator)
    assert result == "3", f"Subtraction test failed: expected 3, got {result}"
    print("Subtraction test passed.")
    calculator.type_keys("C")

def test_calculator_multiplication(calculator):
    calculator.type_keys("3")
    calculator.type_keys("*")
    calculator.type_keys("2")
    calculator.type_keys("=")
    result = get_result(calculator)
    assert result == "6", f"Multiplication test failed: expected 6, got {result}"
    print("Multiplication test passed.")
    calculator.type_keys("C")

def test_calculator_division(calculator):
    calculator.type_keys("6")
    calculator.type_keys("/")
    calculator.type_keys("2")
    calculator.type_keys("=")
    result = get_result(calculator)
    assert result == "3", f"Division test failed: expected 3, got {result}"
    print("Division test passed.")
    calculator.type_keys("C")

def get_result(calculator):
    calc_result = calculator.child_window(auto_id="CalculatorResults", control_type="Text")
    result_text = calc_result.window_text()
    result = result_text.replace("표시는 ", "")
    return result

def main():
    # 계산기 어플리케이션 실행
    app = Application(backend="uia").start("calc.exe")
    
    
    # 계산기 창을 활성화
    calculator = Desktop(backend="uia").계산기
    calculator.wait("ready", timeout=60)
    
    # 사칙연산 테스트
    test_calculator_addition(calculator)
    test_calculator_subtraction(calculator)
    test_calculator_multiplication(calculator)
    test_calculator_division(calculator)

    # 계산기 어플리케이션 종료
    app.kill()

if __name__ == "__main__":
    main()
