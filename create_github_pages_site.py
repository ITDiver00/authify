import os


def create_github_pages_site():
    # Ensure files are created in the /authify folder
    project_root = os.path.dirname(os.path.abspath(__file__))

    # HTML content (updated to match your current index.html with Okta integration and private content)
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

    <div id="login-container"></div>
    <button id="login-btn">Login with Okta</button>
    <button id="logout-btn" style="display:none;">Logout</button>
    <div id="user-info"></div>

    <!-- Content only visible when logged in -->
    <div id="private-content" style="display:none; margin-top:2em;">
        <h2>Private Content</h2>
        <p>Welcome! You are now logged in and can see this protected content.</p>
        <!-- Add more private content here -->
    </div>

    <script src="https://global.oktacdn.com/okta-auth-js/7.4.0/okta-auth-js.min.js"></script>
    <script>
      const oktaDomain = 'https://lundencloud.oktapreview.com';
      const clientId = '0oab7br8m1dr3a5qK0x7';
      const redirectUri = 'https://itdiver00.github.io/authify/';

      const authClient = new OktaAuth({
        issuer: oktaDomain + '/oauth2/default',
        clientId: clientId,
        redirectUri: redirectUri,
        scopes: ['openid', 'profile', 'email'],
        pkce: true
      });

      async function handleLogin() {
        await authClient.token.getWithRedirect({
          responseType: ['token', 'id_token'],
          prompt: 'login'
        });
      }

      async function handleLogout() {
        const tokens = authClient.tokenManager.getTokensSync();
        const idToken = tokens.idToken ? tokens.idToken.idToken : '';
        const logoutUrl = `${oktaDomain}/oauth2/default/v1/logout?id_token_hint=${encodeURIComponent(idToken)}&post_logout_redirect_uri=${encodeURIComponent(redirectUri)}`;
        await authClient.tokenManager.clear();
        window.location.href = logoutUrl;
      }

      async function checkAuth() {
        const tokens = authClient.tokenManager.getTokensSync();
        if (tokens.idToken) {
          document.getElementById('login-btn').style.display = 'none';
          document.getElementById('logout-btn').style.display = 'inline-block';
          document.getElementById('user-info').innerText = 'Hello, ' + tokens.idToken.claims.name;
          document.getElementById('private-content').style.display = 'block';
        } else {
          document.getElementById('login-btn').style.display = 'inline-block';
          document.getElementById('logout-btn').style.display = 'none';
          document.getElementById('user-info').innerText = '';
          document.getElementById('private-content').style.display = 'none';
        }
      }

      authClient.token.parseFromUrl().then(function(res) {
        authClient.tokenManager.setTokens(res.tokens);
        window.location.replace('/authify/');
      }).catch(function() {
        // Not a redirect callback
      }).finally(checkAuth);

      document.getElementById('login-btn').onclick = handleLogin;
      document.getElementById('logout-btn').onclick = handleLogout;
    </script>
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

    # Write files directly to the /authify folder
    with open(os.path.join(project_root, "index.html"), "w") as f:
        f.write(html_content)

    with open(os.path.join(project_root, "style.css"), "w") as f:
        f.write(css_content)

    with open(os.path.join(project_root, "README.md"), "w") as f:
        f.write(readme_content)

    print("✅ Website files created in the /authify directory.")
    print("\n👉 Next steps:")
    print("1. Push these files to a GitHub repository.")
    print("2. Go to 'Settings' > 'Pages' and select 'main' branch (root).")
    print("3. Your site will be available at: https://<your-username>.github.io/<repo-name>/")


if __name__ == "__main__":
    create_github_pages_site()
