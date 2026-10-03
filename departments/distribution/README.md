# Distribution

Publishes and optimizes episodes across platforms. Full role, KPIs and tools: [`docs/departments/distribution.md`](../../docs/departments/distribution.md).

| Folder | Holds |
|--------|-------|
| `youtube/` | Upload records, titles, descriptions, end screens, community posts |
| `instagram/` | Reels, feed posts, stories, captions and hashtags |
| `tiktok/` | Upload records, captions, hashtag strategy |
| `scheduling/` | Release calendar and cross-platform timing |
| `seo/` | Keyword research, title and description copy, tag strategy |

## Handoffs
- **In:** from Post-Production, with a final export in `episodes/ready/`, QC passed and legal compliance verified.
- **Out, after publishing:** all platforms updated, links documented, analytics tracking enabled, Community notified, archive started.

Record the handoff with `./scripts/workflow/handoff.sh EP### distribution community` from the repo root.

## Conventions
- Titles, descriptions, SEO copy and thumbnail text are held to the Red Lines in [`docs/ethics/campaign-principles.md`](../../docs/ethics/campaign-principles.md). Disclose sponsors and affiliates, and keep titles accurate to the content.
- `legal-compliance` verifies disclosures before publish.
- After publishing, record platform IDs in the episode's metadata and move the episode folder to `episodes/published/`. Nothing does this automatically.
- Video and image files are gitignored. Keep links and copy here, not media.
