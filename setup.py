from setuptools import setup

setup(
    name='rtt',
    version='0.2',
    description="use whisper and pyaudio to record audio and do transcription",
    author='chih chuan chang',
    author_email='tea9296@gmail.com',
    install_requires=[
        'torch==2.2.0', 'torchvision==0.17.0', 'torchaudio==2.2.0', 'demucs',
        'click', 'openai-whisper', 'pyaudio==0.2.13', 'numpy>=1.24.4',
        'pytubefix', 'python-docx'
    ],
    packages=['rtt'],
    entry_points={'console_scripts': ['rtt = rtt.cli:rtt']})
