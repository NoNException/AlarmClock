from prompt_toolkit.key_binding import KeyBindings
from ui.DisplayContainer import display_container, AlarmThread, buffer
from dialog.SetAlarmDialog import SetAlarmDialog

kb = KeyBindings()


@kb.add('c-q')
def exit_(event):
    '''
    退出快捷键
    :param event: 事件内容
    :return: null
    '''
    display_container.alarm_thread.stop()
    event.app.exit()


@kb.add('c-w')
def stop_(event):
    '''
    停止计时快捷键
    :param event: 事件内容
    :return:null
    '''
    display_container.alarm_thread.stop()


@kb.add('c-s')
def start_(event):
    '''
    开始快捷键
    :param event:事件内容
    :return: null
    '''

    if display_container.alarm_thread.stop_flag:
        display_container.alarm_thread = AlarmThread(buffer)
        display_container.alarm_thread.start()


@kb.add('c-n')
def set_alarm(event):
    SetAlarmDialog(event)
