import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='usage_tracker',
    version='0.0.4',
    author='Omkar Konnur',
    author_email='omkar.konnur@redis.com',
    description='Track Usage of any python script using redis database',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mar1boroman/usage_tracker',
    project_urls = {
        "Bug Tracker": "https://github.com/mar1boroman/usage_tracker/issues"
    },
    license='MIT',
    packages=['usage_tracker'],
    install_requires=['redis'],
)