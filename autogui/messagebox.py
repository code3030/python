import pyautogui

# btn_1 = pyautogui.alert('경고', 'title', 'OKOK')
# btn_1 = pyautogui.alert(button='OKOK', text='경고', title='title')

# btn_2 = pyautogui.confirm(text='테스트', title='title', buttons=['0', '1', '2', '3'])
# print(btn_2)
# if btn_2 == 'OK':
#     print('OK입니다.')

# btn_3 = pyautogui.prompt()
# btn_3 = pyautogui.prompt(title="TITLE", default='여기에 쓰세요')
# print(btn_3)

btn_4 = pyautogui.password('password', '비밀번호를 입력하세요',mask='$')
if btn_4 == '1234':
    print('OK')
else:
    print('SORRY')