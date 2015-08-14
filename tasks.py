from invoke import run, task

import shutil
import os


class Config:
    dirs = {
        "git": "./.git",
        "venv": "./ve",
        "OSdata": "./tests/data",
    }
    flake8 = {
        "ignore": "E121,E128,E221,E272,E501,W191",
        "max_compl": 10,
    }
    results = {
        "test": "test.xml",
        "lint": "lint.out",
        "fail": "failures.list",
        "osdb": "OSpostcodes.db"
    }


@task
def genosdb():
    run("python tests/prepare_os_data.py")


@task
def test(osdb=False, report=False):
    run("python -m pytest {} {}".format(
        "--osdb" if osdb else "",
        "--junitxml={}".format(Config.results["test"]) if report else ""
    ))


@task
def lint():
    run("python -m flake8 . --ignore={} --exclude={} --max-complexity={} | tee {}".format(
        Config.flake8["ignore"],
        Config.dirs["venv"],
        Config.flake8["max_compl"],
        Config.results["lint"]
    ))


@task
def clean():
    files_to_delete = [] + list(Config.results.values())
    dirs_to_delete = ["__pycache__"]

    for root, dirs, files in os.walk("."):
        for exclusion in Config.dirs.values():
            dirname = os.path.split(exclusion)[1]
            if dirname in dirs:
                dirs.remove(dirname)

        for name in files:
            if name in files_to_delete:
                os.remove(os.path.join(root, name))
        for name in dirs:
            if name in dirs_to_delete:
                shutil.rmtree(os.path.join(root, name))
