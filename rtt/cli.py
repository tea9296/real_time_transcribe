import click


@click.group()
def rtt():

    pass


@click.command()
@click.option("--language", "-l", help="Input file path", default="English")
@click.option("--delay_time",
              "-d",
              help="time for record a audio file",
              default=3)
@click.option("--model", "-m", help="model for transcribe", default="medium")
def stream(language: str, delay_time: int, model: str):

    import tkinter as tk
    from tkinter import ttk
    from rtt.process import record_audio, process_audio
    import threading

    app = tk.Tk()
    app.title("Real-Time Transcription")
    app.geometry("1000x200")  # set window size
    #app.attributes("-alpha", 0.1)
    app.attributes("-transparentcolor", '#000001')
    app.config(bg="#000001")
    app.wm_attributes('-topmost', 1)  # bring window to front

    transcribed_text = tk.StringVar()
    transcribed_label = ttk.Label(app,
                                  textvariable=transcribed_text,
                                  font=("Arial", 24),
                                  background="#000001",
                                  foreground="white")
    transcribed_label.pack(fill="both", expand=True)

    should_stop_threads = True

    #def start():
    #global should_stop_threads
    record_thread = threading.Thread(target=record_audio,
                                     args=(int(delay_time),
                                           should_stop_threads))
    process_thread = threading.Thread(target=process_audio,
                                      args=(transcribed_text, language,
                                            should_stop_threads, model))
    record_thread.setDaemon(True)
    process_thread.setDaemon(True)
    record_thread.start()
    process_thread.start()

    app.mainloop()


@click.command()
@click.option("--url", "-u", help="Youtube video url")
@click.option("--output_file",
              "-o",
              help="output file name, default youtube title",
              default="")
@click.option("--model", "-m", help="model for transcribe", default="medium")
@click.option("--language", "-l", help="Input file path", default="English")
def yt(url: str, output_file: str, model: str, language: str):
    import rtt.yt_process as yt

    transcription = yt.process_youtube_video(url, output_file, model, language)

    print(transcription)


@click.command()
@click.option("--input_file", "-i", help="wav file path")
@click.option("--output_file", "-o", help="output file name", default="")
@click.option("--model", "-m", help="model for transcribe", default="medium")
@click.option("--language", "-l", help="Input file path", default="English")
def wav(input_file: str, output_file: str, model: str, language: str):
    import rtt.yt_process as yt

    transcription = yt.process_wav_audio(input_file, output_file, model,
                                         language)

    print(transcription)


rtt.add_command(stream)
rtt.add_command(yt)
rtt.add_command(wav)

if __name__ == '__main__':
    rtt()
