"""
Setup script for the Job Application AI Agent package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="ai-job-finder",
    version="0.1.0",
    author="Bhavana Goud",
    author_email="bhavanagoud111@github.com",
    description="AI-powered job application automation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhavanagoud111/AI-Job-finder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "job-apply-ai=job_apply_ai.__main__:main",
        ],
    },
    include_package_data=True,
) 