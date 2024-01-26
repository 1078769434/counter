import PySimpleGUI as sg


def calculate(expression):
    try:
        # 使用 eval 来计算表达式，这里添加了对安全的基本考虑
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except Exception as e:
        return f'错误: {str(e)}'


sg.theme('LightGrey1')  # 使用浅色主题

# 定义按钮样式
button_font = ('Calibri', 14)
button_size = (4, 2)

# 运算符按钮样式
operator_button = lambda button_text: sg.Button(button_text, button_color=('black', 'light grey'), size=button_size,
                                                key=button_text, font=button_font)
# 数字按钮样式
number_button = lambda button_text: sg.Button(button_text, button_color=('black', 'white'), size=button_size,
                                              key=button_text, font=button_font)
# 计算 清除 按钮
compute_button = lambda button_text: sg.Button(button_text, button_color=('black', 'light grey'), size=button_size,
                                               key=button_text, font=button_font)
# 退出按钮
quit_button = lambda button_text: sg.Button(button_text, button_color=('black', 'light grey'), size=(20, 2),
                                            key=button_text, font=button_font)

# 创建窗口布局
layout = [

    [sg.Input(key='-IN-', size=(20, 1), font=('Calibri', 18), border_width=0)],  # 无边框且字体较大的输入框
    [number_button('7'), number_button('8'), number_button('9'), operator_button('/')],
    [number_button('4'), number_button('5'), number_button('6'), operator_button('*')],
    [number_button('1'), number_button('2'), number_button('3'), operator_button('-')],
    [number_button('0'), compute_button('清除'), compute_button('='), operator_button('+')],
    [quit_button('退出')]
]

# 创建窗口
window = sg.Window('帽式计算器', layout, background_color='white', icon='counter_new.ico')

# 事件循环
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '退出'):
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']:
        current_input = values['-IN-']
        new_input = current_input + event
        window['-IN-'].update(new_input)
    if event == '清除':
        window['-IN-'].update('')
    if event == '=':
        input_text = values['-IN-']
        result = calculate(input_text)
        window['-IN-'].update(result)

# 关闭窗口
window.close()
