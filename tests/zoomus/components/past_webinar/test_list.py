import datetime
import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ListV2TestCase))
    return suite


class ListV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.past_webinar.PastWebinarComponentV2(
            base_uri="http://foo.com", config={"api_key": "KEY", "api_secret": "SECRET"}
        )

    @responses.activate
    def test_can_list(self):
        responses.add(
            responses.GET, "http://foo.com/past_webinars/ID/instances?webinar_id=ID"
        )
        self.component.list(webinar_id="ID")

    def test_requires_webinar_id(self):
        with self.assertRaisesRegexp(ValueError, "'webinar_id' must be set"):
            self.component.list()


if __name__ == "__main__":
    unittest.main()
