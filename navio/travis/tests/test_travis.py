import pytest
import os
import sys


class TestImport:

    def test_import(self):
        import navio.travis
        from navio.travis import Travis


class Test:


    def test_is_travis(self):
        from navio.travis import Travis

        assert not Travis().is_travis()

        os.environ['TRAVIS'] = 'true'
        assert Travis().is_travis()

        os.environ['TRAVIS'] = 'false'
        assert not Travis().is_travis()

        os.environ['TRAVIS'] = '???'
        assert not Travis().is_travis()

    def test_is_pull_request(self):
        from navio.travis import Travis

        assert not Travis().is_pull_request()

        os.environ['TRAVIS'] = 'true'

        os.environ['TRAVIS_PULL_REQUEST'] = 'true'
        assert Travis().is_pull_request()

        os.environ['TRAVIS_PULL_REQUEST'] = 'false'
        assert not Travis().is_pull_request()

        os.environ['TRAVIS_PULL_REQUEST'] = '???'
        assert not Travis().is_pull_request()

    def test_branch(self):
        from navio.travis import Travis

        os.environ['TRAVIS'] = 'true'

        assert Travis().branch() is None

        os.environ['TRAVIS_BRANCH'] = 'master'
        assert 'master' == Travis().branch()

        os.environ['TRAVIS_BRANCH'] = 'prod'
        assert 'prod' == Travis().branch()

    def test_commit_hash(self):
        from navio.travis import Travis

        os.environ['TRAVIS'] = 'true'

        assert Travis().commit_hash() is None

        os.environ['TRAVIS_COMMIT'] = '1f510ab451bb4'
        assert '1f510ab451bb4' == Travis().commit_hash()

        os.environ['TRAVIS_COMMIT'] = '04124124bcb131'
        assert '04124124bcb131' == Travis().commit_hash()
