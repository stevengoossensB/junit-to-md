from setuptools import setup, find_packages

setup(
    name='junit_to_markdown',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'junit_to_markdown=junit_to_markdown.converter:convert_file',
        ],
    },
    author='Steven Goossens',
    author_email='steven@teamg.be',
    description='Convert JUnit XML reports to Markdown',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/stevengoossensB/junit-to-md',
)
