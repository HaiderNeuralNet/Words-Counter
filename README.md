<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📝 Word Counter App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0E1117;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 1000px;
            margin: auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #FFA500;
        }
        a {
            color: #1E90FF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .badge {
            display: inline-block;
            margin: 5px 5px 5px 0;
        }
        .section {
            margin-bottom: 40px;
        }
        .screenshot {
            border-radius: 10px;
            box-shadow: 0px 0px 15px #222;
            margin: 10px 0;
            max-width: 100%;
        }
        pre {
            background-color: #1c1c1c;
            padding: 15px;
            border-radius: 10px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Word Counter App</h1>

        <!-- Streamlit Open Badge -->
        <div class="section">
            <a href="https://words-counter89.streamlit.app/" target="_blank">
                <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
            </a>
        </div>

        <!-- Badges -->
        <div class="section">
            <img class="badge" src="https://img.shields.io/badge/Python-3.11-blue" alt="Python 3.11">
            <img class="badge" src="https://img.shields.io/badge/Streamlit-1.29-orange" alt="Streamlit 1.29">
            <img class="badge" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
        </div>

        <!-- Description -->
        <div class="section">
            <h2>About</h2>
            <p>A sleek, dark-themed Word Counter web app built with <strong>Streamlit</strong>. Instantly count words, characters, and lines with a modern GUI interface. Perfect for writers, students, and anyone who needs quick text analysis.</p>
        </div>

        <!-- Demo / Screenshots -->
        <div class="section">
            <h2>🎨 Screenshots</h2>
            <h3>Paste your text:</h3>
            <img class="screenshot" src="https://via.placeholder.com/500x200?text=Paste+your+text+here" alt="Text Input">
            <h3>Results:</h3>
            <img class="screenshot" src="https://via.placeholder.com/500x200?text=Words+Characters+Lines+Results" alt="Results Preview">
        </div>

        <!-- Features -->
        <div class="section">
            <h2>🚀 Features</h2>
            <ul>
                <li>🌓 Dark-themed GUI</li>
                <li>📊 Counts Words, Characters, and Lines</li>
                <li>⚡ Minimal, responsive interface</li>
                <li>✅ Easy to use – paste text and click</li>
            </ul>
        </div>

        <!-- Installation -->
        <div class="section">
            <h2>💻 Installation</h2>
            <pre>
# Clone the repo
git clone https://github.com/yourusername/word-counter-app.git
cd word-counter-app

# Optional: create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install streamlit
            </pre>
        </div>

        <!-- Run the app -->
        <div class="section">
            <h2>🏃‍♂️ Run the App</h2>
            <pre>
streamlit run app.py
            </pre>
            <p>The app opens in your browser at: <strong>http://localhost:8501</strong></p>
        </div>

        <!-- Usage -->
        <div class="section">
            <h2>📝 How to Use</h2>
            <ol>
                <li>Paste your text in the text area.</li>
                <li>Click <strong>🔍 Count Words</strong>.</li>
                <li>View metrics: <strong>Words</strong>, <strong>Characters</strong>, <strong>Lines</strong>.</li>
                <li>If empty, a warning will prompt you to enter text.</li>
            </ol>
        </div>

        <!-- Code Highlights -->
        <div class="section">
            <h2>🔧 Code Highlights</h2>
            <pre>
# Count words, characters, lines
words = len(text.split())
characters = len(text)
lines = len(text.splitlines())

# Display results in columns
col1, col2, col3 = st.columns(3)
col1.metric("Words", words)
col2.metric("Characters", characters)
col3.metric("Lines", lines)
            </pre>
        </div>

        <!-- Future Improvements -->
        <div class="section">
            <h2>⚡ Future Improvements</h2>
            <ul>
                <li>Add text file upload support</li>
                <li>Show reading time estimation</li>
                <li>Support multiple languages</li>
                <li>Deploy online for public access</li>
            </ul>
        </div>

        <!-- License -->
        <div class="section">
            <h2>📜 License</h2>
            <p>MIT License © <a href="https://github.com/HaiderNeuralNet">Haider Ali Shah</a></p>
        </div>
    </div>
</body>
</html>
