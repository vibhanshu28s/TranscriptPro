# TranscriptPro
This Python script utilises the whisper library to transcribe audio from a video file and then saves the transcribed text into a Microsoft Word (.docx) document.

# Key Features:
  - Audio Transcription: Employs OpenAI's Whisper model (specifically the "large" model) for highly accurate speech-to-text conversion.
  - SSL Certificate Handling: Includes a workaround for potential SSL certificate verification issues when loading the Whisper model.
  - `.docx` Export: Provides a function `write_text_to_docx` to neatly format and save the lengthy transcription into a `.docx` file, making it easily viewable and editable.
  - Easy Customization: The `video_file_path` variable can be easily adjusted to point to different video files for transcription.

# How to Use:

  1. Install Dependencies:
      pip install openai-whisper python-docx
    
  2.  Download ffmpeg: Ensure `ffmpeg` is installed and accessible in your system's PATH, as Whisper relies on it for audio processing.
  3.  Place Video File: Put your video file (e.g., `Daily Catch UP-20250505_150956-Meeting Recording.mp4`) in the same directory as the script, or update the `video_file_path` variable with the correct path.
  4.  Run the Script:
      python your_script_name.py
  
  This will generate a `transcription.docx` file containing the transcribed text from your video.
