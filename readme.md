# Isaac Daviet — Personal Website

Source code for my personal website, built with plain HTML, CSS, and JavaScript.

## Live Site

The site is hosted via GitHub Pages at:

```
https://idaviet.github.io/personal_website/
```

## Pages

| Page | Description |
|---|---|
| `index.html` | CV / portfolio — research experience, education, skills, projects, and interests |
| `photos.html` | Analog film photography gallery, organized by trip and location |

## Project Structure

```
personal_website/
├── index.html              # Main CV / portfolio page
├── photos.html             # Travel photography gallery
├── image_rename.py         # Utility script for batch-renaming image files
├── assets/
│   └── img/
│       ├── profile.jpg     # Profile photo
│       └── photos_page/    # Gallery images, organized by trip
│           ├── florida/
│           ├── japan/
│           ├── new_york/
│           ├── croatia/
│           ├── italy/
│           ├── alps/
│           ├── sweden/
│           ├── north_cascades/
│           ├── oregon_coast/
│           └── paris/
├── css/                    # Stylesheets
├── js/                     # JavaScript files
└── README.md
```

## Local Development

To run the site locally, simply open either HTML file in a browser:

```
open index.html
```

No build step, framework, or server is required — the site is pure static HTML.

## Photo Gallery

The `photos.html` page displays analog film photography from various trips. Images live in `assets/img/photos_page/`, organized by destination. The `image_rename.py` script can be used to batch-rename image files before adding new trips to the gallery:

```
python image_rename.py --dir assets/img/photos_page/new_trip/ --prefix photo_
```

## Deployment

This repository is configured for GitHub Pages. Any push to `main` is automatically deployed to ```www.isaacdaviet.info```
