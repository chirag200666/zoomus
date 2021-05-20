from datetime import datetime
import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UpdateV2TestCase))
    return suite


class UpdateV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.poll.MeetingsPollComponentV2(
            base_uri="http://foo.com",
            config={
                "api_key": "KEY",
                "api_secret": "SECRET",
                "version": util.API_VERSION_2,
            },
        )

    @responses.activate
    def test_create(self):
        responses.add(
            responses.PUT,
            "http://foo.com/meetings/ID/polls/POLLID",
        )
        response = self.component.update(
            id="ID", poll_id="POLLID", data={'questions': [{'name': 'Did you find the content relevant?', 'type': 'single', 'answers': ['5 - Strongly Agree', '4 - Somewhat Agree', '3 - Neutral', '2 - Somewhat Disagree', '1 - Strongly Disagree']}, {'name': 'Please rate the speaker on knowledge', 'type': 'single', 'answers': ['5 - Strongly Agree', '4 - Somewhat Agree', '3 - Neutral', '2 - Somewhat Disagree', '1 - Strongly Disagree']}, {'name': 'Please rate the speaker on teaching skills.', 'type': 'single', 'answers': ['5 - Strongly Agree', '4 - Somewhat Agree', '3 - Neutral', '2 - Somewhat Disagree', '1 - Strongly Disagree']}, {'name': 'Was the session interactive?', 'type': 'single', 'answers': ['5 - Strongly Agree', '4 - Somewhat Agree', '3 - Neutral', '2 - Somewhat Disagree', '1 - Strongly Disagree']}, {'name': 'Were all your questions addressed?', 'type': 'single', 'answers': ['5 - Strongly Agree', '4 - Somewhat Agree', '3 - Neutral', '2 - Somewhat Disagree', '1 - Strongly Disagree']}]}
        )
        self.assertEqual(
            response.request.body,
            '{"questions": [{"name": "Did you find the content relevant?", "type": "single", "answers": ["5 - Strongly Agree", "4 - Somewhat Agree", "3 - Neutral", "2 - Somewhat Disagree", "1 - Strongly Disagree"]}, {"name": "Please rate the speaker on knowledge", "type": "single", "answers": ["5 - Strongly Agree", "4 - Somewhat Agree", "3 - Neutral", "2 - Somewhat Disagree", "1 - Strongly Disagree"]}, {"name": "Please rate the speaker on teaching skills.", "type": "single", "answers": ["5 - Strongly Agree", "4 - Somewhat Agree", "3 - Neutral", "2 - Somewhat Disagree", "1 - Strongly Disagree"]}, {"name": "Was the session interactive?", "type": "single", "answers": ["5 - Strongly Agree", "4 - Somewhat Agree", "3 - Neutral", "2 - Somewhat Disagree", "1 - Strongly Disagree"]}, {"name": "Were all your questions addressed?", "type": "single", "answers": ["5 - Strongly Agree", "4 - Somewhat Agree", "3 - Neutral", "2 - Somewhat Disagree", "1 - Strongly Disagree"]}]}',
        )

    def test_requires_id(self):
        with self.assertRaisesRegexp(ValueError, "'id' must be set"):
            self.component.create()


if __name__ == "__main__":
    unittest.main()
