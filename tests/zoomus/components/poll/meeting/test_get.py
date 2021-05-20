from datetime import datetime
import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetV2TestCase))
    return suite


class GetV2TestCase(unittest.TestCase):
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
    def test_can_list(self):
        responses.add(responses.GET, "http://foo.com/meetings/ID/polls/POLLID")
        self.component.get(id="ID", poll_id="POLLID")


if __name__ == "__main__":
    unittest.main()
