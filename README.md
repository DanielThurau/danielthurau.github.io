# Daniel Thurau's Personal Website

This is the source code for my personal website hosted at [thurau.io](https://www.thurau.io). It's a Jekyll-based static site that showcases my projects, blog posts, and professional information.

## 🏗️ Architecture

This is a **Jekyll static site** with the following structure:

### Core Components
- **Jekyll 4.3.3** - Static site generator
- **no-style-please theme** - Minimal, clean design theme
- **GitHub Pages** - Hosting platform

### Directory Structure
```
danielthurau.github.io/
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML templates
│   ├── default.html     # Base layout
│   ├── home.html        # Homepage layout
│   ├── page.html        # Standard page layout
│   ├── post.html        # Blog post layout
│   └── archive.html     # Archive page layout
├── _includes/           # Reusable HTML components
├── _posts/              # Blog posts (Markdown)
├── _sass/               # SCSS stylesheets
├── assets/              # Static assets (CSS, JS, images)
├── images/              # Image galleries for projects
├── pdfs/                # PDF documents (resume, etc.)
└── [content pages]      # About, projects, economics, etc.
```

### Key Features
- **Minimal Design**: Clean, fast-loading pages
- **Project Showcases**: Dedicated pages for hardware projects
- **Blog Posts**: Technical writing and updates
- **Responsive**: Works on desktop and mobile
- **Analytics**: GoatCounter integration for privacy-friendly analytics

## 🎯 Purpose

This website serves as my digital home on the internet, featuring:

- **Professional Information**: About me, resume, contact details
- **Project Portfolio**: Showcases of hardware and software projects
- **Blog**: Technical writing and project updates
- **Personal Branding**: Consistent online presence

## 🚀 Local Development

### Prerequisites
- **Ruby** (2.7 or higher)
- **Bundler** (`gem install bundler`)
- **Git**

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/DanielThurau/danielthurau.github.io.git
   cd danielthurau.github.io
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Start the development server**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open your browser and navigate to `http://localhost:4000`

### Development Workflow

1. **Create new blog posts**
   - Add Markdown files to `_posts/` directory
   - Use the format: `YYYY-MM-DD-title.md`
   - Include front matter with layout, title, and other metadata

2. **Add new pages**
   - Create Markdown files in the root directory
   - Include front matter with layout and title
   - Use `layout: page` for standard pages

3. **Modify styling**
   - Edit files in `_sass/` directory
   - Main stylesheet: `assets/css/main.scss`

4. **Add images**
   - Place images in `images/` directory
   - Reference them in Markdown using relative paths

### Useful Commands

```bash
# Start development server with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Serve with drafts
bundle exec jekyll serve --drafts

# Check for broken links
bundle exec jekyll build
bundle exec htmlproofer ./_site
```

## 📝 Content Management

### Blog Posts
- Location: `_posts/`
- Format: Markdown with YAML front matter
- Example front matter:
  ```yaml
  ---
  layout: post
  title: "Your Post Title"
  date: 2024-01-01
  ---
  ```

### Pages
- Location: Root directory
- Format: Markdown with YAML front matter
- Example front matter:
  ```yaml
  ---
  layout: page
  title: "Page Title"
  ---
  ```

### Project Pages
- Create dedicated directories for project images
- Reference projects in `projects.md`
- Use consistent naming conventions

## 🎨 Customization

### Theme Configuration
The site uses the `no-style-please` theme with customizations in `_config.yml`:

```yaml
theme_config:
  appearance: "auto"  # light, dark, or auto
  back_home_text: ".."
  date_format: "%Y-%m-%d"
  show_description: true
```

### Custom Styles
- Main stylesheet: `assets/css/main.scss`
- Custom SCSS in `_sass/` directory
- Override theme defaults as needed

## 🔧 Deployment

This site is automatically deployed via **GitHub Pages**:

1. Push changes to the `main` branch
2. GitHub Pages automatically builds and deploys
3. Site is available at `https://danielthurau.github.io`
4. Custom domain configured via `CNAME` file

### Manual Deployment
```bash
# Build the site
bundle exec jekyll build

# The built site is in `_site/` directory
# Upload contents to your web server
```

## 📊 Analytics

The site uses **GoatCounter** for privacy-friendly analytics:
- Only active in production environment
- No cookies or tracking scripts
- Respects user privacy

## 🤝 Contributing

While this is a personal website, if you find issues or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [LICENSE](LICENSE) file.

## 🔗 Links

- **Live Site**: [thurau.io](https://www.thurau.io)
- **GitHub**: [@DanielThurau](https://github.com/DanielThurau)
- **Twitter**: [@DanielNThurau](https://twitter.com/DanielNThurau)

---

*Built with Jekyll and hosted on GitHub Pages* 