# Claude Squad

> Manage multiple AI agents like Claude Code, Aider, Codex, and Amp simultaneously

[![Go Version](https://img.shields.io/badge/go-1.21+-blue.svg)](https://golang.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Release](https://img.shields.io/github/v/release/smtg-ai/claude-squad)](https://github.com/smtg-ai/claude-squad/releases)

## What is Claude Squad?

Claude Squad is a terminal user interface (TUI) that allows you to run multiple AI coding agents in parallel, each working in isolated environments using tmux sessions and git worktrees.

**Key Features:**
- 🔄 **Parallel execution** - Run multiple AI agents simultaneously
- 🌿 **Git isolation** - Each agent works in its own git worktree
- 📊 **Real-time monitoring** - See the progress of all agents
- 🎯 **Task management** - Assign different tasks to different agents
- 💻 **Terminal UI** - Clean, intuitive interface built with Bubble Tea

## Quick Start

### Installation

```bash
# Install via Homebrew (macOS/Linux)
brew install smtg-ai/claude-squad/claude-squad

# Or install from source
go install github.com/smtg-ai/claude-squad@latest

# Or download binary from releases
curl -L https://github.com/smtg-ai/claude-squad/releases/latest/download/claude-squad-linux-amd64 -o claude-squad
chmod +x claude-squad
```

### Basic Usage

```bash
# Start Claude Squad TUI
claude-squad

# Or use the shorter alias
cs

# Run with auto-yes mode (experimental)
cs -y

# Use a specific program
cs -p "aider --model claude-3-5-sonnet"
```

### Web Interface

Claude Squad also includes a modern web interface built with Next.js:

```bash
# Navigate to web directory
cd web/

# Install dependencies
npm install

# Start development server
npm run dev

# Open http://localhost:3000
```

## How it Works

1. **Create a new agent**: Press `n` in the TUI or create through web interface
2. **Choose your AI tool**: Claude Code, Aider, Codex, or any custom program
3. **Describe your task**: Tell the agent what you want to accomplish
4. **Monitor progress**: Watch in real-time as the agent works
5. **Review changes**: See git diffs before applying changes

Each agent:
- Runs in an isolated tmux session
- Works in its own git worktree (branch)
- Can be monitored independently
- Preserves state between sessions

## Supported AI Agents

- **Claude Code** - Anthropic's powerful coding assistant
- **Aider** - AI pair programming tool
- **GitHub Codex** - OpenAI's code generation model  
- **Custom programs** - Any command-line tool you specify

## Configuration

Claude Squad can be configured via:

- Command-line flags
- Environment variables
- Configuration files in `~/.claude-squad/`

### Key Commands

| Key | Action |
|-----|--------|
| `n` | Create new agent |
| `Enter` | View agent details |
| `d` | Delete agent |
| `r` | Restart agent |
| `↑/↓` | Navigate agents |
| `Tab` | Switch between Preview/Diff |
| `q` | Quit |

## Examples

### Web Development Team
```bash
# Frontend developer
cs -p "claude" --task "Create React login component"

# Backend developer  
cs -p "aider" --task "Build user authentication API"

# QA engineer
cs -p "claude" --task "Write comprehensive tests"
```

### Code Review
```bash
# Multiple perspectives on the same codebase
cs -p "claude" --task "Review for security issues"
cs -p "aider" --task "Optimize for performance"  
cs -p "claude" --task "Improve code documentation"
```

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│     TUI     │────│   Session    │────│    tmux     │
│  (Bubble)   │    │   Manager    │    │   Session   │
└─────────────┘    └──────────────┘    └─────────────┘
       │                   │                   │
       │                   │                   │
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Web Interface│────│ Git Worktree │────│ AI Agent    │
│  (Next.js)  │    │  Management  │    │ (Claude/etc)│
└─────────────┘    └──────────────┘    └─────────────┘
```

## Development

### Prerequisites
- Go 1.21+
- tmux
- git

### Building from Source

```bash
git clone https://github.com/smtg-ai/claude-squad.git
cd claude-squad
go build -o cs main.go
```

### Running Tests

```bash
go test ./...
```

### Web Development

```bash
cd web/
npm install
npm run dev
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Troubleshooting

### Common Issues

**Agent not responding:**
```bash
# Check tmux sessions
tmux list-sessions

# Reset all agents
cs reset
```

**Git worktree issues:**
```bash
# Clean up worktrees
git worktree prune

# Reset storage
rm -rf ~/.claude-squad/storage.json
```

**Web interface not loading:**
```bash
# Reinstall dependencies
cd web/
rm -rf node_modules package-lock.json
npm install
```

## License

Claude Squad is open source software licensed under the [MIT License](LICENSE.md).

## Links

- [GitHub Repository](https://github.com/smtg-ai/claude-squad)
- [Documentation](https://github.com/smtg-ai/claude-squad/wiki)
- [Issues](https://github.com/smtg-ai/claude-squad/issues)
- [Releases](https://github.com/smtg-ai/claude-squad/releases)