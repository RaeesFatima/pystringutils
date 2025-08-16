# Contributing to PyStringToolkit

First off, thanks for taking the time to contribute! Your help makes this project better for everyone.  

We welcome all kinds of contributions — from bug reports and code fixes to new features, documentation improvements, and examples.

---

## How to Contribute

### 1. Fork & Clone
1. Fork this repository on GitHub  
2. Clone your fork locally:  
   ```bash
   git clone https://github.com/<your-username>/pystringtoolkit.git
   cd pystringtoolkit
    ```
### 2. Setup Environment

We recommend creating a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

### 3. Run Tests

Make sure everything passes before pushing changes:
```
pytest
```

### 4. Make Your Changes

* Follow PEP8 style guidelines
* Add type hints where possible
* Write/update tests for your changes
* Update docs if you added/modified functionality

### 5. Submit a Pull Request
1. Push to your fork:
```commandline
git checkout -b feature/my-awesome-feature
git commit -m "Add my awesome feature"
git push origin feature/my-awesome-feature
```
2. Open a Pull Request on GitHub

### Reporting Issues

* Use GitHub Issues
* Clearly describe the problem (steps to reproduce, expected vs actual behavior, environment info)
* If possible, include code samples or screenshots
### Contribution Ideas
Not sure where to start? Here are some good places:

* Add new string utilities (validators, transformations, text stats)
* Improve documentation or examples
* Add more unit tests
* Optimize performance of existing functions
Check out issues labeled good first issue or help wanted.

### Recognition

All contributors will be credited in:

* GitHub Contributors graph
* Release notes
* README (via all-contributors)

We value every contribution, big or small ❤️

### Code of Conduct
By participating in this project, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
