import json
import plotly.graph_objects as go
import re

filename_without_extension = 'test_data_melody_line'
filename = filename_without_extension + '.json'

with open(filename, 'r') as json_open:
    json_load = json.load(json_open)

bpm = 76
minute_msec = 60
quarter_duration_msec = minute_msec/bpm
eighth_duration_msec = quarter_duration_msec/2
sixteenth_duration_msec = eighth_duration_msec/2
thirty_second_duration_msec = sixteenth_duration_msec/2
sixty_fourth_duration_msec = thirty_second_duration_msec/2

cnt = 0
min_dur = 999999
filtered_note = []
for elm in json_load:
    note_duration = elm['end'] - elm['start']
    # filtering by duration of note
    if note_duration > sixty_fourth_duration_msec:
        # filtering by timing of note
        # -> no mean
        # mod_sixteenth = elm['start'] % sixteenth_duration_msec
        # mod_sixteenth = min(mod_sixteenth, sixteenth_duration_msec - mod_sixteenth)
        # if mod_sixteenth < sixty_fourth_duration_msec:
        filtered_note.append(elm)

# output
output_filename = filename_without_extension + '_filtered_mod.json'
with open(output_filename, "w") as f:
    json.dump(filtered_note, f, indent=4)

# visualize melody data
NORMALIZED_NOTE_DICTIONARY \
    = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
NOTE_NUM = 12


def convert_full_note_name_to_note_num(full_note_str):
    octave = int(re.sub(r"\D", "", full_note_str))
    note_name = re.sub(r"\d", "", full_note_str)
    note_num = NOTE_NUM*octave + NORMALIZED_NOTE_DICTIONARY[note_name]
    return note_num


fig = go.Figure()
fig.add_trace(go.Scatter())
for elm in json_load:
# for elm in filtered_note:
    note_num = convert_full_note_name_to_note_num(elm['note_name'])
    fig.add_shape(type='rect',
                  xref='x', yref='y',
                  x0=elm['start'], y0=note_num+0.5,
                  x1=elm['end'], y1=note_num-0.5,
                  line=dict(
                      color="RoyalBlue",
                      width=3
                  ),
                  fillcolor="LightSkyBlue",
                  )
fig.update_layout(width=10000)
fig.show()
