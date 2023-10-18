import os

from pydub import AudioSegment
import assemblyai as aai
import re


def convert_to_mp3(input_file_path, output_file_path):
    audio = AudioSegment.from_file(input_file_path)
    audio.export(output_file_path, format="mp3")
    return output_file_path


def transcribe_audio(input_file_path, assembly_ai_api_key):
    aai.settings.api_key = assembly_ai_api_key
    config = aai.TranscriptionConfig(speaker_labels=True, language_code="pt")

    path, filename = os.path.split(input_file_path)
    output_file_path = os.path.join(path, "transcribed_" + filename)

    convert_to_mp3(input_file_path, output_file_path=output_file_path)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
        output_file_path,
        config=config
    )

    print(transcript.text)

    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")

    return transcript
