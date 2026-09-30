# AI Wedding Photo Skill

一套面向 Codex 和其他支持 Agent Skill 规范的 AI 婚纱照工作流。

它提供 15 种婚纱照风格选择，并引导用户选择生图模型、输出适配该模型的提示词、分镜清单和负面提示词。现有 9 种配有九宫格总览图；新增 6 种目前以文字风格卡呈现，其九宫格预览和补充菜单待内置图像生成工具可用后补齐。在 Codex 中，如果当前环境提供生图工具，还可以继续使用上传的情侣或宠物参考照直接生成图片。

## 15 种风格

![现有九种 AI 婚纱照风格总览](ai-wedding-photo/assets/style-previews/style-menu.png)

1. 日系胶片自然风
2. 韩系极简清透风
3. 海边度假纪实风
4. 法式复古花园风
5. 赛里木湖莫奈风
6. 从校服到婚姻
7. 公路旅行主题
8. 有宠物家庭
9. 暖金电影花园风
10. 新中式仪式感婚纱照
11. 都市夜景电影感
12. 雪山冬日纯白
13. 沙漠日落旅拍
14. 庄园葡萄园复古
15. 现代建筑美术馆

## 安装

将 `ai-wedding-photo` 文件夹复制到 Codex Skills 目录：

```bash
cp -R ai-wedding-photo ~/.codex/skills/
```

然后在对话中使用：

```text
使用 $ai-wedding-photo 帮我做一套 AI 婚纱照
```

## 工作流程

1. 展示 15 种风格选项；先展示现有九种风格总览图，新增六种暂以文字简介提供选择，待预览素材生成后再加入菜单。
2. 让用户选择风格，或根据场景、氛围和故事偏好推荐。
3. 询问使用 OpenAI/ChatGPT Images、Midjourney、Nano Banana、即梦、豆包或其他模型。
4. 收集情侣及宠物参考照、画幅和必要偏好。
5. 输出导演式分镜表，为每张照片分别设计景别、互动、动作、表情和构图。
6. 为 6-9 个分镜分别生成独立提示词，逐张生图，避免整套姿势雷同。
7. 在具备生图工具的 Codex 环境中继续生成与迭代。

## 项目结构

```text
ai-wedding-photo/
├── SKILL.md
├── agents/openai.yaml
├── assets/style-previews/
├── references/styles.md
├── references/shot-direction.md
├── references/model-adapters.md
└── scripts/make_contact_sheet.py
```

## 许可

代码和文字采用 MIT License。示例图片的肖像权、著作权与训练/生成平台条款需由发布者单独确认；仓库开源许可不自动授予第三方使用示例人物肖像的权利。
