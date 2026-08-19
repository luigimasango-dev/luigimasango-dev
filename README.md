## Luigi Masango

I build small production tools with AI coding agents. Python, JavaScript and PowerShell, on Windows.

Self-taught, no computer science degree. Before this I spent five years as a machine operator in cable manufacturing, running fine wire drawing, stranding and extrusion machines. Katlehong, Gauteng, South Africa.

### What I have built

**[youtube-transcript-mcp](https://github.com/luigimasango-dev/youtube-transcript-mcp)** — Model Context Protocol server for pulling and searching YouTube transcripts. Built to close a gap in my own stack, now in daily use.

**[webcam-mcp](https://github.com/luigimasango-dev/webcam-mcp)** — webcam capture and offline speech transcription. Runs entirely on the machine, no service calls.

**[local-ai-image-detector](https://github.com/luigimasango-dev/local-ai-image-detector)** — Chrome MV3 extension that flags AI-generated images. Detection runs locally, with no server round-trip.

**[claude-office](https://github.com/luigimasango-dev/claude-office)** — Telegram Mini App. A live pixel office showing what my coding agents are working on, reading local session transcripts. The bot menu button is provisioned automatically on start.

**[browser-tools-mcp](https://github.com/luigimasango-dev/browser-tools-mcp)** — MCP server exposing browser inspection and control to an agent.

**[chrome-bridge](https://github.com/luigimasango-dev/chrome-bridge)** — a WebSocket bridge and Chrome extension pairing a local agent to a running browser.

Not yet public: a suite of ten MCP servers covering company registry lookup, B-BBEE scorecard estimation, POPIA data-flow auditing, payroll anomaly detection and tender monitoring against a government API; a passive reconnaissance server with certificate-transparency history and an RDAP lookup that falls back to whois for `.za`, because RDAP has no coverage there; and two trading integrations built around hard safety gates.

### How I work

I run Claude Code and Hermes Agent in production against my own projects, and I have debugged both.

Evaluating what they produce is a normal part of the day, including the failure modes that actually cost you: confident wrong answers, fabricated tool results, silent truncation. I keep a written record of every time an agent was confidently wrong, because each one cost me hours. A bridge tool once reported a job complete and returned a plausible summary of a deliverable that did not exist on disk.

I write the evaluation rubric before the work rather than after, because a rubric written afterwards is shaped by the output it is meant to judge.

On safety gates: my trading integrations sit behind a flag that defaults off, a hard capital cap, and a kill switch with no software reset. A pre-execution hook blocks edits to the gate itself, so the safety cannot be switched off by the same process that would benefit from switching it off.

### Contact

luigimasango@gmail.com · [LinkedIn](https://www.linkedin.com/in/luigi-masango-417196111/)

Available for remote contract or full-time work.
