# CLAUDE.md - AI Assistant Guidelines

This document provides context and guidelines for AI assistants working with this codebase.

## Project Overview

**Repository:** Nerfed-ai/AI
**Description:** AI project repository (currently in initial setup phase)
**Status:** New project - establishing foundations

## Repository Structure

```
/home/user/AI/
├── .git/                 # Git version control
├── README.md             # Project readme
└── CLAUDE.md             # AI assistant guidelines (this file)
```

> **Note:** This is a newly initialized repository. Structure will evolve as the project develops.

## Development Workflow

### Git Conventions

- **Main branch:** Default branch for production-ready code
- **Feature branches:** Use descriptive names prefixed with feature type
  - `feature/` - New features
  - `fix/` - Bug fixes
  - `docs/` - Documentation updates
  - `refactor/` - Code refactoring
  - `claude/` - AI-assisted development branches

### Commit Message Guidelines

Use clear, descriptive commit messages following this format:

```
<type>: <short description>

[optional body with more details]
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

### Branch Strategy

1. Create feature branches from the main branch
2. Make incremental, focused commits
3. Push changes with `git push -u origin <branch-name>`
4. Create pull requests for review

## Code Standards

### General Principles

1. **Simplicity:** Keep solutions focused and avoid over-engineering
2. **Clarity:** Write self-documenting code with meaningful names
3. **Consistency:** Follow established patterns in the codebase
4. **Security:** Never commit secrets, credentials, or sensitive data

### File Organization

- Keep related files together in logical directories
- Use clear, descriptive file names
- Maintain a flat structure where possible, nest only when necessary

## For AI Assistants

### Before Making Changes

1. **Read first:** Always read and understand existing code before modifying
2. **Understand context:** Review related files to understand patterns
3. **Check dependencies:** Understand how changes might affect other parts

### When Implementing Features

1. Start with the simplest solution that works
2. Make incremental changes with clear commits
3. Don't add features, refactoring, or "improvements" beyond what's requested
4. Avoid speculative code for hypothetical future needs

### Code Quality

- Don't add unnecessary comments or documentation
- Trust internal code and existing patterns
- Only validate at system boundaries (user input, external APIs)
- Avoid backwards-compatibility shims when direct changes work

### Security Considerations

- Never commit `.env` files or credentials
- Sanitize user inputs at entry points
- Be mindful of common vulnerabilities (XSS, injection, etc.)

## Testing

> Testing infrastructure to be set up as the project develops.

When tests are available:
- Run tests before committing changes
- Add tests for new functionality
- Ensure existing tests pass after modifications

## Build & Run

> Build commands will be documented as the project develops.

## Useful Commands

```bash
# Check repository status
git status

# View recent commits
git log --oneline -10

# Create and switch to a new branch
git checkout -b <branch-name>

# Push with upstream tracking
git push -u origin <branch-name>
```

## Project-Specific Notes

*(This section will be updated as the project develops with specific patterns, dependencies, and architectural decisions.)*

---

*Last updated: January 2026*
