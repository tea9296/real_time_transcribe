# whisper # https://github.com/openai/whisper
import pyaudio
import whisper
import numpy as np
import queue

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
REMAIN_LINE = 5
RATE = 16000
# Create a queue for storing audio data
global audio_queue
audio_queue = queue.Queue()


def get_device_index(p):
    dev_index = 2
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        #print(dev)
        if dev['hostApi']==0 and ('立體聲混音' in dev['name'] or \
            '立体声混音' in dev['name'] or 'Stereo Mix' in dev['name']) :
            dev_index = i
            #print(dev)
            return dev_index
    return dev_index


def create_audio_stream(record_sec: int = 3):
    record_sec = int(record_sec)
    p = pyaudio.PyAudio()

    dev_index = get_device_index(p)

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=dev_index,
                    frames_per_buffer=RATE * record_sec)

    return stream


# Function to continuously record audio and put it into the queue
def record_audio(record_sec: int = 3, should_stop_threads: bool = True):

    stream = create_audio_stream(record_sec)

    while should_stop_threads:
        data = stream.read(RATE * record_sec)
        audio = np.frombuffer(data, np.int16).astype(np.float32) / 32768
        audio = whisper.pad_or_trim(audio)
        audio_queue.put(audio)


# Function to process audio data from the queue and perform speech-to-text
def process_audio(transcribed_text,
                  language: str = "English",
                  should_stop_threads: bool = True,
                  model_name: str = "medium"):

    model = whisper.load_model(set_model_name(model_name))
    content_text = []
    while should_stop_threads:
        audio = audio_queue.get()
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(fp16=False, language=language)
        result = whisper.decode(model, mel, options)
        # PRINT LAST 5 LINES
        if "謝謝觀看" in result.text or "Thank you for watching!" in result.text:
            continue
        else:
            content_text.append(result.text)
            content_text = content_text[-REMAIN_LINE:]
            transcribed_text.set('\n'.join(content_text))

        print(result.text)


def set_model_name(model_name: str):

    all_model = whisper.available_models()

    if model_name in all_model:
        return model_name
    return "medium"
