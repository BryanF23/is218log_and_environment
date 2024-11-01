# app.py
class App:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def start(self):
        while True:
            command = input('> ')
            if command in self.commands:
                self.commands[command]()
            elif command == 'exit':
                print("Exiting the application.")
                break
            else:
                print(f"No such command: {command}")

# Define a greet command
def greet():
    print("Hello, World!")

# Main execution to register commands
if __name__ == '__main__':
    app = App()
    app.register_command('greet', greet)
    app.start()
