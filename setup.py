from setuptools import setup

req_file = "requirements.txt"
with open(req_file, encoding="utf-8") as f:
    requirements = f.read().splitlines()
setup(
    name='rtt',
    version='0.3',
    description="use whisper and pyaudio to record audio and do transcription",
    author='chih chuan chang',
    author_email='tea9296@gmail.com',
    install_requires=requirements,
    packages=['rtt'],
    entry_points={'console_scripts': ['rtt = rtt.cli:rtt']})
