import time
from pywinauto import Desktop, Application

# pywinauto를 사용하여 'calc.exe' 프로세스를 시작하고 계산기 창을 엽니다.
app = Application(backend="uia").start('calc.exe')

# Desktop 객체를 사용하여 계산기 창을 가져옵니다.
# 계산기 창은 Desktop 객체에만 접근 가능합니다.
dlg = Desktop(backend="uia").계산기

# 대기합니다.
wait_time = 60
start = time.time()
print(f"{time.time() - start:.1f}: 계산기가 준비될 때까지 대기합니다.")
dlg.wait("ready", timeout=wait_time)

print(f"{time.time() - start:.1f}: 대기 시간이 종료되었습니다.")

# 숫자와 연산자를 입력하고 결과를 출력합니다.
dlg.type_keys('2*3=')
dlg.print_control_identifiers()

# 계산기 창을 최소화한 후, 다시 복원합니다.
dlg.minimize()
Desktop(backend="uia").window(title='계산기', visible_only=False).restore()

# 자식 창 객체를 사용하여 결과 텍스트를 가져옵니다.
calc_result = dlg.child_window(auto_id="CalculatorResults", control_type="Text")
result_text = calc_result.window_text()
result = result_text.replace("표시는 ", "")
print(f"{time.time() - start:.1f}: {result}")
