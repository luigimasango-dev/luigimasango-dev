## Luigi Masango

I build and run AI agent systems that do real work, in Python, JavaScript and PowerShell on
Windows. I live in Katlehong, Gauteng.

I am self-taught. Before this I spent four and a half years as a machine operator at South Ocean
Electric Wire in Alrode, running fine wire drawing, stranding and extrusion machines. I have no
computer science degree. Everything below I built by directing coding agents and then checking
what they produced on disk, which is where the habits further down come from.

### Ubuntu Lab Consultants

I run Ubuntu Lab Consultants (Pty) Ltd, a consultancy for private businesses. The software
exists so one person can do the research, coordination and follow-up of a small office. The
consulting work so far: sourcing tenders and matching them to businesses that can deliver,
lining up partners where a bid needs a skill or grading we lack, screening businesses against
South African funding programmes, and an export pack for growers using China's zero-duty
window, which runs from 1 May 2026 to 30 April 2028.

Field apps for site crews sit beside it. Proof Pack turns a photo, a quantity and a client
signature into one A4 page. A certificate tracker drafts the reminder before a ticket lapses.
Offline calculators handle paint and steel quantities, and FieldOps turns the daily pre-start
check into cost per machine-hour. They all work with no signal.

### What I am building now (November 2026)

An agent estate, with gates that can fail. It has 233 agent definitions and 40 declared MCP
servers, 26 of them connected. The numbers matter less than the instruments. A pin gate checks
that every model pin still resolves against the live registry. A freshness gate checks that the
rules files still describe the machines they govern. A TDD gate refuses production code that has
no test. When one of them goes red on healthy work, I fix the gate rather than the claim.

A betting analysis lane that measures itself. It has a goals model, calibration over 1,095
de-vigged observations, and one admission rule: a selection only goes in at 70% or better model
probability. A pre-placement gate enforces ten rules and has refused my own book on merit rather
than let it through. 1,060 automated tests.

A trading system whose safety defaults off. MT5 integration sits behind a live-trading gate, a
daily-loss cap and a mandatory stop on every position. The kill switch survives a restart and
there is no way to reset it from a chat: once it trips, a human edits the state file by hand. The
bot fills in a missing stop and target on any open trade, including mine, but never moves one a
person set, and it refuses a trade whose single stop would cost more than the whole account. A
read-only audit traced every order path in it back to one guarded choke point. 1,069 automated
tests. A pre-execution hook judges every shell command and file write before it happens, and it
fails open rather than locking the machine.

Infrastructure I run myself instead of renting. Firecrawl, the scraping and search engine, runs
in Docker on my own machine and only answers on localhost, so agents scrape and search without
API credits. Ten upstream projects the estate depends on (OpenCode, the MCP Python SDK, the
desktop driver and others) are cloned and studied at the source, and the findings I acted on
were checked against the file and line they cite first. A watchdog checks long-running agent
goals every 15 minutes with an independent judge, because a model grading its own progress has a
blind spot.

Smaller builds include a Roblox game with its own test suite. The MCP servers are pinned below.

### How I work

I verify on disk rather than trusting an agent's summary. A bridge tool once reported a job
complete and returned a plausible description of a deliverable that did not exist.

I write the rubric before the work, because a rubric written afterwards is shaped by the output
it is meant to judge.

Every countable claim I publish traces to something that can re-measure it. If a number cannot
be re-measured on demand, it does not go in the document.

Every failure that costs real time or money gets a numbered lesson. There are 35 of them so far.

### Numbers, measured 2026-11-04

| Measure | Value |
|---|---|
| Agent definitions in the estate | 233 |
| MCP servers declared / connected | 40 / 26 |
| Automated tests, company estate | 667 |
| Automated tests, betting lane | 1,060 |
| Automated tests, trading system | 1,069 passing, 0 failing |
| Public repositories (2026-11-17) | 10 |

### Pinned projects

| Project | What it does |
|---|---|
| [local-ai-image-detector](https://github.com/luigimasango-dev/local-ai-image-detector) | Chrome MV3 extension that flags AI-generated images; inference runs entirely in-browser via ONNX/WebGPU |
| [youtube-transcript-mcp](https://github.com/luigimasango-dev/youtube-transcript-mcp) | MCP server for pulling, searching and chapter-summarising YouTube transcripts, no API key |
| [webcam-mcp](https://github.com/luigimasango-dev/webcam-mcp) | MCP server: webcam stills, mic transcription (faster-whisper), TTS and wake word, all local |
| [claude-office](https://github.com/luigimasango-dev/claude-office) | Telegram Mini App and desktop dashboard showing a live pixel-art office of coding agents, fed from local transcripts |
| [browser-tools-mcp](https://github.com/luigimasango-dev/browser-tools-mcp) | Headed-Chromium browser control for OpenCode and Claude Code |
| [chrome-bridge](https://github.com/luigimasango-dev/chrome-bridge) | WebSocket bridge and MV3 extension that lets an agent drive your already logged-in Chrome |

### Currently

Running Ubuntu Lab Consultants and building the tools behind it. Open to contract work on
operations coordination, Python, agent orchestration, MCP servers and test-first delivery.

### Contact

luigimasango@gmail.com · [LinkedIn](https://www.linkedin.com/in/luigi-masango-417196111/) ·
[Ubuntu Lab Consultants](https://luigimasango-dev.github.io/ulc-site/)

Ubuntu Lab Consultants (Pty) Ltd: Exempted Micro Enterprise, 100% black-owned. Katlehong, Gauteng.
