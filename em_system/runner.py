from typing import Self


class PytestTestRunner:
    """Runs pytest to discover and run tests."""

    QUIET = 1
    VERBOSE = 2
    ALL = 3

    def __init__(
        self: Self,
        verbosity: int = 1,
        failfast: bool = False,
        keepdb: bool = False,
        **kwargs: dict,
    ) -> None:
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb
        self.kwargs = kwargs

    @property
    def verbosity_level(self: Self) -> str:
        if self.verbosity == self.QUIET:
            return "--quiet"
        if self.verbosity == self.VERBOSE:
            return "--verbose"
        if self.verbosity == self.ALL:
            return "-vv"
        return ""

    def run_tests(self: Self, test_labels: list) -> any:
        """Run pytest and return the exitcode.
        It translates some of Django's test command option to pytest's.
        """

        import pytest

        argv = [self.verbosity_level]
        if self.failfast:
            argv.append("--exitfirst")
        if self.keepdb:
            argv.append("--reuse-db")

        argv.extend(test_labels)
        return pytest.main(argv)
