import requests
from datetime import datetime


class CodewarsAPI:

    def does_user_exist(self, username):
        resp = requests.get('https://www.codewars.com/api/v1/users/' + username)
        return resp.status_code == 200 and 'username' in resp.json()

    def get_user_done_tasks(self, username):
        if not self.does_user_exist(username):
            return []
        resp = requests.get('https://www.codewars.com/api/v1/users/{}/code-challenges/completed'.format(username))
        return resp.json() if resp.status_code == 200 else {}


class CodewarsTasks:
    def __init__(self, tasks_json):
        try:
            self.tasks = {task['id']: {
                'name': task['name'],
                'languages': task['completedLanguages'],
                'completion_time': datetime.strptime(task['completedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
            } for task in tasks_json['data']}
        except Exception:
            msg = 'Error cannot parse tasks_json from codewars'
            print(msg)
            raise ValueError(msg)

    def filter(self, **kwargs):
        filtered = {}
        if 'language' in kwargs:
            for task_id, task in self.tasks.items():
                if kwargs['language'] in task['languages']:
                    filtered[task_id] = task

        return filtered


class CodewarsDoneTasksFormatter:
    def format(self, tasks, **kwargs):
        formatted = []
        name = False
        id = False
        languages = False
        completion_time = False
        link = False
        if 'name' in kwargs and kwargs['name']:
            name = True
        if 'id' in kwargs and kwargs['id']:
            id = True
        if 'languages' in kwargs and kwargs['languages']:
            languages = True
        if 'completion_time' in kwargs and kwargs['completion_time']:
            completion_time = True

        if 'link' in kwargs and kwargs['link']:
            link = True

        for task_id, task in tasks.items():
            formatted.append({
                **({'id': task_id} if id else {}),
                **({'name': task['name']} if name else {}),
                **({'languages': task['languages']} if languages else {}),
                **({'completion_time': task['completion_time']} if completion_time else {}),
                **({'link': f'https://www.codewars.com/kata/{task_id}'} if link else {}),
            })

        formattedStr = ''

        for elem in formatted:
            for val in elem.values():
                formattedStr += val + ' '
            formattedStr += '\n'

        return formattedStr
