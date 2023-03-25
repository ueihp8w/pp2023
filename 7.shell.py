import subprocess
import re

if __name__=="__main__":
    while True:
        s = input()
        if (s == "exit"): break
        if (s.strip() == ""): continue
        commands = s.split("|")
        input_stream = None
        output_stream = None
        for i, command in enumerate(commands):
            cmd = re.split(r"([<>])", command)

            if (i == 0) and ("<" in cmd):
                input_file = cmd.pop(cmd.index("<") + 1).strip()
                input_stream = open(input_file, "r")
            if (i == len(commands) - 1) and (">" in cmd):
                output_file = cmd.pop(cmd.index(">") + 1).strip()
                output_stream = open(output_file, "w")
            cmd = cmd[0].strip().split()
            if (i < (len(commands) - 1)):
                process = subprocess.Popen(cmd, stdin=input_stream, stdout=subprocess.PIPE)
            else:
                process = subprocess.Popen(cmd, stdin=input_stream, stdout=output_stream)
            input_stream = process.stdout

        if input_stream is not None:
            input_stream.close()

        if output_stream is not None:
            output_stream.close()