from attest import Tests, assert_hook
from redispacetests import protocol


suite = Tests()
suite.register(protocol.suite)


@suite.test
def boolean():
    assert True is not False