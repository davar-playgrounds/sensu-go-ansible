from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from ansible_collections.sensu.sensu_go.plugins.module_utils import (
    arguments,
)


class TestGetSpecPayload:
    def test_no_key(self):
        params = dict(
            name="name",
            key="value"
        )

        assert arguments.get_spec_payload(params) == dict()

    def test_spec_payload(self):
        params = dict(
            name="name",
            key="value",
        )

        assert arguments.get_spec_payload(params, "key") == dict(
            key="value",
        )


class TestGetMutationPayload:
    def test_no_key(self):
        params = dict(
            auth=dict(
                namespace="space"
            ),
            name="name",
        )

        assert arguments.get_mutation_payload(params) == dict(
            metadata=dict(
                name="name",
                namespace="space",
            ),
        )

    def test_wanted_key(self):
        params = dict(
            auth=dict(
                namespace="space"
            ),
            name="name",
            key="value",
        )

        assert arguments.get_mutation_payload(params, "key") == dict(
            key="value",
            metadata=dict(
                name="name",
                namespace="space",
            ),
        )

    def test_labels(self):
        params = dict(
            auth=dict(
                namespace="space"
            ),
            name="name",
            labels=dict(
                some="label",
                numeric=3,
            ),
        )

        assert arguments.get_mutation_payload(params) == dict(
            metadata=dict(
                name="name",
                namespace="space",
                labels=dict(
                    some="label",
                    numeric="3",
                ),
            ),
        )

    def test_annotations(self):
        params = dict(
            auth=dict(
                namespace="space"
            ),
            name="name",
            annotations=dict(
                my="Annotation",
                number=45,
            ),
        )

        assert arguments.get_mutation_payload(params) == dict(
            metadata=dict(
                name="name",
                namespace="space",
                annotations=dict(
                    my="Annotation",
                    number="45",
                ),
            ),
        )