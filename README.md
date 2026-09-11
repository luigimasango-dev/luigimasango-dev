## Luigi Masango

I build small production tools with AI coding agents. Python, JavaScript and PowerShell, on Windows.

Self-taught, no computer science degree. Before this I spent five years as a machine operator in cable manufacturing, running fine wire drawing, stranding and extrusion machines. Katlehong, Gauteng, South Africa.

### Pinned projects

| Project | What it does | Screenshot |
|---|---|---|
| [local-ai-image-detector](https://github.com/luigimasango-dev/local-ai-image-detector) | Chrome MV3 extension that flags AI-generated images, inference runs entirely in-browser via ONNX/WebGPU | ![local-ai-image-detector](https://github.com/luigimasango-dev/local-ai-image-detector/raw/main/docs/tests.png) |
| [youtube-transcript-mcp](https://github.com/luigimasango-dev/youtube-transcript-mcp) | MCP server for pulling, searching and chapter-summarizing YouTube transcripts, no API key | ![youtube-transcript-mcp](https://github.com/luigimasango-dev/youtube-transcript-mcp/raw/main/docs/demo.png) |
| [webcam-mcp](https://github.com/luigimasango-dev/webcam-mcp) | MCP server: webcam stills, mic transcription (faster-whisper), TTS and wake-word, all local | ![webcam-mcp](https://github.com/luigimasango-dev/webcam-mcp/raw/main/docs/demo.png) |
| [claude-office](https://github.com/luigimasango-dev/claude-office) | Telegram Mini App + desktop dashboard: live pixel-art office of coding agents from local transcripts | ![claude-office](https://github.com/luigimasango-dev/claude-office/raw/main/docs/demo.png) |
| [browser-tools-mcp](https://github.com/luigimasango-dev/browser-tools-mcp) | Headed-Chromium browser control for OpenCode/Claude Code, five tools, CI smoke green | ![browser-tools-mcp](https://github.com/luigimasango-dev/browser-tools-mcp/raw/main/docs/demo.png) |
| [chrome-bridge](https://github.com/luigimasango-dev/chrome-bridge) | WebSocket bridge + MV3 extension letting agents drive your logged-in Chrome (login-walled sites) | ![chrome-bridge](https://github.com/luigimasango-dev/chrome-bridge/raw/main/docs/demo.png) |

### How I work

I run Claude Code and Hermes Agent in production against my own projects, and I have debugged both.

Evaluating what they produce is a normal part of the day, including the failure modes that actually cost you: confident wrong answers, fabricated tool results, silent truncation. I keep a written record of every time an agent was confidently wrong, because each one cost me hours. A bridge tool once reported a job complete and returned a plausible summary of a deliverable that did not exist on disk.

I write the evaluation rubric before the work rather than after, because a rubric written afterwards is shaped by the output it is meant to judge.

On safety gates: my trading integrations sit behind a flag that defaults off, a hard capital cap, and a kill switch with no software reset. A pre-execution hook blocks edits to the gate itself, so the safety cannot be switched off by the same process that would benefit from switching it off.

### Currently

Building MCP servers and agent tooling. Available for remote contract work.

### Contact

luigimasango@gmail.com · [LinkedIn](https://www.linkedin.com/in/luigi-masango-417196111/) · [Ubuntu Lab Consultants](https://luigimasango-dev.github.io/ulc-site/)