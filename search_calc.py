from pywinauto import findwindows

# 현재 윈도우 화면에 있는 프로세스 목록 리스트를 반환한다. 
# 리스트의 각 요소는 element 객체로 프로세스 id, 핸들값, 이름 등의 정보를 보유한다.  
procs = findwindows.find_elements()

for proc in procs:
    print(f"{proc} / 프로세스 : {proc.process_id}")