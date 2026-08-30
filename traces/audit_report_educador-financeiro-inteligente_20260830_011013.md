# GitAudit AI Report - alananjos06/educador-financeiro-inteligente

**Generated at:** 2026-08-30 01:10:13

---

**Claim-by‑Claim Evaluation**

| # | Resume Claim | GitHub Evidence | Classification | Justification |
|---|---------------|-----------------|----------------|---------------|
| 1 | *“Complete React + Vite interface for IBM Bob Dev Hackathon.”* | No commits referencing this hackathon or a Vite‑based React project. | ❌ Unsubstantiated | Commit history does not mention the project name, React, or Vite. |
| 2 | *“Assisted teammate with Django backend, PostgreSQL, and API endpoints.”* | No Django or PostgreSQL related commits. | ❌ Unsubstantiated | All commits involve Node.js, SQLite, Firebase, and front‑end JS; no Django code. |
| 3 | *“Worked with CI/CD pipelines via GitHub Actions for automated tests.”* | No commit messages or file changes indicating GitHub Actions workflows or test execution. | ❌ Unsubstantiated | Repository does not show any workflow YAML files or test scripts. |
| 4 | *“5‑person Agile team delivering 3 project phases.”* | No evidence of team size, Agile artifacts, or phase milestones. | ❌ Unsubstantiated | Commit messages provide no information on team structure or iteration boundaries. |
| 5 | *“Front‑end of Open Resource platform (React Vite), custom design system.”* | No commits referencing “Open Resource”, React Vite, or design‑system components. | ❌ Unsubstantiated | All commits pertain to FinFreela; no other project code. |
| 6 | *“Interactive components: Badge, SkillTag, Score Ring, Skeleton, Toast.”* | No commits or file names matching these components. | ❌ Unsubstantiated | No evidence of component files or integration with APIs. |
| 7 | *“FinFreela: full‑stack web application for freelancer financial management.”* | Multiple commits adding a Node.js backend, SQLite database, and a front‑end README. | ✅ Well supported | Commit “feat: adiciona back‑end do FinFreela com Node.js e SQLite” confirms a full‑stack effort. |
| 8 | *“Refactoring architecture from Firebase & SQLite to Node.js & PostgreSQL.”* | Commits show a migration to Firebase (Firestore, Auth, Hosting) and a Node.js backend with SQLite, but **no PostgreSQL** usage. | ⚠️ Partially supported | The migration and Node.js backend are verified; however, the PostgreSQL claim is not supported. |
| 9 | *“Implemented transaction CRUD, monthly filtering, trend chart, CSV export.”* | Commit “feat: adiciona gráfico de pizza e ordenação na tabela” indicates a chart and table sorting. No commits about CRUD, filtering, or CSV export. | ⚠️ Partially supported | Chart functionality is confirmed; other features lack evidence. |
|10 | *“User authentication & protected routes between React front‑end and backend.”* | Commit “add: middleware e auth” and other “auth” mentions imply authentication logic. | ⚠️ Partially supported | Authentication middleware exists, but protected route implementation is not directly shown. |
|11 | *“Sabor & Brasa – multi‑page restaurant site with MySQL via PHP.”* | No PHP or MySQL commits. | ❌ Unsubstantiated | Repository shows only JS/Node/SQLite code. |
|12 | *“Dev Girls – multi‑page agency site with responsive navigation, profiles, services, contact.”* | No commits relating to this project. | ❌ Unsubstantiated | No evidence of this site or its components. |

---

### Overall Score Calculation

- **Well‑supported claims**: 1 (FinFreela full‑stack)
- **Partially supported claims**: 4 (FinFreela architecture, chart, auth, CRUD‑like features)
- **Unsubstantiated claims**: 7

**Resume Match Score** = \((1 + 4) / 12 = 5/12 ≈ 41.7 %\)

**Resume Match Score: 42%**