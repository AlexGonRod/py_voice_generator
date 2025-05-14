
import whisper

class Transcriber:
	def __init__(self, audio_file):
		self.audio_file = audio_file

	def transcribe(self):
		try:
			model = whisper.load_model("base")
			result = model.transcribe(self.audio_file, language="es",fp16=False)
			transcription = result["text"]
			
			print(f"Texto original: {transcription}")
			return transcription
		except Exception as e:
			raise Exception(f"A transcription error occurred: {str(e)}")
		

