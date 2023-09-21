# real_time_transcribe
Use Pyaudio to catch speakers audio from Stereo Mixer, and then use Whisper to transcribe voice to text



## Install
1. make sure you have Stereo Mixer in the computer and enable it in recording.
2. create a Python=3.8 environment and use "pip install -r requirements.txt" to install require packages.
3. use "python tk.py -l {language} -d {delay time}" to run the program and it will create a windows start to show transcribes of computer speakers audio.
4. close the window and the program will terminate.



## Example

```console

python tk.py -l Japanese -d 5
```

-l or --language you can type English, Japanese or Chinese...
-d or --delay_time you can type a number less than 30, this means the length (seconds) of each audio clip, and each clip will send to whisper model to output texts.




## Future work 
1. separate audio data by the loudness (try not to split a sentense)
2. fix button not work issue when the tkinter user interface is transparent, so that i can start and end the program or changing config using user interface.
3. add some config like the model of whipser(currently medium), select recording device, font color and size? 
