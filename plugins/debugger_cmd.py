"""
开发者命令行
"""
import os
import sys
from typing import IO, Any
from libs import *
from cmd import Cmd

__name__ = "开发者命令行"
__author__ = "此程序开发者"
__version__ = "1.2.0"

public = {"info": "这是一个公共字典，可以在其中存储变量"}

class DebuggerCmd(Cmd):
    intro = "欢迎使用开发者命令行\n"
    prompt = "debug -> "

    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

    def cmdloop(self, intro: Any | None = None) -> None:
        if not calculator.debug:
            QMessageBox.warning(calculator, __name__, "非调试模式无法启动")
            return
        os.system("title Debugger Cmd")
        return super().cmdloop(intro)

    def default(self, line: str) -> None:
        os.system(line)

    def do_exit(self, *ignoerd):
        """
        退出。
        """
        sys.exit(0)

    def do_exec(self, args: str):
        """
        运行代码。

        用法：exec [-l command] [-i] [-p attr]

            -l command        运行单行代码。
            -i                启动多行输入模式，运行多段代码。
            -p attr           输出指定的属性。

        多行输入模式命令： [#run] [#rewrite line] [#show] [#exit]

            #run              运行输入的代码。
            #rewrite line     重写第line行的代码。
            #show             展示所有代码，可以在使用#rewrite命令后确认代码是否准确。
            #exit             退出多行输入模式（不运行）。
        """
        args = args.split(" ")
        command = """"""
        if args[0] == "-l":
            for i in args[1:]:
                command += i + " "
            try:
                exec(command)
            except Exception as e:
                print("\nError: %s"%type(e))
                print(e)
                for i in e.args[1:]:
                    print(i)
                print()
        elif args[0] == "-i":
            commands = []
            line = 0
            while True:
                cmd = input("Line%s: "%line)
                if cmd == "#run":
                    break
                elif cmd.startswith("#rewrite"):
                    cmd = cmd.split(" ")
                    if not cmd[1].isdigit():
                        print("%s不是行数。"%cmd[1])
                        continue
                    if not len(commands) > int(cmd[1]):
                        print("没有行%s。"%cmd[1])
                        continue
                    rewrite = input("Line%s[rewrite]: "%cmd[1])
                    commands[int(cmd[1])] = rewrite + "\n"
                elif cmd == "#show":
                    print()
                    for i in range(len(commands)):
                        print("%s: %s"%(i, commands[i]), end="")
                    print()
                elif cmd == "#exit":
                    return
                else:
                    commands.append(cmd + "\n")
                    line += 1
            for i in commands:
                command += i
            try:
                exec(command)
            except Exception as e:
                print("\nError: %s\n"%type(e))
                print(e)
                for i in e.args[1:]:
                    print(i)
                print()
        elif args[0] == "-p":
            print(eval(args[1]))
        else:
            print("无效参数%s。"%args[0])
    
    def get_ui_attr(self, widget):
        names = []
        for i in dir(widget):
            if not i.startswith("__"):
                names.append("calculator.ui." + i)
        for i in names:
            try:
                for j in dir(eval(i)):
                    if not j.startswith("__"):
                        names.append(i + "." + j)
            except:
                break
        return names
    
    def get_class_attr(self, _class):
        functions = []
        for i in dir(_class):
            if not i.startswith("_"):
                functions.append("calculator." + i)
        return functions
    
    def complete_exec(self, text: str, line: str, begidx: int, endidx: int):
        if line.startswith("exec -l") or line.startswith("exec -p"):
            widgets = self.get_ui_attr(calculator.ui)
            functions = self.get_class_attr(calculator)
            complete = widgets + functions
            return [i for i in complete if i.startswith(text)]
        if line.startswith("exec"):
            return ["-l", "-i", "-p"]

debuggerCmd = DebuggerCmd()

start_debugger_cmd_action = QAction("启动开发者命令行", calculator.ui.functions_menu)
start_debugger_cmd_action.triggered.connect(lambda: debuggerCmd.cmdloop())

calculator.ui.functions_menu.addAction(start_debugger_cmd_action)
