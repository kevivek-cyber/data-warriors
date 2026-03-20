# Data Warriors - Dash Application Deployment Guide

## Quick Start for Render Deployment

### 1. **Prepare Your Repository**
- Ensure all files are ready:
  - `app.py` (main application)
  - `requirements.txt` (dependencies)
  - `users.csv` (data)
  - `admin.csv` (data)
  - `Procfile` (tells Render how to run your app)
  - `render.yaml` (Render configuration)
  - `.gitignore` (what to exclude from git)

### 2. **Create a GitHub Repository**
```bash
# Navigate to your project folder
cd "DATA WARRIORS"

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - Data Warriors Dash app"

# Add GitHub remote (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 3. **Deploy on Render.com**

**Option A: Using Dashboard (Recommended)**
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Select your repository
5. Fill in the details:
   - **Name:** data-warriors (or any name you like)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:server`
   - **Region:** Choose closest to you (oregon, us-east, europe, etc.)
   - **Plan:** Free (or paid if you need more)
6. Click "Create Web Service"
7. Wait for deployment (typically 2-5 minutes)

**Option B: Using render.yaml (Automatic)**
If you use the `render.yaml` file included:
1. Push to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" → "Blueprint"
4. Select your GitHub repository
5. Click "Deploy"
6. Render will automatically read render.yaml and deploy

### 4. **Monitor Your Deployment**
- Go to your Render dashboard
- Click on your service
- Check "Logs" tab for any errors
- Once you see "Build successful", your app is live!
- Your app URL will be like: `https://data-warriors-xxxxx.onrender.com`

### 5. **Important Notes**

⚠️ **CSV Data Persistence:**
- Render has an ephemeral filesystem, which means CSV files are reset when the service restarts
- Data entered by users will be lost on app restart
- Solutions:
  - Use a database (PostgreSQL, MongoDB) instead of CSV
  - Use a cloud storage service (AWS S3, Azure Blob Storage)
  - Or keep CSV as prototype-only (as your app notes)

✅ **What Works:**
- Displaying existing data from CSV files
- Quiz functionality
- Admin dashboard
- Data visualization

### 6. **Troubleshooting**

**"ModuleNotFoundError"**
- Ensure `requirements.txt` has all needed packages
- Run locally: `pip install -r requirements.txt`
- Check Render build logs for details

**"Port" errors**
- The app automatically uses Render's assigned port
- No changes needed to app.py

**CSV files missing**
- Upload data to the CSV files before deploying
- Or add initial data to the app's file creation logic

### 7. **Next Steps (Optional Improvements)**

1. **Add a Database:**
   ```bash
   pip install psycopg2-binary SQLAlchemy
   ```
   Then modify app to use PostgreSQL instead of CSV

2. **Add Environment Variables:**
   In Render dashboard Settings → Environment:
   ```
   DASH_DEBUG=False
   FLASK_ENV=production
   ```

3. **Custom Domain:**
   In Render dashboard Settings → Custom Domain
   Add your own domain name (requires DNS configuration)

### 8. **Deploy Updates**
Push changes to GitHub:
```bash
git add .
git commit -m "Updated features"
git push origin main
```
Render automatically redeploys!

---

**Need Help?**
- Render Docs: https://render.com/docs
- Dash Docs: https://dash.plotly.com/
- GitHub: https://docs.github.com/
