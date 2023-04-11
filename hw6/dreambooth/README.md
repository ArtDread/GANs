# Subject-Driven Generation

DreamBooth is a method to personalize text2image models like stable diffusion given just a few images of a subject. I used 14 different images of me (guy Daniel Moore) with different angles (/src) and tried some prompts. Here's what I got.

## Results

### Prompt 1: Daniel Moore as a human fighter in the style of a baldurs gate character portrait

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_1/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_1/1.png> Guidance scale: 7|<img width="512" alt="2.png" src=./inference_1/2.png> Guidance scale: 7|<img width="512" alt="3.png" src=./inference_1/3.png> Guidance scale: 7|
|<img width="512" alt="4.png" src=./inference_1/4.png> Guidance scale: 7|<img width="512" alt="5 (g_s_4).png" src="./inference_1/5 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="6 (g_s_4).png" src="./inference_1/6 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="7 (g_s_4).png" src="./inference_1/7 (g_s_4).png"> Guidance scale: 4|

### Prompt 2: Highly detailed portrait of Daniel Moore, sunglasses, blue eyes, tartan scarf, white hair by atey ghailan, by greg rutkowski, by greg tocchini, by james gilleard, by joe fenton, by kaethe butcher, gradient yellow, black, brown and magenta color scheme, grunge aesthetic!!! graffiti tag wall background

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_2/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_2/1.png> Guidance scale: 7|<img width="512" alt="2 (g_s_4).png" src="./inference_2/2 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="3 (g_s_4).png" src="./inference_2/3 (g_s_4).png"> Guidance scale: 4|
|<img width="512" alt="4 (g_s_9).png" src="./inference_2/4 (g_s_9).png"> Guidance scale: 9|<img width="512" alt="5 (g_s_9).png" src="./inference_2/5 (g_s_9).png"> Guidance scale: 9|<img width="512" alt="6 (g_s_9).png" src="./inference_2/6 (g_s_9).png"> Guidance scale: 9|<img width="512" alt="7 (g_s_9).png" src="./inference_2/7 (g_s_9).png"> Guidance scale: 9|

This prompt was the most stable in the sense of generating good images of me.

### Prompt 3: Daniel Moore, on a vintage 90's anime style; by hajime sorayama, greg tocchini, virgil finlay, sci-fi, colors, neon lights. line art

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_3/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_3/1.png> Guidance scale: 7|<img width="512" alt="2.png" src="./inference_3/2.png"> Guidance scale: 7|<img width="512" alt="3.png" src="./inference_3/3.png"> Guidance scale: 7|
|<img width="512" alt="4 (g_s_4).png" src="./inference_3/4 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="5 (g_s_4).png" src="./inference_3/5 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="6 (g_s_4).png" src="./inference_3/6 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="7 (g_s_4).png" src="./inference_3/7 (g_s_4).png"> Guidance scale: 4|

### Prompt 4: Daniel Moore in stylish haute couture outfit in the style of 90's vintage anime, surrealism, akira style. detailed line art. fine details. inside a space ship

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_4/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_4/1.png> Guidance scale: 7|<img width="512" alt="2.png" src="./inference_4/2.png"> Guidance scale: 7|<img width="512" alt="3.png" src="./inference_4/3.png"> Guidance scale: 7|
|<img width="512" alt="4.png" src="./inference_4/4.png"> Guidance scale: 7|<img width="512" alt="5.png" src="./inference_4/5.png"> Guidance scale: 7|<img width="512" alt="6 (g_s_4).png" src="./inference_4/6 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="7 (g_s_9).png" src="./inference_4/7 (g_s_9).png"> Guidance scale: 9|

### Prompt 5: Perfect portrait of Daniel Moore, new york, medium format, fuji superia 400, iso 400, cinematic, photorealistic, surrealistic, details, 8k

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_5/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_5/1.png> Guidance scale: 7|<img width="512" alt="2.png" src="./inference_5/2.png"> Guidance scale: 7|<img width="512" alt="3.png" src="./inference_5/3.png"> Guidance scale: 7|
|<img width="512" alt="4.png" src="./inference_5/4.png"> Guidance scale: 7|<img width="512" alt="5.png" src="./inference_5/5.png"> Guidance scale: 7|<img width="512" alt="6.png" src="./inference_5/6.png"> Guidance scale: 7|<img width="512" alt="7.png" src="./inference_5/7.png"> Guidance scale: 7|

This prompt did a great work in the sense of photography quality and generation of great New York landscapes but my face is totally ruined. It's probably because of poor quality source images as there's huge "face variance". It seems that result would be much better if all images were provided from one photo session.

### Prompt 6: A portrait of Daniel Moore viking runing muscular, smoking a cigar, gorgeous, intricate, elegant, volumetric lighting, scenery, high detail digital art, smooth, tony sart, lucian freud, anato finnstark, randy vargas, diego gisbert llorens, johan grenier, ruan jia, steve mccurry, photorealistic lighting, sharp focus, illustration

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_6/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_6/1.png> Guidance scale: 7|<img width="512" alt="2.png" src="./inference_6/2.png"> Guidance scale: 7|<img width="512" alt="3.png" src="./inference_6/3.png"> Guidance scale: 7|
|<img width="512" alt="4.png" src="./inference_6/4.png"> Guidance scale: 7|<img width="512" alt="5.png" src="./inference_6/5.png"> Guidance scale: 7|<img width="512" alt="6.png" src="./inference_6/6.png"> Guidance scale: 7|<img width="512" alt="7.png" src="./inference_6/7.png"> Guidance scale: 7|

### Prompt 7: Daniel Moore is programming at a computer in a room full of gadgets, by makoto shinkai and ghibli studio, outlined silhouettes, dramatic lighting, highly detailed, incredible quality, trending on artstation

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_7/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_7/1.png> Guidance scale: 7|<img width="512" alt="2.png" src=./inference_7/2.png> Guidance scale: 7|<img width="512" alt="3.png" src=./inference_7/3.png> Guidance scale: 7|
|<img width="512" alt="4.png" src=./inference_7/4.png> Guidance scale: 7|<img width="512" alt="5 (g_s_4).png" src="./inference_7/5 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="6 (g_s_4).png" src="./inference_7/6 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="7 (g_s_9).png" src="./inference_7/7 (g_s_9).png"> Guidance scale: 9|

### Prompt 8: Daniel Moore wearing cyberpunk intricate streetwear, respirator, beautiful, detailed portrait, cell shaded, 4 k, vivid colours, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality

| | | | |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img width="512" alt="0.png" src=./inference_8/0.png> Guidance scale: 7|<img width="512" alt="1.png" src=./inference_8/1.png> Guidance scale: 7|<img width="512" alt="2.png" src="./inference_8/2.png"> Guidance scale: 7|<img width="512" alt="3 (g_s_4).png" src="./inference_8/3 (g_s_4).png"> Guidance scale: 4|
|<img width="512" alt="4 (g_s_4).png" src="./inference_8/4 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="5 (g_s_4).png" src="./inference_8/5 (g_s_4).png"> Guidance scale: 4|<img width="512" alt="6 (g_s_9).png" src="./inference_8/6 (g_s_9).png"> Guidance scale: 9|<img width="512" alt="7 (g_s_9).png" src="./inference_8/7 (g_s_9).png"> Guidance scale: 9|
