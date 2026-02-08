"""
Simple Flask Application for GitHub Actions Demo
"""

from flask import Flask, jsonify, request
import logging
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Application metadata
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')


@app.route('/')
def home():
    """Home endpoint - returns welcome message"""
    logger.info("Home endpoint accessed")
    return jsonify({
        "message": "Hello from GitHub Actions!",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route('/health')
def health():
    """Health check endpoint for Kubernetes probes"""
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION,
        "environment": ENVIRONMENT
    }), 200


@app.route('/ready')
def ready():
    """Readiness probe endpoint"""
    return jsonify({
        "status": "ready",
        "version": APP_VERSION
    }), 200


@app.route('/api/info')
def info():
    """Application information endpoint"""
    return jsonify({
        "name": "GitHub Actions Demo App",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "features": [
            "RESTful API",
            "Health checks",
            "Kubernetes ready",
            "CI/CD integrated"
        ]
    })


@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint - returns posted data"""
    data = request.get_json()
    logger.info(f"Echo endpoint called with data: {data}")
    return jsonify({
        "received": data,
        "timestamp": datetime.utcnow().isoformat()
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource was not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred"
    }), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    logger.info(f"Starting application on port {port}")
    logger.info(f"Environment: {ENVIRONMENT}")
    logger.info(f"Version: {APP_VERSION}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=(ENVIRONMENT == 'development')
    )
