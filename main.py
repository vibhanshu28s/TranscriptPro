import whisper
import ssl
import urllib.request
from docx import Document

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

model = whisper.load_model("large")
video_file_path = "Daily Catch UP-20250605_150956-Meeting Recording.mp4" # Adjust
result = model.transcribe(video_file_path)
transcription_text = result["text"]
print(transcription_text)

def write_text_to_docx(text, output_docx_file):
    """
    Writes text to a Word .docx file.

    Args:
        text: The text to write.
        output_docx_file: The path to the .docx file to create.
    """
    try:
        document = Document()
        document.add_paragraph(text)
        document.save(output_docx_file)
        print(f"Transcription successfully written to: {output_docx_file}")
    except Exception as e:
        print(f"An error occurred while writing to .docx: {e}")

# Specify the output .docx file path
output_file = "transcription.docx"

# Call the function to write the transcription to a .docx file
write_text_to_docx(transcription_text, output_file)