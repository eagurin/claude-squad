# CLAUDE.md - Claude Squad Project Guidelines

## Project Overview
Claude Squad is a Go-based terminal UI multiplexer for managing multiple Claude sessions.

## Code Style Guidelines

### Go Code Standards
- Follow standard Go formatting (gofmt)
- Use meaningful variable and function names
- Add comments for exported functions
- Handle errors explicitly
- Use interfaces for testability

### Project Structure
- `/app` - Core application logic
- `/cmd` - Command handling
- `/config` - Configuration management
- `/daemon` - Background service logic
- `/session` - Session management (git, tmux)
- `/ui` - Terminal UI components
- `/web` - Web interface (Next.js)

## PR Guidelines

When creating PRs:
1. Keep changes focused and atomic
2. Write clear commit messages
3. Add tests for new functionality
4. Update documentation if needed
5. Ensure all tests pass

## Testing Requirements
- Write unit tests for new functions
- Test coverage should not decrease
- Run `go test ./...` before creating PR

## Security Considerations
- Never commit API keys or secrets
- Validate all user input
- Use secure communication for daemon

## Dependencies
- Minimize external dependencies
- Document why each dependency is needed
- Keep go.mod tidy

## Error Handling
- Return errors, don't panic
- Provide context with errors using fmt.Errorf
- Log errors appropriately