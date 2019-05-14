from testCase.baidu_login import BaiDuLogin
import unittest
from result.testResult import TestResult


def run():
    tests = [BaiDuLogin('test_search')]
    test_result = TestResult()
    test_result.suite.addTests(tests)
    test_result.get_html_report()


run()
