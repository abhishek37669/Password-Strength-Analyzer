
import string
import secrets
import streamlit as st

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

COMMON_PASSWORDS = {
    "password", "password123", "12345678", "123456789",
    "qwerty", "qwerty123", "admin", "admin123",
    "letmein", "welcome123", "iloveyou", "abc123"
}

SEQUENCES = [
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]


def has_sequence(password):
    value = password.lower()
    for sequence in SEQUENCES:
        for i in range(len(sequence) - 2):
            part = sequence[i:i + 3]
            if part in value or part[::-1] in value:
                return True
    return False


def analyze_password(password):
    feedback = []
    score = 0
    length = len(password)

    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters; 16 or more is better.")

    checks = [
        (any(c.islower() for c in password),
         "Add lowercase letters."),
        (any(c.isupper() for c in password),
         "Add uppercase letters."),
        (any(c.isdigit() for c in password),
         "Add numbers."),
        (any(c in string.punctuation for c in password),
         "Consider adding symbols.")
    ]

    for passed, suggestion in checks:
        if passed:
            score += 1
        else:
            feedback.append(suggestion)

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a common password. Choose a different one.")

    if len(password) >= 4 and len(set(password)) <= 2:
        score = min(score, 1)
        feedback.append("Avoid repeating the same few characters.")

    if has_sequence(password):
        score = max(0, score - 1)
        feedback.append("Avoid predictable sequences like abc or 123.")

    if length < 12:
        score = min(score, 3)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Fair"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return min(score, 7), strength, list(dict.fromkeys(feedback))


def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%&*?"
    while True:
        password = "".join(
            secrets.choice(alphabet) for _ in range(length)
        )
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in "!@#$%&*?" for c in password)
        ):
            return password


st.title("🔐 Password Strength Analyzer")
st.caption("A local educational tool for password security")

st.markdown(
    "Check password characteristics, receive improvement tips, "
    "and generate a random password."
)

st.info(
    "For this local version, analysis runs in your local Python process. "
    "Do not enter real passwords into public or untrusted websites."
)

password = st.text_input(
    "Enter a sample password",
    type="password",
    placeholder="Try a password you do not use elsewhere"
)

if password:
    score, strength, feedback = analyze_password(password)

    st.subheader(f"Strength: {strength}")
    st.progress(score / 7)
    st.write(f"Score: {score}/7")

    if strength == "Weak":
        st.error("This password needs improvement.")
    elif strength == "Fair":
        st.warning("Consider improving this password.")
    else:
        st.success("Good password characteristics.")

    if feedback:
        st.markdown("#### Recommendations")
        for item in feedback:
            st.write(f"- {item}")
    else:
        st.write("No basic improvement suggestions.")

st.divider()
st.subheader("Generate a Secure Password")

length = st.slider("Password length", 12, 32, 16)

if st.button("Generate Secure Password"):
    st.session_state.generated_password = generate_password(length)

if "generated_password" in st.session_state:
    st.code(st.session_state.generated_password)
    st.caption(
        "Generated using Python's secrets module. "
        "Store passwords in a trusted password manager."
    )
