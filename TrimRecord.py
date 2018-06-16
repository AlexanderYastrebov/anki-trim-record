import anki.sound

trim_start="0.25"
trim_end="0.15"

anki.sound.processingChain = [
    ["sox", "-q", "rec.wav", "trimmed.wav", "trim", trim_start, "reverse", "trim", trim_end, "reverse"],
    ["mv", "trimmed.wav", "rec.wav"],
] + anki.sound.processingChain
