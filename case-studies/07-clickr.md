# Clickr
*Real-Time UX Research Tagging Tool*

## Live product
[clickr-two.vercel.app](https://clickr-two.vercel.app) — live on Vercel, built in under a week

## The Problem
UX research sessions move fast. Moderators and observers need to flag moments — a pain point, a quote, a moment of confusion — in real time, without breaking the flow of the conversation. After the call, matching those moments to a transcript is manual, slow, and lossy. Existing tools either require post-session tagging (you forget the context) or are too heavy to run alongside a video call.

## What I Built
A lightweight, real-time collaborative tagging app built for live research sessions. Multiple team members join the same session and tag moments simultaneously — each click is timestamped and synced instantly via Firebase. After the session, tags can be matched against an imported transcript (Google Meet, .srt, .sbv) with auto-alignment logic.

### Core Features

- **Live collaborative sessions**: Host creates a session with a 6-char join code; observers join from any browser. All tags sync in real time via Firestore subscriptions.
- **Customizable tag buttons**: 6 default tags (Pain point, Delight, Confusion, Quote, Insight, Feature req) with color coding. Add new buttons mid-session without interrupting the flow.
- **Timestamped tag log**: Every click is recorded with elapsed time, tagger name, and label. Filterable by participant during the session.
- **Pause/resume timer**: Host can pause the session clock (e.g., during a break) without losing tag history. Keyboard shortcuts for speed (1–9 to tag, Z to undo, Space to pause).
- **Emoji reactions**: Lightweight non-verbal communication between observers during the call (👀 🔥 ⚠️ 💡 ❓) — floating animations visible to all participants.
- **Transcript matching**: Upload a transcript post-session; the app auto-aligns tag timestamps to transcript lines using a closest-match algorithm with adjustable offset. Highlights tagged moments inline.
- **Export**: CSV (with transcript context column) and styled HTML report — session metadata, tag breakdown by type and by person, full timestamped log with matched transcript lines.
- **Session history**: All sessions persist in Firestore, organized by project. Reload any past session for review or re-export.
- **Presence system**: Heartbeat-based presence tracking shows who's active in a session.

## Tech Stack
React 18, Vite, Firebase (Firestore real-time), Tailwind CSS, JavaScript (ES2023)

## What This Shows
- **Product sense**: Identified the exact moment in the research workflow where value is lost (real-time tagging with no good tool) and built the minimum viable solution that solves it without adding friction
- **Customer empathy**: Designed for the moderator's context — running a live call, can't context-switch. Keyboard shortcuts, one-click tagging, pause support, and a clean mobile-friendly UI reflect deep understanding of the use case
- **Systems thinking**: Real-time sync architecture (Firestore subscriptions + presence heartbeat), auto-alignment algorithm for transcript matching, multi-role session model (host vs. observer)
- **Data storytelling**: The export layer turns raw click data into a structured research artifact — HTML report with tag breakdown, per-person attribution, and transcript context inline
- **Iterative design**: Feature set reflects real research team needs: multi-participant support, mid-session button creation, undo, pause, emoji reactions — each one solving a specific friction point

## Portfolio Angle
Clickr is a tool I built in under a week because the research workflow had a gap nobody had cleanly solved: real-time, multi-person tagging during a live call, with post-session transcript alignment. I designed the full session model (host/observer roles, 6-char join codes, heartbeat-based presence), built the real-time sync layer on Firebase Firestore, and shipped a transcript matching algorithm that auto-aligns click timestamps to transcript lines with adjustable offset. The export layer produces a shareable research artifact — HTML report with tag breakdown, per-person attribution, and transcript context inline. It's live, it works, and it's ready to use. This is what I do: see a workflow gap, design the solution, ship it.

---

## What's Included in This Repo

### Architecture Diagram (`../visuals/clickr/`)
**`architecture-diagram.svg`** — Full system diagram showing the React screen flow, Firebase Firestore data model (sessions + presence collections), real-time subscription layer, and the 6-step session lifecycle from create → join → live → end → review → export.

### Code (`../samples/clickr/` or link to source)
- Full source available at [github.com/gizmonty/clickr](https://github.com/gizmonty/clickr)
- Key files: `src/App.jsx` (session state machine), `src/lib/sessions.js` (Firestore layer), `src/components/SessionScreen.jsx` (live tagging UI), `src/components/ReviewScreen.jsx` (transcript matching + export)

### Visuals (`../visuals/clickr/`)
- Session screen with tag buttons, live timer, and tag log
- Review screen with transcript matched inline (highlighted rows)
- HTML export report
- Join flow (welcome → enter name → join code)
- Multi-participant tag log filtered by person
