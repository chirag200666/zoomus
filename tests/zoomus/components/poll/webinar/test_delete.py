from datetime import datetime
import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DeleteV2TestCase))
    return suite


class DeleteV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.poll.WebinarPollComponentV2(
            base_uri="http://foo.com",
            config={
                "api_key": "KEY",
                "api_secret": "SECRET",
                "version": util.API_VERSION_2,
            },
        )

    @responses.activate
    def test_can_list(self):
        responses.add(responses.DELETE, "http://foo.com/webinars/ID/polls/POLLID")
        self.component.delete(id="ID", poll_id="POLLID")


if __name__ == "__main__":
    unittest.main()
