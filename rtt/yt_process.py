
import subprocess
from pytube import YouTube
from pathlib import Path
import whisper
import datetime
import shutil
from docx import Document


# Function to download a YouTube video
def download_video(url, output_dir):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    download_path = Path(output_dir)
    download_path.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
    # use datetime to name the file
    title = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = stream.title
    output_file = download_path / (title + ".mp4")
    stream.download(output_path=download_path, filename=title+".mp4")
    return output_file, file_name

# Function to convert video to WAV using FFmpeg
def convert_to_wav(input_file, output_file):
    subprocess.run(["ffmpeg", "-i", input_file, "-acodec", "pcm_s16le", "-ar" ,"16000", output_file])
    
# Function to filter vocals using Demucs
def filter_vocals(input_file):
    subprocess.run(["demucs", "--two-stems=vocals", input_file])

# Function to transcribe audio using OpenAI Whisper
def transcribe_audio(input_file):
    model = whisper.load_model("medium")
    result = model.transcribe(input_file.__str__(), initial_prompt="以下是普通話的句子。",verbose=True)
    # import json
    # with open('transcription.json', 'w',encoding='utf-8') as f:
    #     json.dump(result, f)

    return result['text']


def save_doc(text, output_file_name):
    # Create a new document
    doc = Document()

    # Add a title to the document
    doc.add_heading(output_file_name.split('.')[:-1], 0)

    # Your transcription content, including both Chinese and English
    transcription = text.replace('。', '。\n\n').replace('!', '!\n\n').replace('?', '?\n\n').replace('.','.\n\n')

    # Add the transcription content to the document
    doc.add_paragraph(transcription)

    # Save the document to a file
    doc.save(output_file_name)
    
    return 


# Main function to perform the entire process
def process_youtube_video(url:str, output_file_name:str = ""):
    
    output_dir = "temp"
    
    
    
    video_file, file_name = download_video(url, output_dir)
    wav_file = Path(output_dir) / (video_file.stem + ".wav")
    
    
    
    if output_file_name=="":
        output_file_name = "./" + file_name.replace('/','_').replace(' ','') 
    
    if output_file_name.split('.')[-1] != 'docx':
        output_file_name += '.docx'
    
    
    
    
    separated_audio = f"./separated/htdemucs/{video_file.stem}/vocals.wav"
    

    convert_to_wav(video_file, wav_file)
    filter_vocals(wav_file)
    transcription = transcribe_audio(separated_audio)

    # Delete temporary files
    video_file.unlink()
    wav_file.unlink()
    #separated_audio.unlink()
    try:      
        shutil.rmtree('./separated/')
        
    except OSError as e:
        print(f"Error: {e}")
    
    
    save_doc(transcription, output_file_name)
    
    
    return transcription

# # Example usage:
# video_url = "https://www.youtube.com/watch?v=J6MUvl8P3Us"
# ve = "https://www.youtube.com/watch?v=rvZWLTtEyoU"

# transcription = process_youtube_video(ve)
# print("Transcription:", transcription)

