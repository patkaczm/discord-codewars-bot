class HelpHandler:
    def __init__(self, handlers: []):
        self.handlers = handlers

    def help(self):
        return "/help - prints help for every handler"

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        if message == '/help':
            return self.__handle_help__()
        return None

    def __handle_help__(self):
        return f'```\n' + '\n'.join([h.help() for h in self.handlers]) + '\n```'
