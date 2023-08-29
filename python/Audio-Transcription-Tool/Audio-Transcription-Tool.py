"""
Script Name: Audio Transcription Tool
Copyright (c) 2022, Tech Lovers. All rights reserved.
Project Name: python_transcription
Feature: Drag and drop transcription
Creation Date: 2022-12-26
Programming language used: Python
Author: DEmodoriGatsuO
GitHub: https://github.com/DEmodoriGatsuO
Twitter: https://twitter.com/DemodoriGatsuo
Note: This script transcribes audio from a WAV file using Google's speech recognition.

Requirements:
   * pip install SpeechRecognition

Usage:
   * python script_name.py input_audio.wav

"""

import sys
import speech_recognition as sr

def transcribe_audio(input_audio_path):
    """
    Transcribe audio from a WAV file using Google's speech recognition and save the result to a text file.
    
    Args:
        input_audio_path (str): Path to the input WAV audio file.
    """
    recognizer = sr.Recognizer()
    
    # Load audio file
    with sr.AudioFile(input_audio_path) as source:
        audio = recognizer.record(source)
    
    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio, language='ja-JP')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return
    
    # Write transcription to a text file
    with open('transcription.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    
    print("Transcription saved to transcription.txt")

if __name__ == "__main__":
    # Supported file extension
    supported_ext = '.wav'

    # Check for input argument
    if len(sys.argv) != 2:
        print("Error! This program requires one argument: input_audio.wav")
        sys.exit(1)

    input_file = sys.argv[1]

    # Check if the input file has the supported extension
    if not input_file.endswith(supported_ext):
        print("Error! This program only supports .wav files.")
        sys.exit(1)

    transcribe_audio(input_file)
