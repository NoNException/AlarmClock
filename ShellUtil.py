import os
import shutil
import subprocess


# method to execute commands
def execute_commands(command: str, view=False, joiner="", debug=False):
    commands = command.split(" ")
    if joiner:
        view = True
    subprocess_opened = subprocess.Popen(commands, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    subprocess_opened.wait(200)
    err = subprocess_opened.stderr.readlines()
    if subprocess_opened.returncode:
        if view:
            print(joiner.join([x.decode('utf-8') for x in err]))
        if debug:
            print("[DEBUG] error info is:{}".format(err))
        raise ChildProcessError("执行命令:{} 错误..".format(command))
    out = subprocess_opened.stdout.readlines()
    out = [x.decode('utf-8').rstrip() for x in out if x.decode('utf-8').strip().rstrip("\n")]
    if view:
        print(joiner.join(out))
    return out


def execute_commands_sync(commands: str, cwd, view=False, joiner=""):
    print("执行命令:{}".format(commands))
    cmd = commands.split(" ")
    if joiner:
        view = True
    subprocess_opened = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                         cwd=cwd)
    while subprocess_opened.poll() is None:
        line = subprocess_opened.stdout.readline()
        line = line.strip()
        if line or view:
            print(line.decode('utf-8'))
    subprocess_opened.wait()
    if subprocess_opened.returncode:
        print(subprocess_opened.stderr.readlines())
        raise ChildProcessError("执行命令:{} 失败..".format(commands))
    return subprocess_opened.returncode


def create_folder(path, force=False, ignore=False):
    if os.path.exists(path):
        if force:
            print("目录:{} 已存在, 删除文件..".format(path))
            shutil.rmtree(path)
            print("目录:{} 删除成功..".format(path))
        elif ignore:
            print("目录:{} 已存在, 跳过..".format(path))
            return
        else:
            raise FileExistsError("目录:{}已存在存在..")
    os.mkdir(path)


if __name__ == '__main__':
    os.chdir('/Users/zongzi/IdeaProjects/CodeAdmin')
    execute_commands("toilet aaaa", joiner="\n", view=True)
