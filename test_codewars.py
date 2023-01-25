import pytest
from codewars import CodewarsAPI, CodewarsTasks
import responses


class TestCodewars():
    api = CodewarsAPI()
    non_existing_user = 'pknagato4xd'
    existing_user = 'pknagato4'
    user_done_tasks = {'totalPages': 1, 'totalItems': 48, 'data': [
        {'id': '54da539698b8a2ad76000228', 'name': 'Take a Ten Minutes Walk', 'slug': 'take-a-ten-minutes-walk',
         'completedLanguages': ['python'], 'completedAt': '2023-01-15T17:38:24.143Z'},
        {'id': '5d41e16d8bad42002208fe1a', 'name': 'More Zeros than Ones', 'slug': 'more-zeros-than-ones',
         'completedLanguages': ['python'], 'completedAt': '2023-01-15T17:29:31.246Z'},
        {'id': '5503013e34137eeeaa001648', 'name': 'Give me a Diamond', 'slug': 'give-me-a-diamond',
         'completedLanguages': ['python'], 'completedAt': '2023-01-15T16:52:29.099Z'},
        {'id': '5518a860a73e708c0a000027', 'name': 'Last digit of a huge number', 'slug': 'last-digit-of-a-huge-number',
         'completedLanguages': ['cpp', 'python'], 'completedAt': '2023-01-13T13:23:51.737Z'},
        {'id': '5511b2f550906349a70004e1', 'name': 'Last digit of a large number',
         'slug': 'last-digit-of-a-large-number', 'completedLanguages': ['cpp, c'],
         'completedAt': '2023-01-13T12:21:01.508Z'},
        {'id': '57b06f90e298a7b53d000a86', 'name': 'The Supermarket Queue', 'slug': 'the-supermarket-queue',
         'completedLanguages': ['c'], 'completedAt': '2023-01-13T10:36:03.651Z'}]}

    def setup_method(self):
        responses.get('https://www.codewars.com/api/v1/users/' + self.non_existing_user, json={
            'success': False, 'reason': 'not found'
        }, status=200)
        responses.get('https://www.codewars.com/api/v1/users/' + self.existing_user, json={
            'id': '5a5f0d4880eba80f9b00009a', 'username': 'pknagato4', 'name': 'Patryk Kaczmarek', 'honor': 465,
            'clan': 'BakcylBegin_Nokia2019', 'leaderboardPosition': 94576, 'skills': ['c;c++;python;'],
            'ranks': {'overall': {'rank': -5, 'name': '5 kyu', 'color': 'yellow', 'score': 640},
                      'languages': {'cpp': {'rank': -5, 'name': '5 kyu', 'color': 'yellow', 'score': 354},
                                    'python': {'rank': -5, 'name': '5 kyu', 'color': 'yellow', 'score': 283},
                                    'javascript': {'rank': -8, 'name': '8 kyu', 'color': 'white', 'score': 2},
                                    'c': {'rank': -8, 'name': '8 kyu', 'color': 'white', 'score': 8}}},
            'codeChallenges': {'totalAuthored': 0, 'totalCompleted': 48}
        }, status=200)
        responses.get('https://www.codewars.com/api/v1/users/{}/code-challenges/completed'.format(self.existing_user),
                      json=self.user_done_tasks, status=200)

    @responses.activate
    def test_does_user_exist_returns_false_when_user_does_not_exist(self):
        assert self.api.does_user_exist(self.non_existing_user) == False

    @responses.activate
    def test_does_user_exist_returns_true_when_user_does_exist(self):
        assert self.api.does_user_exist(self.existing_user) == True

    @responses.activate
    def test_get_user_done_tasks_returns_empty_list_when_user_does_not_exist(self):
        assert self.api.get_user_done_tasks(self.non_existing_user) == []

    @responses.activate
    def test_get_user_done_tasks_returns_not_empty_list_when_user_exists(self):
        assert self.api.get_user_done_tasks(self.existing_user) != []

    @responses.activate
    def test_get_user_done_tasks_returns_user_done_tasks_when_user_exists(self):
        assert self.api.get_user_done_tasks(self.existing_user) == self.user_done_tasks


class TestCodewarsTasks:
    user_done_tasks = {'totalPages': 1, 'totalItems': 48, 'data': [
        {'id': '54da539698b8a2ad76000228', 'name': 'Take a Ten Minutes Walk', 'slug': 'take-a-ten-minutes-walk',
         'completedLanguages': ['python'], 'completedAt': '2023-01-15T17:38:24.143Z'},
        {'id': '5d41e16d8bad42002208fe1a', 'name': 'More Zeros than Ones', 'slug': 'more-zeros-than-ones',
         'completedLanguages': ['python'], 'completedAt': '2023-01-15T17:29:31.246Z'},
        {'id': '5503013e34137eeeaa001648', 'name': 'Give me a Diamond', 'slug': 'give-me-a-diamond',
         'completedLanguages': ['python'], 'completedAt': '2023-01-15T16:52:29.099Z'},
        {'id': '5518a860a73e708c0a000027', 'name': 'Last digit of a huge number 2',
         'slug': 'last-digit-of-a-huge-number-2',
         'completedLanguages': ['cpp', 'python'], 'completedAt': '2023-01-13T13:23:51.737Z'},
        {'id': '5511b2f550906349a70004e1', 'name': 'Last digit of a large number',
         'slug': 'last-digit-of-a-large-number', 'completedLanguages': ['cpp', 'c'],
         'completedAt': '2023-01-13T12:21:01.508Z'},
        {'id': '57b06f90e298a7b53d000a86', 'name': 'The Supermarket Queue', 'slug': 'the-supermarket-queue',
         'completedLanguages': ['c'], 'completedAt': '2023-01-13T10:36:03.651Z'}]}
    python_tasks = {'54da539698b8a2ad76000228', '5d41e16d8bad42002208fe1a', '5503013e34137eeeaa001648',
                    '5518a860a73e708c0a000027'}

    cpp_tasks = {'5518a860a73e708c0a000027', '5511b2f550906349a70004e1'}
    c_tasks = {'57b06f90e298a7b53d000a86', '5511b2f550906349a70004e1'}

    def has_tasks_with_id(self, actual, expected):
        return actual.keys() == expected

    def test_empty_raw_input_raises_value_error(self):
        with pytest.raises(ValueError):
            CodewarsTasks({})

    def test_filter_language_returns_tasks_completed_in_such_language(self):
        tasks = CodewarsTasks(self.user_done_tasks)
        assert self.has_tasks_with_id(tasks.filter(language='python'), self.python_tasks)
        assert self.has_tasks_with_id(tasks.filter(language='cpp'), self.cpp_tasks)
        assert self.has_tasks_with_id(tasks.filter(language='c'), self.c_tasks)

# @todo tests for formatter