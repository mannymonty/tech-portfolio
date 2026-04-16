# Snapshot
*Gamified Personal Finance App with AI Coaching*

## Live product
[takesnapshot.com](https://takesnapshot.com) — production web app, fully functional

## The Problem
Every personal finance app assumes the hard part is getting data (bank sync, transaction imports). The real problem is getting people to care about the data they already have. People avoid their finances, lose motivation, and never build the habit of checking in.

## What I Built
A full-stack personal finance companion — web app (Next.js, 27 pages) + mobile app (React Native/Expo, 15+ screens) — that turns financial check-ins into a ritual. The core insight: manual observation changes spending behavior. Gamification makes the habit stick.

- **The Snapshot Ritual**: 8-step wizard captures your full financial picture in 60 seconds, prefilled from last time. Delta analysis shows exactly what changed.
- **Snappy AI Coach**: Claude-powered companion delivering personalized briefings — adherence scores, pattern detection, actionable next steps. ~$0.01/call with DB caching.
- **Deep Gamification**: 27 achievements across 4 tiers, XP-based leveling, streak tiers, flash challenges. A full progression system.
- **Debt Payoff Engine**: Avalanche/snowball simulation, what-if scenarios, per-debt amortization, paycheck planner.
- **Two-Client Architecture**: Web (command center) + mobile (quick-draw companion), shared backend, one account.

## Tech Stack
Next.js 14, React 18, React Native/Expo, TypeScript, Tailwind CSS, PostgreSQL (Supabase), Prisma ORM (38 models), Anthropic Claude, Clerk Auth, Recharts, Framer Motion, Vercel, EAS Build, Vitest + fast-check

## PMM Skills Demonstrated
- **Product sense**: Identified a gap no one was filling — the check-in itself as the core product, not the data sync
- **Customer empathy**: Built to solve my own problem first, then designed for the user who avoids their finances — not the one who's already engaged
- **GTM strategy**: Tiered pricing (Free/Pro/Elite), competitive positioning against 6 competitors, community-driven growth thesis
- **Messaging & positioning**: Elevator pitches at 10s/30s/2min, objection-handling scripts, "manual entry is a feature" reframe
- **Competitive analysis**: Documented positioning against Mint, YNAB, Monarch, Copilot, Habitica, Credit Karma
- **Technical execution**: 38-model Prisma schema, Claude AI integration at $0.01/call with DB caching, dual-client architecture (web + mobile) on a shared backend
- **Content production**: Built a Remotion-powered explainer video using the actual Snapshot codebase — programmatic video rendered from React components, not a screen recording

## Explainer Video (`../visuals/snapshot/snapshot-sales.mp4`)
A product explainer video produced with [Remotion](https://www.remotion.dev/) — a React framework for programmatic video. The video was built directly from the Snapshot codebase, meaning every animation, transition, and data visualization is driven by code rather than assembled in a traditional video editor. This is the same approach used for data-driven marketing content at scale.

This demonstrates the full PMM content loop: understand the product → define the narrative → produce the asset → ship it.

## Key Visuals (`../visuals/snapshot/`)
- `snapshot-sales.mp4` — Remotion explainer video (see above)
- Live app: [app.takesnapshot.com](https://app.takesnapshot.com)

## Portfolio Angle
Snapshot is a product I built from zero to production because I saw a gap nobody was filling. I identified the behavioral insight (manual observation changes financial behavior), designed a gamification system that creates long-term engagement loops, integrated AI coaching at near-zero marginal cost (~$0.01/call), and built a full go-to-market strategy with tiered pricing, competitive positioning against 6 competitors, and a community-driven growth thesis. Then I produced a Remotion-powered explainer video — programmatic video built from React components using the actual codebase — to show I can close the loop from product to marketing asset. The result: a live production web app (27 pages), a mobile companion (15+ screens), a marketing site, a pitch deck, and a product video — all shipped while working full-time.
