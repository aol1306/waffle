class CommandHandler:
    def handle_command(this, command):
        print("Handling command", command)
        if command == "exit":
            exit()
        return "ACK"