CONTRIBUTING
************

Introduction
============

To assure code quality and maintainability as well as tidiness of the repository, a few rules to be followed by contributors are in place.
This is especially important, since the goal of this project is to learn about, and gain experience in *collaborative* software development.
Contributors are thus asked to read and follow the instructions laid out in this document.

Since this is a course project, contributions from external contributors cannot be accepted at the moment.

Git Workflow
============

The MDCode project uses a `Shared Repository Model <https://docs.github.com/en/github/collaborating-with-pull-requests/getting-started/about-collaborative-development-models>`_.
Contributors can open different branches (e.g. feature, bugfix, experimental) of this repository and commit on, push to, pull from them. Once their work on said branch is done, a `Pull Request <https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`_ is submitted to merge into the development (`dev <https://github.com/JFxMachina/MDCode-solo/dev>`_) branch.
Pull requests for the `dev <https://github.com/JFxMachina/MDCode-solo/dev>`__ branch require at least two reviews to be accepted. Pull requests into the `main <https://github.com/JFxMachina/MDCode-solo/main>`__ are only allowd from the `dev <https://github.com/JFxMachina/MDCode-solo/dev>`__ branch and require at least three reviews to be accepeted. 

Branching
---------

While pushing to the main and dev branches is prohibited, contributors are free to create branches for feature development, testing, bug fixing etc.
For opening new branches, the following naming convention shall be used:

<TYPE>/<description-of-the-branch>

Where <TYPE> describes the nature of the branch and can be one of the following:

* BUG - For bug fixing
* WIP - For feature development
* EXP - For testing and experimental development

..
  # FIXEME : We should probably all agree on what to actually use.

The <description-of-the-branch> can be made up of multiple words separated by hyphens (`-`), however it should be kept as short as possible while still adequately describing what the branch is used for.

Commits
-------

Commits should cover individual but complete changes to the code base. E.g. when adding a module, commits should encompass the creation of for example a function, a class, or functionality. I.e. commit once your work on a code unit is done, and not mid way through editing. A good rule of thumb is, that you should be able to describe the changes in a simple sentence without having to go into too much details.

Commit messages should be as short as possible while still adequately describing the changes made and can either be made up of only a subject (brief description) or a subject and a body (detailed description). The subject should be written in the imperative form with the first letter capitalized and no punctuation at the end of the message. For reference, the reader is encouraged to take a look at `this blog post <https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide>`_.

Pull Requests
-------------

Pull requests into the `dev <https://github.com/JFxMachina/MDCode-solo/dev/>`__ branch should (generally) only be issued once work on one or more issues is complete. They will generally only be granted once all tests are passed and the changes have been reviewed by two individual contributors (Exceptions can be made).
Pull requests into the `main <https://github.com/JFxMachina/MDCode-solo/main/>`__ branch are only accepted from the dev branch and require reviews by three individual contributors.

If the pull request closes some issue, it should be marked in the message.

Reviewer should check, that all tests pass, there is reasonable unit test coverage for the added features and that code quality standards are met. If a pull request closes an issue, reviewers should check that the issue has been correctly and completely adressed and solved.


Coding Standard
================

Style Guide
-----------

Contributions should (within reason!) adhere to the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__ style guide for python code.
For this purpose using the `pycodestyle <https://pypi.org/project/pycodestyle/>`_ is recommended.
Contributors are encouraged to skim over the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ and to refer to it in case of uncertantiy.

Naming conventions
^^^^^^^^^^^^^^^^^^

The `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__ naming conventions are summarized bellow:


+----------------------------+--------------------+---------------------+
| Type                       | Public             | Internal            |
+============================+====================+=====================+
| Packages                   | lower              |                     |
+----------------------------+--------------------+---------------------+
| Modules                    | lower              | _lower              |
+----------------------------+--------------------+---------------------+
| Classes                    | CapWords           | _CapWords           |
+----------------------------+--------------------+---------------------+
| Exceptions                 | CapWords           |                     |
+----------------------------+--------------------+---------------------+
| Functions                  | lower_with_under() | _lower_with_under() |
+----------------------------+--------------------+---------------------+
| Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER    |
+----------------------------+--------------------+---------------------+
| Global/Class Variables     | lower_with_under   | _lower_with_under   |
+----------------------------+--------------------+---------------------+
| Instance Variables         | lower_with_under   | _lower_with_under   |
+----------------------------+--------------------+---------------------+
| Method Names               | lower_with_under() | _lower_with_under() |
+----------------------------+--------------------+---------------------+
| Function/Method Parameters | lower_with_under   |                     |
+----------------------------+--------------------+---------------------+
| Local Variables            | lower_with_under   |                     |
+----------------------------+--------------------+---------------------+


If it improves readability lower_with_under can be used for modules as well.

Module imports
^^^^^^^^^^^^^^

Star (``*``) imports eg.
::

	from <somepackage>.<some_module> import *

are not to be used, as this pollutes the namespace, interferes with linting and generally makes the code harder to understand and less maintainable.

Testing
-------

Unit test for new code units should be written in parallel to the code units themselves.
Reviewers should check, whether code submitted in pull requests has sufficient test coverage.

Test modules (files containing tests) can contain tests for multiple different code units. They must be named and placed in the tests folder or one of its subfolders according to the following scheme:

If the test module contains (amongst others) a test testing the entire module 'some_module' in package 'somepackage' it is placed at
::

	'tests/<somepackage>/<some_module>_test.py'

If, on the other hand, the test module only contains tests for a specific part of the module (e.g. a class 'SomeClass' or a function 'some_function') it is placed at
::

	'tests/<somepackage>/<some_module>_<SomeClass>_test.py'

or::

	'tests/<somepackage>/<some_module>_<some_function>_test.py'

respectively.

To run the tests, call pytest from the project root directory.

Documentation
-------------

Inline Documentation
^^^^^^^^^^^^^^^^^^^^

Inline documentation for new code units should be written in parallel to the code units themselves.
While docstrings for small code units (functions, classes etc.) that are only used within the module can be omitted,
all code units that are accessed from other modules or scripts should at least have a basic docstring.

For functions the docstring should contain a brief and an extended description, a list of the expected arguments as well as a list of the return values.
If arguments are modified by the function, it should be noted as well.

For classes the docstring should contain a brief and an extended description. Eventual class and instance attributes should be documented as well.

For more information on how to proprely document python code, contributors are encouraged to skim overthe section on comments in `PEP 8 <https://www.python.org/dev/peps/pep-0008/#comments>`__, `PEP 257 - Docstring Conventrions <https://www.python.org/dev/peps/pep-0257/>`_, and the section on Abstract Syntax Mining in `PEP 258 <https://www.python.org/dev/peps/pep-0258/#ast-mining>`_ in which the types of docstrings that are included in automatic documentation generation are explained.
For a quick guide on writing reStructuredText, please refer to the `Sphinx and RST syntax guide <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_.

Reviewers should check, whether code submitted in pull requests has sufficient documentation coverage.

To build the documentation locally, go to the doc directory and run
::

	source run_sphinx.sh

Code Tags
^^^^^^^^^

Code annotation using code tags is encouraged. For a quick overview of the idea, please refer to `PEP350 (rejected) <https://www.python.org/dev/peps/pep-0350/>`__.

Code tags used in this code base are:

* TODO (To do: Informal tasks/features that are pending completion.)
* FIXME (Fix me: Areas of problematic or ugly code needing refactoring or cleanup.)
* NOTE (Notes: Something readers should know. General catch all tag.)
* BUG (Bugs: Reported defects tracked in bug database.)
* SEE (See: Pointers to other code, web link, etc.)
* TEST (Tests: Requires testing.)
* IDEA (Ideas: Possible future enhancement.)
* ??? (Questions: Something is not clear.)
* !!! (Alerts: Needs attention.)

Contributors are asked to stick to these without variation, as having a list of the actually used code tags allows for quick lookup e.g. using grep. However suggestions for additions are welcome.

Useful links and references
===========================

Git and GitHub

* `GitHub Docs <https://docs.github.com/en>`__
* `Git Pro <https://git-scm.com/book/en/v2>`__ and `Git Reference Manual <https://git-scm.com/docs>`__

Python

* `The Hitchhiker's Guide to Python <https://docs.python-guide.org/>`__
* `The Python Language Reference <https://docs.python.org/3/reference/>`__
* `PEP 8 - Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`__

reStructuredText

* `Sphinx and RST Syntax Guide <https://thomas-cokelaer.info/tutorials/sphinx/index.html>`__
* `Sphinx reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
* `DOCX 2 RST Converter <https://alldocs.app/convert-word-docx-to-restructured-text>`__

Automated documentation (Sphinx)

* `SPHINX Python Documentation Generator <https://www.sphinx-doc.org/en/master/>`__

Automated testing (PyTest)

* `PyTest Documentation <https://docs.pytest.org/>`__

Core 3rd party libraries

* `ASE (Atomic Simulation Environment) <https://wiki.fysik.dtu.dk/ase/>`__
* `ASAP (Atomic SimulAtion Program / As Soon As Possible) <https://wiki.fysik.dtu.dk/asap>`__

Course page

* `CSEP course Page <https://mdi.gitlab-pages.liu.se/collab_proj_course.html>`__
