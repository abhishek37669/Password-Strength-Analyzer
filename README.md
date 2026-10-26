

\# Password Strength Analyzer



A Python and Streamlit cybersecurity project that evaluates basic password characteristics and generates random passwords using Python's `secrets` module.



\## Features



\- Password length and character variety checks

\- Basic common-password and predictable-sequence detection

\- Strength score and actionable suggestions

\- Random password generator with adjustable length

\- Local analysis without intentionally storing entered passwords



\## Technologies



\- Python

\- Streamlit

\- Python `secrets` module



\## Installation



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd Password-Strength-Analyzer

python -m venv venv

```



Activate the environment on Windows:



```bat

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\## Run the application



```bash

streamlit run app.py

```



\## Security note



This is an educational project, not a production authentication system. Its scoring rules are heuristic and cannot guarantee password security. Do not enter real passwords into public or untrusted deployments.



\## Author



Abhishek Nuchu



