# Model Adapters

Start from the chosen style definition, the approved directing table, and a factual description of the uploaded references. Keep identity instructions near the beginning. Write one self-contained prompt per frame. Do not submit the entire set as one generation request, because this often collapses the set into repeated poses and compositions.

## OpenAI / ChatGPT Images

Write natural-language art direction. Explicitly state which uploaded image corresponds to each person or pet. Describe identity preservation, scene, wardrobe, pose, light, camera framing, and exclusions in complete sentences. Do not add Midjourney parameters.

Recommended structure:

```text
Using the uploaded reference portraits, create one wedding photograph of [subjects].
Preserve [identity details]. Apply [style direction].
This frame's unique story beat is [emotion]. The subjects are actively [concrete action].
Use [light, lens/framing, palette]. Keep [continuity rules].
This frame must differ from the rest of the series through [shot size, viewpoint, composition, expression].
Do not [identity and artifact exclusions].
```

## Midjourney

Write a separate prompt for every frame. Compress the visual description into weighted clauses. Put character consistency and references first, followed by the frame's concrete action, expression, shot size, composition, environment, and light. End with parameters supported by the user's version, typically `--ar`, `--stylize`, and `--chaos`. Do not invent image-reference URLs; tell the user to attach or paste them in the target interface.

Use low chaos for a coherent wedding series. Avoid unsupported negative-prompt syntax; use `--no` for a short list of concrete exclusions.

## Nano Banana

Use clear natural-language instructions and attach the reference portraits in the target interface. Identify each person or pet by reference-image order, then state what must remain unchanged: facial structure, glasses, hairstyle, skin tone, age range, and pet markings.

Describe one frame per prompt for better identity and composition control. Specify subjects, wardrobe, action, environment, light, framing, and continuity with the rest of the series. Avoid Midjourney parameters and long tag lists. Phrase exclusions as direct instructions such as "不要改变两人的面部特征" and "不要生成额外人物或手指畸形".

## 即梦

Use concise Chinese prose. State subject identity consistency, number of people, clothing, location, concrete action, emotional reaction, shot size, camera position, composition, and texture. Split a multi-image series into numbered standalone prompts rather than asking one generation to produce a collage. Repeat essential identity and continuity requirements in every prompt.

## 豆包

Use fluent Chinese natural-language instructions. State that the uploaded portraits are identity references, identify each person or pet, and explicitly preserve facial structure, glasses, hairstyle, age range, skin tone, and pet markings. Describe one frame at a time with clothing, concrete action, emotional reaction, setting, light, shot size, camera viewpoint, composition, and photographic texture. Repeat identity requirements in every standalone frame prompt. Keep instructions concise, avoid parameter syntax from other platforms, and express exclusions as direct Chinese requirements.

## Unknown Model

Return a universal natural-language prompt plus:

- Aspect ratio
- One frame only
- Identity-reference note
- Optional negative prompt
- A warning that exact parameter syntax depends on the interface
