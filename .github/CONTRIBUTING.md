# Contributing to Testified

We love your input! We want to make contributing to Testified as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Commit Messages

We follow [Conventional Commits](https://www.conventionalcommits.org/) specification. This leads to more readable messages that are easy to follow when looking through the project history.

Each commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

Examples:
```
feat(auth): add login with Google OAuth
fix(api): handle null response from user endpoint
docs(readme): update installation instructions
```

## Pull Request Process

1. Update the README.md with details of changes to the interface, if applicable.
2. Update the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
3. The PR may be merged once you have the sign-off of at least one other developer.

## Any Questions?

Don't hesitate to create an issue with the tag `question` if you have any questions about how to contribute.

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
