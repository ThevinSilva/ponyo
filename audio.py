from faster_whisper import WhisperModel

model_size = "small"

model = WhisperModel(model_size, device="cpu", compute_type="int8")
segments, _ = model.transcribe("fish.mp3", word_timestamps=True)

for segment in segments:
    for word in segment.words:
        print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))