from setuptools import setup, find_packages

version = "1.0.0"

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="intellichat",
    version=version,
    description="A convenient wrapper for OpenAI's Chat Completion API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Swas.py",
    author_email="cwswas.py@gmail.com",
    packages=find_packages(),
    url="https://github.com/CodeWithSwastik/intellichat",
    project_urls={
        "Issue tracker": "https://github.com/CodeWithSwastik/intellichat/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=["openai"],
    python_requires=">=3.8",
)