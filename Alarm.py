import ShellUtil
import time


def get_current_alarm():
    return time.strftime('%H : %M : %S', time.localtime(time.time()))


def get_formatted_alarm():
    time_string = get_current_alarm()
    display_time = "figlet {}".format(time_string)
    str_list = ShellUtil.execute_commands(display_time, view=False)
    return "\n".join(str_list)
