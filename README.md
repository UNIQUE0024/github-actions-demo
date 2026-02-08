# GitHub Actions CI/CD Demo Project

A complete CI/CD pipeline using GitHub Actions with Flask application.

## ✅ What's Included

- **Flask Application**: Simple REST API with health checks
- **GitHub Actions CI/CD**: Automated testing, building, and validation
- **Docker Support**: Container image with health checks
- **Kubernetes Manifests**: Deployment, Service, Namespace
- **Comprehensive Tests**: Unit tests with pytest
- **Code Quality**: Flake8 linting

## 📁 Project Structure

```
github-actions-complete/
├── .github/
│   └── workflows/
│       └── ci.yml              # Main CI/CD pipeline
├── app/
│   ├── __init__.py             # Makes app a Python package
│   ├── app.py                  # Flask application
│   ├── requirements.txt        # Python dependencies
│   └── Dockerfile              # Container image definition
├── tests/
│   ├── __init__.py             # Test package
│   └── test_app.py             # Unit tests (FIXED IMPORTS!)
├── kubernetes/
│   ├── namespace.yaml          # K8s namespace
│   ├── deployment.yaml         # K8s deployment
│   └── service.yaml            # K8s service
├── .gitignore                  # Git ignore rules
├── pytest.ini                  # Pytest configuration
└── README.md                   # This file
```

## 🚀 Quick Start

### 1. Upload to GitHub

**UPLOAD THESE FILES:**
- ✅ `.github/` folder (with workflows)
- ✅ `app/` folder (all files)
- ✅ `tests/` folder (all files)
- ✅ `kubernetes/` folder (all files)
- ✅ `.gitignore`
- ✅ `pytest.ini`
- ✅ `README.md`

**DO NOT UPLOAD:**
- ❌ `__pycache__/` folders
- ❌ `.pytest_cache/` folders
- ❌ `venv/` or `env/` folders
- ❌ `.coverage` files
- ❌ `*.pyc` files

### 2. Create Repository

1. Go to github.com
2. Click "New repository"
3. Name: `github-actions-demo`
4. Public or Private
5. DON'T add README (we have one)
6. Create repository

### 3. Upload Files

**Method A: Web Upload (Easiest)**
```
1. Click "uploading an existing file"
2. Drag ALL folders and files
3. Commit message: "Initial commit"
4. Click "Commit changes"
```

**Method B: Git Command Line**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/github-actions-demo.git
git push -u origin main
```

### 4. Watch It Run

1. Go to "Actions" tab
2. See workflow running
3. Wait 3-5 minutes
4. All checks should pass ✅

## 🧪 Running Tests Locally

```bash
# Install dependencies
pip install -r app/requirements.txt
pip install pytest pytest-cov flake8

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app

# Run linting
flake8 app/
```

## 🐳 Docker

```bash
# Build image
cd app
docker build -t github-actions-demo .

# Run container
docker run -p 8080:8080 github-actions-demo

# Test
curl http://localhost:8080/health
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home - welcome message |
| `/health` | GET | Health check |
| `/ready` | GET | Readiness probe |
| `/api/info` | GET | Application info |
| `/api/echo` | POST | Echo posted data |

## 🔧 CI/CD Pipeline

### Workflow Jobs

1. **Test** (runs first)
   - Lint code with flake8
   - Run pytest unit tests
   - Generate coverage report
   
2. **Build** (after test passes)
   - Build Docker image
   - Push to GitHub Container Registry
   
3. **Validate K8s** (after test passes)
   - Validate Kubernetes YAML files
   
4. **Summary** (always runs)
   - Show results of all jobs

### Triggers

- Push to `main` or `develop`
- Pull requests to `main`
- Manual trigger (workflow_dispatch)

## ☸️ Kubernetes Deployment

```bash
# Create namespace
kubectl apply -f kubernetes/namespace.yaml

# Deploy application
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# Check status
kubectl get pods -n demo
kubectl get svc -n demo

# Test
kubectl port-forward -n demo svc/github-actions-demo 8080:80
curl http://localhost:8080/health
```

## 🔍 Troubleshooting

### Tests Fail
- Check import errors in test_app.py
- Verify `app/__init__.py` exists
- Ensure Python 3.11 is used

### Build Fails
- Check Dockerfile syntax
- Verify requirements.txt has all deps

### K8s Validation Fails
- Check YAML syntax
- Verify indentation is correct

## 📝 Key Files Explained

### `app/__init__.py`
Makes `app` directory a Python package so it can be imported.

### `tests/test_app.py`
Contains all unit tests. **CRITICAL**: Has fixed import with sys.path.insert()

### `.github/workflows/ci.yml`
Defines the CI/CD pipeline that runs on every push.

### `pytest.ini`
Configures pytest behavior, test discovery, and coverage.

## ✨ Features

- ✅ Automated testing on every push
- ✅ Docker image building and pushing
- ✅ Kubernetes manifest validation
- ✅ Code coverage reporting
- ✅ Linting with flake8
- ✅ Health checks for K8s
- ✅ Multi-stage Docker builds
- ✅ GitHub Container Registry integration

## 🎯 What Gets Tested

- ✅ All API endpoints return 200
- ✅ JSON responses are valid
- ✅ Health checks work
- ✅ Echo endpoint works
- ✅ 404 errors handled properly
- ✅ Code coverage > 80%

## 🔒 Security

- Non-root Docker user (production)
- Health checks for container orchestration
- Minimal Docker image (Python slim)
- GitHub Actions automatic token management

## 📦 Dependencies

- Flask 3.0.0
- Werkzeug 3.0.1
- pytest 7.4+
- pytest-cov 4.1+
- flake8 6.1+

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Run tests locally
5. Push and create PR
6. Wait for CI to pass

## 📄 License

MIT License - feel free to use for learning!

## 🆘 Support

If you have issues:
1. Check Actions logs for exact error
2. Read error messages carefully
3. Verify all files uploaded correctly
4. Check file structure matches above

---

**Ready to deploy!** Just upload to GitHub and watch it work! 🚀
