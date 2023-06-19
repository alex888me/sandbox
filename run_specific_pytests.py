import pytest

tests_to_run = {
    'path/to/test_script_1.py': ['test_function_1', 'test_function_2'],
    'path/to/test_script_2.py': ['TestClass.test_method_1', 'TestClass.test_method_2']
}


def run_tests(tests):
    for test_script, test_list in tests.items():
        test_args = [f'{test_script}::{test_name}' for test_name in test_list]
        pytest.main(test_args)


run_tests(tests_to_run)
