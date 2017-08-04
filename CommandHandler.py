import subprocess

class CommandHandler:
    def __init__(self):
        self.state = "normal"
        print("state: normal")

    def handle_command(self, command):
        if self.state == "normal":    
            return self.handle_normal_command(command)
        elif self.state == "shell":
            return self.handle_shell_command(command)
        
    def handle_normal_command(self, command):
        print("Handling normal command", command)
        if command == "exit":
            exit()
        if command == "shell":
            self.state = "shell"
            print("state: shell")
            return "Switched to shell"
        else:
            return "Unknown command"
            
    def handle_shell_command(self, command):
        print("Handling shell command", command)
        if command == "exit":
            self.state = "normal"
            print("state: normal")
            return "exit"
        else:
            return str(subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True))