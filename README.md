# Smoke test
# Test after Kimi fix
# Test Moonshot API

## Hosting the frontend on Vercel

Yes. The landing frontend in `static/index.html` can be deployed to Vercel as a static app while this FastAPI service continues to run as the API.

1. Deploy this repository to Vercel as a static project. The included `vercel.json` rewrites app routes to `static/index.html`.
2. Configure the frontend API base URL by copying `static/config.example.js` to `static/config.js` in your Vercel deployment and setting:

   ```js
   window.DRUFIY_API_BASE = "https://YOUR_BACKEND_DOMAIN";
   ```

3. Configure the backend environment so browser requests from Vercel are accepted:

   ```bash
   FRONTEND_URL=https://YOUR_VERCEL_APP.vercel.app
   # Optional for Vercel preview deployments:
   FRONTEND_ORIGIN_REGEX=https://.*\\.vercel\\.app
   ```

4. In your GitHub OAuth app, add the Vercel URL as an allowed callback URL that matches the page serving `static/index.html`.
