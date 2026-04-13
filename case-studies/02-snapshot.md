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
- **Product sense**: Identified a gap no one was filling — the check-in itself as the core product
- **Customer empathy**: Built to solve my own problem, alpha tested with real users, iterated on feedback
- **GTM strategy**: Tiered pricing (Free/Pro/Elite), competitive positioning against 6 competitors, community-driven growth thesis
- **Messaging & positioning**: Elevator pitches at 10s/30s/2min, objection-handling scripts, "manual entry is a feature" reframe
- **Competitive analysis**: Documented positioning against Mint, YNAB, Monarch, Copilot, Habitica, Credit Karma

## Key Visuals
> Add screenshots to `../visuals/snapshot/`

- Dashboard waterfall chart (cash flow visualization)
- Player profile character sheet (level, XP, streaks, achievements)
- Snapshot comparison view (side-by-side delta analysis)
- Debt payoff engine (avalanche vs. snowball)
- Mobile snapshot wizard (7-step swipe-through)
- Promo/marketing site with pricing tiers
- Live at: [app.takesnapshot.com](https://app.takesnapshot.com)

## Portfolio Angle
Snapshot is a product I built from zero to alpha because I saw a gap nobody was filling. I identified the behavioral insight (manual observation changes financial behavior), validated it through my own usage and alpha testers, designed a gamification system that creates long-term engagement loops, integrated AI to deliver personalized coaching at near-zero marginal cost, and built a go-to-market strategy with tiered pricing, competitive positioning, and a community-driven growth thesis. I shipped a production web app, a mobile companion, a marketing site, and a pitch deck — all while working full-time.
