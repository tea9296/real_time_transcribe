import tkinter as tk
from tkinter import ttk
import threading
import argparse
from process import record_audio, process_audio

# Create the Tkinter app
DEFAULT_LANGUAGE = "English"
DEFAULT_TIME_DELAY = 3
app = tk.Tk()
app.title("Real-Time Transcription")
app.geometry("1000x200") # set window size
#app.attributes("-alpha", 0.1)
app.attributes("-transparentcolor", '#000001')
app.config(bg="#000001")
app.wm_attributes('-topmost', 1) # bring window to front




# # Language selection dropdown
# language_label = ttk.Label(app, text="Select Language:")
# language_label.pack(side="left")
# languages = ["English", "Japanese", "Chinese"]  # Add more languages as needed
# language_var = tk.StringVar()
# language_select = ttk.Combobox(app, textvariable=language_var, values=languages)
# language_select.pack(side="left")
# language_select.set(DEFAULT_LANGUAGE)

# # Delay time input
# delay_label = ttk.Label(app, text="Delay Time (seconds):")
# delay_label.pack(side="left")
# delay_var = tk.StringVar()
# delay_entry = ttk.Entry(app, textvariable=delay_var)
# delay_entry.pack(side="left")
# delay_var.set(str(DEFAULT_TIME_DELAY))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI Tool")
    parser.add_argument("-l","--language", help="Input file path", default="English")
    parser.add_argument("-d", "--delay_time", help="time for record a audio file", default=3)

    args = parser.parse_args()

    
    transcribed_text = tk.StringVar()
    transcribed_label = ttk.Label(app, textvariable=transcribed_text,font=("Arial", 24),background="#000001",foreground="white")
    transcribed_label.pack(fill="both", expand=True)

    should_stop_threads = True

    #def start():
    #global should_stop_threads
    record_thread = threading.Thread(target=record_audio,args=(int(args.delay_time), should_stop_threads))
    process_thread = threading.Thread(target=process_audio, args = (transcribed_text, args.language, should_stop_threads))
    record_thread.setDaemon(True)
    process_thread.setDaemon(True)
    record_thread.start()
    process_thread.start()

    



    # Start and Stop buttons
    #start_button = ttk.Button(app, text="Start", command=start)
    #stop_button = ttk.Button(app, text="Stop", command=stop)
    #start_button.pack(side="left")
    #stop_button.pack()

    
    app.mainloop()
