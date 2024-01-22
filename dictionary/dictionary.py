import os
import json

dir_path = "videos"
file_ext = ".mp4"

video_files = [os.path.splitext(f)[0] for f in os.listdir(dir_path) if f.endswith(file_ext)]


with open("video_list.txt", "w") as file:
    for video_file in video_files:
        file.write(video_file + "\n")

print("Video list created!")

with open('WLASL_v0.3.json') as f:
    data = json.load(f)

new_data = {}

for instance in data:
    gloss = instance['gloss']
    video_ids = [inst['video_id'] for inst in instance['instances']]
    new_data[gloss] = video_ids

with open('new_data.json', 'w') as f:
    json.dump(new_data, f)

with open('video_list.txt', 'r') as f:
    video_list = [line.strip() for line in f]

with open('new_data2.json', 'r') as f:
    data = json.load(f)


new_data = {}


for gloss, video_ids in data.items():
    for video_id in video_ids:
        if video_id in video_list:
            new_data[gloss] = video_id
            break

with open('new_data_filtered.json', 'w') as f:
    json.dump(new_data, f)