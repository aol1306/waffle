import subprocess

class CommandHandler:
    def __init__(this):
        this.state = "normal"
        print("state: normal")

    def handle_command(this, command):
        if this.state == "normal":    
            return this.handle_normal_command(command)
        elif this.state == "shell":
            return this.handle_shell_command(command)
        
    def handle_normal_command(this, command):
        print("Handling normal command", command)
        if command == "exit":
            exit()
        if command == "shell":
            this.state = "shell"
            print("state: shell")
            return "Switched to shell"
        else:
            return "Unknown command"
            
    def handle_shell_command(this, command):
        print("Handling shell command", command)
        if command == "exit":
            this.state = "normal"
            print("state: normal")
            return "exit"
        else:
            return str(subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True))