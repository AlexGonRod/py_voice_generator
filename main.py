import gradio as gr
from dotenv import dotenv_values


config = dotenv_values(".env")
ELEVEN_API_KEY = config["ELEVENLABS_APY_KEY"]

def translate(audio_file):
	from controllers.voices import Voices
	from controllers.transcriber import Transcriber
	
	transcription = Transcriber(audio_file).transcribe()
	print(f"Trans: {transcription}")
	voices = Voices(ELEVEN_API_KEY)
	audio = voices.generate_voice(transcription)

	save_file_path = 'audios/audio.mp3'

	with open(save_file_path, "wb") as f:
		for chunk in audio:
			if chunk:
				f.write(chunk)

	return save_file_path
	
web = gr.Interface(
    fn=translate,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Español"
    ),
    outputs=[
        gr.Audio(),
    ],
    title="Traductor de voz",
    description="Traductor de voz con IA a varios idiomas"
)

web.launch()