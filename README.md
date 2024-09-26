<div align="center">
  <h1>Robot Framework Metrics</h1>
  <p>
     Custom HTML report (dashboard view) by parsing robotframework output.xml file
  </p>

<!-- Badges -->
<p>
  <a href="https://github.com/adiralashiva8/robotframework-metrics/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/adiralashiva8/robotframework-metrics" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/adiralashiva8/robotframework-metrics" alt="last update" />
  </a>
  <a href="https://github.com/adiralashiva8/robotframework-metrics/network/members">
    <img src="https://img.shields.io/github/forks/adiralashiva8/robotframework-metrics" alt="forks" />
  </a>
  <a href="https://github.com/adiralashiva8/robotframework-metrics/stargazers">
    <img src="https://img.shields.io/github/stars/adiralashiva8/robotframework-metrics" alt="stars" />
  </a>
  <a href="https://github.com/adiralashiva8/robotframework-metrics/issues/">
    <img src="https://img.shields.io/github/issues/adiralashiva8/robotframework-metrics" alt="open issues" />
  </a>
  <a href="https://github.com/adiralashiva8/robotframework-metrics/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/adiralashiva8/robotframework-metrics.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://adiralashiva8.github.io/robotframework-metrics/metrics.png" target="_blank">View Demo</a>
  <span> · </span>
    <a href="https://github.com/adiralashiva8/robotframework-metrics/blob/master/README.md">Documentation</a>
  <span> · </span>
    <a href="https://github.com/adiralashiva8/robotframework-metrics/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/adiralashiva8/robotframework-metrics/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# 📔 Table of Contents

- [About the Project](#-about-the-project)
  * [Screenshots](#-screenshots)
  * [Tech Stack](#-tech-stack)
  * [Features](#-features)
- [Getting Started](#-getting-started)
  * [Installation](#-installation)
- [Usage](#usage)
  * [Continuous Integration (CI) Setup](#-cisetup)
- [Contact](#-contact)
- [Acknowledgements](#-acknowledgements)

<!-- About the Project -->
## 🌟 About the Project

`Robot Framework Metrics` is a tool designed to generate comprehensive `HTML reports` from Robot Framework's `output.xml` files. These reports provide a __dashboard view__, offering detailed insights into your test executions, including __suite__ statistics, __test case__ results, and __keyword__ performance.

<!-- Screenshots -->
### 📷 Screenshots

![Metrics Report](https://adiralashiva8.github.io/robotframework-metrics/metrics.png)

<!-- TechStack -->
### 🛠️ Tech Stack

<details>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://robot-framework.readthedocs.io/en/stable/autodoc/robot.result.html">Robotframework results api</a></li>
    <li><a href="https://pandas.pydata.org/docs/getting_started/index.html">Pandas</a></li>
    <li><a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja2</a></li>
  </ul>
</details>

<!-- Features -->
### 🎯 Features

- *Custom HTML Report:* Create visually appealing and informative dashboard.
- *Detailed Metrics:* Access suite, test case, keyword statistics, status, and elapsed time.
- *Support for RF7:* Fully compatible with Robot Framework 7 (from v3.5.0 onwards).
- *Command-Line Interface:* Easy-to-use CLI for report generation.


<!-- Getting Started -->
## 🧰 Getting Started

<!-- Installation -->
### ⚙️ Installation

You can install `robotframework-metrics` using one of the following methods:

__Method 1__: Using pip
```
pip install robotframework-metrics==3.3.3
```

__Method 2__: From Source (clone the repository and install using setup.py)
```
git clone https://github.com/adiralashiva8/robotframework-metrics.git
cd robotframework-metrics
python setup.py install
```

__Method 3__: Latest Development Version  (**Recommended**) (for the latest features and RF7 support)
```
pip install git+https://github.com/adiralashiva8/robotframework-metrics
```

__DOCKER__:
```
docker pull adiralashiva8/robotframework-metrics:latest
```

<!-- Usage -->
## 👀 Usage

After executing your Robot Framework tests, you can generate a metrics report by running:

__Default Configuration__: If `output.xml` is in the current directory
```
robotmetrics
```

__Custom Path__: If `output.xml` is located in a different directory
```
robotmetrics --inputpath ./Result/ --output output1.xml
```

For more options:
```
robotmetrics --help
```

### 🧪 Continuous Integration (CI) Setup

To automate report generation in CI/CD pipelines, add the following steps to your pipeline configuration:

1. Run tests with Robot Framework
2. Generate the metrics report
   ```
   robot test.robot &
   robotmetrics [:options]
   ```
   > & is used to execute multiple command's in .bat file

<!-- Contact -->
## 🤝 Contact

For any questions, suggestions, or feedback, please contact:

- Email: <a href="mailto:adiralashiva8@gmail.com?Subject=Robotframework%20Metrics" target="_blank">`adiralashiva8@gmail.com`</a> 

<!-- Acknowledgments -->
## 💎 Acknowledgements

Special thanks to the following individuals for their guidance, contributions, and feedback:

*Idea, Guidance and Support:*
 - Steve Fisher
 - Goutham Duduka

*Contributors:*
1. [Pekka Klarck](https://www.linkedin.com/in/pekkaklarck/) [Author of robotframework]
2. [Ruud Prijs](https://www.linkedin.com/in/ruudprijs/)
3. [Jesse Zacharias](https://www.linkedin.com/in/jesse-zacharias-7926ba50/)
4. [Bassam Khouri](https://www.linkedin.com/in/bassamkhouri/)
5. [Francesco Spegni](https://www.linkedin.com/in/francesco-spegni-34b39b61/)
6. [Sreelesh Kunnath](https://www.linkedin.com/in/kunnathsree/)

*Feedback:*
1. [Mantri Sri](https://www.linkedin.com/in/mantri-sri-4a0196133/)
2. [Prasad Ozarkar](https://www.linkedin.com/in/prasad-ozarkar-b4a61017/)
3. [Suresh Parimi](https://www.linkedin.com/in/sparimi/)
4. [Amit Lohar](https://github.com/amitlohar)
5. [Robotframework community users](https://groups.google.com/forum/#!forum/robotframework-users)

---

⭐ Star this repository if you find it useful! (it motivates)

---
