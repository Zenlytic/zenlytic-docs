# Zenlytic Documentation

This repository contains the documentation for Zenlytic, built using MkDocs with the Material theme.

## Project Structure

```
.
├── assets/           # Images and other static assets
├── docs/            # Documentation content
│   ├── getting-started/
│   ├── data-sources/
│   ├── authentication/
│   ├── dashboards/
│   ├── data-modeling/
│   └── follow-ups/
├── mkdocs.yml       # MkDocs configuration
└── requirements.txt # Python dependencies
```

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install MkDocs and the Material theme:
   ```bash
   pip install mkdocs mkdocs-material
   ```

3. Serve the documentation locally:
   ```bash
   mkdocs serve
   ```

4. Build the documentation:
   ```bash
   mkdocs build
   ```

## Development

- Documentation is written in Markdown
- Images should be placed in the `assets/` directory
- Navigation is configured in `mkdocs.yml`
- The Material theme is used for styling and features

## Contributing

1. Create a new branch for your changes
2. Make your changes
3. Test locally using `mkdocs serve`
4. Submit a pull request 