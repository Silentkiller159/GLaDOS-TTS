import os
import re
import num2words
import soundfile as sf
import json

audio_dir = 'aegis'

def audio_duration(fn):
    f = sf.SoundFile(fn)
    return f.frames / f.samplerate

def main():

    filenames = [f for f in os.listdir(audio_dir) if os.path.isfile(os.path.join(audio_dir, f))]
    
    total_audio_time = 0
    outFile=open(os.path.join(audio_dir, "manifest.json"), 'w')
    for i in range(len(filenames)):
        item = {}
        text = "TBD"
        filename = filenames[i]
        item["audio_filepath"] = os.path.join(audio_dir, filename)
        #item["text_normalized"] = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), text)
        item["text"] = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), text).lower()
        item["duration"] = audio_duration(os.path.join(audio_dir, filename))
        total_audio_time = total_audio_time + item["duration"]
        outFile.write(json.dumps(item, ensure_ascii=True, sort_keys=True) + "\n")
 
    outFile.close()
    print("\n" + str(total_audio_time/60.0) + " min\n")

main()