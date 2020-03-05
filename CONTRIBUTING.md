# Contribution Guidelines

## Before accepting merge requests

* `flake8 .` returns no code style check errors.
* Any `flake8` errors have been resolved or a `# noqa: <code>` comment added to each line on a case-by-case basis.
* `safety check -r requirements.txt` returns no requirement vulnerabilities.
* `piprot requirements.in` returns no outdated requirements.
* `pip-compile --upgrade` has generated an up to date `requirements.txt` file.
* Unit test coverage is sufficient and covers the lines changed in the merge request.
* Integration test coverage is sufficient and covers the lines changed in the merge request.
* Any interface or resource representation changes are reflected in the `swagger.json` specification.

## When creating new tags

* Follow the [Semantic Versioning 2.0.0](http://semver.org/) specification.

## When updating the changelog

* Follow the [changelog guiding principles](http://keepachangelog.com/en/1.0.0/#how).
* Follow the [Semantic Versioning 2.0.0](http://semver.org/) specification.
* Add links from each version number to git diff with previous version, e.g. `<repo>/compare/<last_version>...<this_version>`