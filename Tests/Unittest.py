


# # run_tests.py
# import unittest
# import io
# import sys
# import requests
# import json

# def add(x, y):
#     return x + y

# class SimpleTest(unittest.TestCase):
#     @unittest.skip("demonstrating skipping")
#     def test_add1(self):
#         self.assertEqual(add(4, 5), 9)

# if __name__ == '__main__':
#     # Capture the test results
#     test_output = io.StringIO()
#     runner = unittest.TextTestRunner(stream=test_output, verbosity=2)
#     unittest.main(testRunner=runner, exit=False)

#     # Print the results to the console (optional)
#     print(test_output.getvalue())

#     # Send the results to Slack via Webhook
#     SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

#     # Construct the message payload
#     slack_message = {
#         'text': f"Test Results:\n```\n{test_output.getvalue()}\n```"
#     }

#     # Send the message to the Slack webhook URL
#     response = requests.post(
#         SLACK_WEBHOOK_URL, 
#         data=json.dumps(slack_message),
#         headers={'Content-Type': 'application/json'}
#     )

#     if response.status_code != 200:
#         raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")



# # import unittest
# # import io
# # import sys
# # import requests
# # import json

# # def add(x, y):
# #     return x + y

# # class SimpleTest(unittest.TestCase):
# #     @unittest.skip("demonstrating skipping")
# #     def test_add1(self):
# #         self.assertEqual(add(4, 5), 9)

# # if __name__ == '__main__':
# #     # Capture the test results
# #     test_output = io.StringIO()
# #     runner = unittest.TextTestRunner(stream=test_output, verbosity=2)
# #     unittest.main(testRunner=runner, exit=False)

# #     # Print the results to the console (optional)
# #     print(test_output.getvalue())

# #     # Send the results to Slack via Webhook
# #     SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

# #     # Construct the message payload
# #     slack_message = {
# #         'text': f"Test Results:\n```\n{test_output.getvalue()}\n```"
# #     }

# #     # Send the message to the Slack webhook URL
# #     response = requests.post(
# #         SLACK_WEBHOOK_URL, 
# #         data=json.dumps(slack_message),
# #         headers={'Content-Type': 'application/json'}
# #     )

# #     if response.status_code != 200:
# #         raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")



import unittest
import io
import sys
import requests
import json

def add(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_add1(self):
        self.assertEqual(add(4, 5), 9)

if __name__ == '__main__':
    # Capture the test results
    test_output = io.StringIO()
    runner = unittest.TextTestRunner(stream=test_output, verbosity=2)
    unittest.main(testRunner=runner, exit=False)

    # Print the results to the console (optional)
    print(test_output.getvalue())

    # Send the results to Slack via Webhook
    SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

    # Construct the message payload
    slack_message = {
        'text': f"Test Results:\n```\n{test_output.getvalue()}\n```"
    }

    # Send the message to the Slack webhook URL
    response = requests.post(
        SLACK_WEBHOOK_URL, 
        data=json.dumps(slack_message),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
