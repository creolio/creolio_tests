from srtfiles import srtreader
from helpers import environment
from helpers import file
from textprocessing import frequencies
import split_fr as split_fr

script_directory = environment.get_path_from_filepath(__file__)

files_with_subtitles = environment.get_files_that_end_with(script_directory, ".srt")

def process_srt(filename):
    text = srtreader.get_content_as_plain_text(filename)

    if filename.endswith("_fr.srt"):
        words = split_fr.split_into_words(text)
        word_frequencies = frequencies.calculate_frequencies(words)
        file.save_as_json(filename + ".json", word_frequencies)

    file.write_text_to_file(filename + ".txt", text)

def process_srt_files_in_folder():
    for filename in files_with_subtitles:
        print(f"  - processing {filename} ...")
        process_srt(filename)

if __name__ == "__main__":
   process_srt_files_in_folder()


        
