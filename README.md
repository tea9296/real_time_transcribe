# real_time_transcribe
Use Pyaudio to catch speakers audio from Stereo Mixer, and then use Whisper to transcribe voice to text. 
Also can input a youtube url and get the transcription.

1. "rtt stream"  to open a tkinter ui and show real time transcription
2. "rtt yt  -u  {url}"  given a youtube video url and transcribe it into docx file.


## GPU
to use GPU, need to install torch with cuda compatible version
install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

## Install
1. make sure you have Stereo Mixer in the computer and enable it in recording.
2. use pip install git+https://github.com/tea9296/real_time_transcribe.git  to install the rtt package.
3. use "rtt stream -l {language} -d {delay_time}"  to open a tkinter ui and show real time transcription
4. use "rtt yt  -u {url} -o {output_file_name}"  given a youtube video url and transcribe it into docx file.
5. use "rtt wav -i {wav file path} -o {output_file_name}" to transcribe a .wav file.


## Example

```console

rtt stream -l Japanese -d 5
```

-l or --language you can type English, Japanese or Chinese...
-d or --delay_time you can type a number less than 30, this means the length (seconds) of each audio clip, and each clip will send to whisper model to output texts.



```console

rtt yt -u https://www.youtube.com/watch?.... -o tsp.docx
rtt yt -u https://www.youtube.com/watch?.... -o tsp.srt -l Chinese
```
-u or --url the youtube url link.
-o or --output_file the output .docx file name, default is the title of youtube url link. If the extension is .srt or .txt, will save into text file with timestamps.
-l or --language the language. Chinese, English or Japanese... 


## Future work 
1. separate audio data by the loudness (try not to split a sentense)
2. fix button not work issue when the tkinter user interface is transparent, so that i can start and end the program or changing config using user interface.
3. add some config like the model of whipser(currently medium), select recording device, font color and size? 
