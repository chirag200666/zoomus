import datetime
import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PollsV2TestCase))
    return suite


class PollsV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.past_webinar.PastWebinarComponentV2(
            base_uri="http://www.foo.com",
            config={"version": util.API_VERSION_2, "token": "token"},
        )

    @responses.activate
    def test_can_list(self):
        responses.add(
            responses.GET, "http://www.foo.com/past_webinars/ID/polls",
        )
        self.component.get_polls(webinar_id="ID")
        expected_headers = {"Authorization": "Bearer token"}
        actual_headers = responses.calls[0].request.headers
        self.assertTrue(
            set(expected_headers.items()).issubset(set(actual_headers.items()))
        )


if __name__ == "__main__":
    unittest.main()
