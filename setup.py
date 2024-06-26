from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
    name="inventree-tui",
    version="0.1.6",
    auther="John Huff",
    description="Terminal UI for InvenTree",
    url='https://github.com/j-huff/inventree-tui',
    packages=find_packages(),
    install_requires=["textual","inventree","pydantic", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "inventree-tui = inventree_tui.entrypoint:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "inventree_tui": ["*.tcss"],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
