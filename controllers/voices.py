from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

class Voices:
	def __init__(self, API_KEY):
		self.API_KEY = API_KEY

	def generate_voice(self, transcription):
		try:
			client = ElevenLabs(api_key=self.API_KEY)
			# en_translation = Translator(from_lang="es", to_lang="es").translat, audio)
			response = client.text_to_speech.convert(
				voice_id="yiWEefwu5z3DQCM79clN",  # Laura
				optimize_streaming_latency="0",
				output_format="mp3_22050_32",
				text=transcription,
				model_id="eleven_multilingual_v2",
				voice_settings=VoiceSettings(
					stability=0.3,
					similarity_boost=0.0,
					style=0.5,
					use_speaker_boost=False,
				),
			)
			return response
			# print(f"Texto trans: {en_translation}")
		except Exception as e:
			raise Exception(f"An error during translation: {str(e)}")