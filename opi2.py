import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import io

import pretty_midi
from scipy.io import wavfile


st.title(":musical_note: Convert a MIDI file to WAV")

uploaded_file = st.file_uploader("Upload MIDI file (you can fetch one on https://bitmidi.com/)", type=["mid"])

if uploaded_file is None:
    st.info("Please upload a MIDI file")
    st.stop()

midi_data = pretty_midi.PrettyMIDI(uploaded_file)
audio_data = midi_data.fluidsynth()
audio_data = np.int16(audio_data / np.max(np.abs(
    audio_data)) * 32767 * 0.9)  # -- Normalize for 16 bit audio https://github.com/jkanner/streamlit-audio/blob/main/helper.py

virtualfile = io.BytesIO()
wavfile.write(virtualfile, 44100, audio_data)

st.audio(virtualfile)
st.markdown("Download the audio by right-clicking on the media player")
st.title('Invitation!')