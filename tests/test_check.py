from precommit.scripts.poetry_package_version_checker import check_version


def test_check():
    assert check_version() ==True
