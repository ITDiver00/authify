import os


def create_github_pages_site():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My GitHub Pages Site</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Welcome to My GitHub Pages Site!</h1>
    <p>This is a static website hosted on GitHub Pages.</p>
</body>
</html>"""

    # CSS content
    css_content = """body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
    background-color: #f4f4f4;
    color: #333;
}"""

    # README
    readme_content = "# My GitHub Pages Site\nA simple static website ready for GitHub Pages."

    # Write files directly to the project root
    with open(os.path.join(project_root, "index.html"), "w") as f:
        f.write(html_content)

    with open(os.path.join(project_root, "style.css"), "w") as f:
        f.write(css_content)

    with open(os.path.join(project_root, "README.md"), "w") as f:
        f.write(readme_content)

    print("✅ Website files created in the project root directory.")
    print("\n👉 Next steps:")
    print("1. Push these files to a GitHub repository.")
    print("2. Go to 'Settings' > 'Pages' and select 'main' branch (root).")
    print("3. Your site will be available at: https://<your-username>.github.io/<repo-name>/")


if __name__ == "__main__":
    create_github_pages_site()
