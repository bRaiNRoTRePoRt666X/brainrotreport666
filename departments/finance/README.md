# Finance

Manages budgets, revenue and expenses. Full role, KPIs and tools: [`docs/departments/finance.md`](../../docs/departments/finance.md).

| Folder | Holds | Cadence |
|--------|-------|---------|
| `budgets/` | Episode, department and campaign budgets | Per episode |
| `invoices/` | Contractor and vendor invoice tracker | Monthly |
| `revenue/` | Platform, sponsorship, merch and affiliate income | Monthly |
| `expenses/` | Equipment, software, contractor and operating costs | Monthly |

## Approvals
- Budget over $500: department head and Finance.
- Budget over $2000: executive approval.
- New vendor: Finance and Legal.

## Handoffs
- **To departments:** budget allocation, spending limits and the expense reporting process.
- **From departments:** expense reports, invoice requests, and an explanation of any budget variance.

## Conventions
- Finance supports every stage. Sponsorship and affiliate income must match what was disclosed in the episode. Flag mismatches to `legal-compliance`.
- Budget lives in the episode's metadata as well. Keep the two in step by hand.
- Keep bank details, tax IDs and other sensitive data out of the repo. Store only references to invoices and records.
