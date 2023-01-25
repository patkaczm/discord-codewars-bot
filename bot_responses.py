import codewars


def handle_response(message) -> str:
    message = message.lower()
    api = codewars.CodewarsAPI()

    if message == 'hello':
        return "Hey there!"

    if message == '!help':
        return "`This is help message :)`"

    if 'exists' in message:
        user = message.replace('exists', '').strip()
        print(f'Check if user {user} exists')
        return f'User: {user} {"exists" if api.does_user_exist(user) else "does not exist"}'

    if 'done tasks' in message:
        user = message.replace('done tasks', '').strip()
        tasks = codewars.CodewarsTasks(api.get_user_done_tasks(user)).filter(language='python')
        formatter = codewars.CodewarsDoneTasksFormatter()
        return formatter.format(tasks, name=True, link=True)

