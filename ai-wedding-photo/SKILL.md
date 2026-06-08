---
name: ai-wedding-photo
description: Create personalized AI wedding-photo prompts and, when image-generation tools are available, generate wedding photos from uploaded reference portraits. Use when users ask for AI wedding photos, 婚纱照, 情侣写真, pre-wedding portraits, wedding style selection, model-specific image prompts, or one of the nine curated styles bundled with this skill.
---

# AI Wedding Photo

Guide the user from style selection to model-ready prompts and optional image generation.

## Workflow

1. Check whether the user has already supplied clear portrait references for both people and any pet that must appear.
2. Present all nine styles from [references/styles.md](references/styles.md). Show `assets/style-previews/style-menu.png` first, then show individual previews when the user wants a closer comparison. Use Markdown image syntax. If the interface cannot display local images, provide the style names and concise descriptions.
3. Ask the user to choose one style or request a recommendation. If recommending, ask only for the desired setting, mood, season, and whether pets or a story timeline should appear.
4. After the style is selected, ask which image model or platform will be used. Offer: OpenAI/ChatGPT Images, Midjourney, Nano Banana, 即梦, 豆包, or another named model.
5. Read the selected style entry in [references/styles.md](references/styles.md), the directing rules in [references/shot-direction.md](references/shot-direction.md), and the model rules in [references/model-adapters.md](references/model-adapters.md).
6. Collect only missing essentials:
   - Reference portraits for identity preservation
   - Number and identity of people or pets
   - Preferred aspect ratio or output count
   - Any clothing, location, pose, or cultural requirements
7. Produce:
   - A concise creative brief
   - One master prompt
   - A directing table for 6-9 distinct frames
   - One complete model-adapted prompt per frame
   - A negative prompt only when the chosen model supports it
8. Run the diversity check in [references/shot-direction.md](references/shot-direction.md). Rewrite duplicated frames before generating.
9. If running in Codex and an image-generation tool is available, ask for missing reference images, then generate directly. Generate every frame as a separate image request using its own prompt; never ask one request to create the whole set or a contact sheet. Generate one representative frame first unless the user explicitly requests a full set. Preserve identity and iterate from user feedback.
10. If direct generation is unavailable, give the frame prompts in separate copy-ready code blocks and concise usage notes for the selected model.

## Interaction Rules

- Show the style menu before asking about the model unless the user already chose a style.
- Do not ask every possible preference at once. Ask the minimum needed for the next step.
- Treat uploaded faces as identity references, not as style references.
- Preserve ethnicity, age range, facial structure, glasses, hairstyle, and distinguishing features unless the user requests changes.
- Keep skin texture natural. Avoid automatic face slimming, whitening, age regression, or body reshaping.
- For multi-image sets, treat the reference collage as a directing target: reproduce its variety of interaction, expression, camera distance, composition, and environmental storytelling without copying a single image literally.
- Do not accept superficial variation such as changing hand position while keeping the same standing pose, camera distance, facial expression, and background.
- Use no more than two formal side-by-side standing portraits in one set.
- Keep subjects looking directly at the camera in no more than two frames. Favor mutual eye contact, laughter, movement, quiet glances, and absorbed interaction.
- Give each frame one clear emotional beat and one physical action. Avoid vague directions such as "pose naturally" or "look intimate."
- Do not promise exact identity reproduction. State briefly that results depend on the selected model and reference quality.
- Never identify a real person from an image.

## Asset Map

Preview paths and style IDs are listed in [references/styles.md](references/styles.md).

Use `scripts/make_contact_sheet.py` when a style is supplied as nine separate images and needs a square 3x3 preview:

```bash
python3 scripts/make_contact_sheet.py INPUT_DIR OUTPUT.png
```
