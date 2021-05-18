"""Zoom.us REST API Python Client"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class PastWebinarComponentV2(base.BaseComponent):
    def list(self, **kwargs):
        util.require_keys(kwargs, "webinar_id")
        kwargs["webinar_id"] = util.encode_uuid(kwargs.get("webinar_id"))
        return self.get_request(
            "/past_webinars/{}/instances".format(kwargs.get("webinar_id")),
            params=kwargs,
        )

    def get_polls(self, **kwargs):
        util.require_keys(kwargs, "webinar_id")
        kwargs["webinar_id"] = util.encode_uuid(kwargs.get("webinar_id"))
        return self.get_request(
            "/past_webinars/{}/polls".format(kwargs.get("webinar_id"))
        )
