import setuptools
import os


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


def main():
    with open('README.md', 'r') as fp:
        readme = fp.read()

    setuptools.setup(
        name='cafeteria-simulation',
        version='1.0.1',
        description='Python package for cafe simulation',
        long_description=readme,
        long_description_content_type='text/markdown',
        url='https://github.com/m-star18/cafeteria-simulation',
        license='Apache Software License 2.0',
        author='Ryusei Ito',
        author_email='31807@toyota.kosen-ac.jp',
        packages=['cafe'],
        install_requires=read_requirements(),
        python_requires='>=3.6, <3.9',
    )


main()
