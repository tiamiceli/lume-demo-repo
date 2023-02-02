from setuptools import setup, find_packages
from os import path
import versioneer

cur_dir = path.abspath(path.dirname(__file__))

# parse requirements
with open(path.join(cur_dir, "requirements.txt"), "r") as f:
    requirements = f.read().split()

setup(
    name="lume-demo-package",
    author="Tia Miceli",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    #  license="...",
    install_requires=requirements,
    url="https://github.com/slaclab/lume-services-model-template",
    include_package_data=True,
    python_requires=">=3.8",
    entry_points={
        "orchestration": [
            "lume-demo-package.model=\
                lume-demo-package.model:LumeDemoModel",
            "lume-demo-package.flow=\
                lume-demo-package.flow:flow",
        ]
    },
)