from stt import record_audio, transcribe_audio
from intents import understand_command
from actions import perform_action

def main():
    audio_file = record_audio()
    spoken_text = transcribe_audio(audio_file)
    print(f"📝 Recognized: {spoken_text}")
    
    command = understand_command(spoken_text)
    print(f"🔍 Intent: {command}")
    
    perform_action(command)

if __name__ == "__main__":
    main()