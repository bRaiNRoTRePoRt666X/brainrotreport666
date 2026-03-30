import json, sys
profile = sys.argv[1] if len(sys.argv)>1 else "joker"
with open(f"departments/voice-pantheon/profiles/{profile}.json") as f: template = json.load(f)
script = sys.stdin.read()
print(f"FEED THIS TO YOUR TTS:\n{json.dumps({**template, 'script': script}, indent=2)}")
