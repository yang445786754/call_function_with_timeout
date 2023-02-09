import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="call_function_with_timeout", 
    version="1.1.1",
    author="Tony_9410",
    author_email="tony_9410@foxmail.com",
    description="Python Call function with timeouts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yang445786754/call_function_with_timeout",
    project_urls={
        'Homepage': 'https://github.com/yang445786754/call_function_with_timeout',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['thread-with-results'],
    setup_requires=['wheel'],
)
