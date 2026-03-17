<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📝 Word Counter App - README</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0E1117;
            color: #e0e0e0;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            width: 90%;
            max-width: 1000px;
            margin: 0 auto;
            padding: 30px;
            background-color: #1a1a1a;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        }
        h1 {
            color: #FFA500;
            font-size: 2.5em;
            margin-bottom: 10px;
            border-bottom: 2px solid #333;
            padding-bottom: 15px;
        }
        h2 {
            color: #FFA500;
            font-size: 1.8em;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        h3 {
            color: #FFA500;
            font-size: 1.3em;
            margin: 15px 0 10px;
        }
        a {
            color: #1E90FF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
            color: #FFA500;
        }
        .badge {
            display: inline-block;
            margin: 5px;
            border-radius: 4px;
        }
        .section {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #242424;
            border-radius: 12px;
            border-left: 4px solid #FFA500;
        }
        .screenshot {
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            margin: 15px 0;
            max-width: 100%;
            border: 1px solid #333;
        }
        pre {
            background-color: #2d2d2d;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.5;
            color: #e6e6e6;
            border: 1px solid #444;
            margin: 15px 0;
        }
        code {
            background-color: #2d2d2d;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            color: #FFA500;
        }
        ul, ol {
            padding-left: 25px;
            margin: 10px 0;
        }
        li {
            margin: 8px 0;
        }
        hr {
            border: none;
            border-top: 1px solid #333;
            margin: 30px 0;
        }
        .badge-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #333;
            color: #888;
        }
        .screenshot-placeholder {
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            padding: 30px;
            text-align: center;
            border-radius: 10px;
            border: 2px dashed #FFA500;
            color: #888;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Word Counter App</h1>

        <!-- Streamlit Open Badge -->
        <div class="badge-container">
            <a href="https://words-counter89.streamlit.app/" target="_blank">
                <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit" class="badge">
            </a>
        </div>

        <!-- Badges -->
        <div class="badge-container">
            <img class="badge" src="https://img.shields.io/badge/Python-3.11-blue" alt="Python 3.11">
            <img class="badge" src="https://img.shields.io/badge/Streamlit-1.29-orange" alt="Streamlit 1.29">
            <img class="badge" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
            <img class="badge" src="https://img.shields.io/badge/Version-1.0.0-brightgreen" alt="Version 1.0.0">
        </div>

        <!-- Description -->
        <div class="section">
            <h2>📌 About</h2>
            <p>A sleek, dark-themed Word Counter web app built with <strong>Streamlit</strong>. Instantly count words, characters, and lines with a modern GUI interface. Perfect for writers, students, and anyone who needs quick text analysis.</p>
        </div>

        <!-- Live Demo -->
        <div class="section">
            <h2>🚀 Live Demo</h2>
            <p>Try the app live: <a href="https://words-counter89.streamlit.app/" target="_blank">https://words-counter89.streamlit.app/</a></p>
        </div>

        <!-- Screenshots -->
        <div class="section">
            <h2>🎨 Screenshots</h2>
            
            <h3>📋 Text Input Interface:</h3>
            <div class="screenshot-placeholder">
                [Screenshot: Text input area with "Paste your text here" field and Count Words button]
            </div>
            
            <h3>📊 Results Display:</h3>
            <div class="screenshot-placeholder">
                [Screenshot: Results showing Words: 42, Characters: 256, Lines: 5 with success message]
            </div>
        </div>

        <!-- Features -->
        <div class="section">
            <h2>✨ Features</h2>
            <ul>
                <li><strong>🌓 Dark-themed GUI</strong> - Easy on the eyes with modern dark interface</li>
                <li><strong>📊 Real-time Analysis</strong> - Counts Words, Characters, and Lines instantly</li>
                <li><strong>⚡ Minimal & Responsive</strong> - Clean interface that works on all devices</li>
                <li><strong>✅ Simple Workflow</strong> - Just paste your text and click count</li>
                <li><strong>🎯 User-friendly</strong> - Success messages and warnings for empty input</li>
            </ul>
        </div>

        <!-- Installation -->
        <div class="section">
            <h2>💻 Installation</h2>
            <pre># Clone the repository
git clone https://github.com/yourusername/word-counter-app.git
cd word-counter-app

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install streamlit</pre>
        </div>

        <!-- Run the app -->
        <div class="section">
            <h2>🏃‍♂️ Run the App Locally</h2>
            <pre>streamlit run main.py</pre>
            <p>The app will automatically open in your browser at: <strong>http://localhost:8501</strong></p>
        </div>

        <!-- Usage -->
        <div class="section">
            <h2>📝 How to Use</h2>
            <ol>
                <li><strong>Step 1:</strong> Paste or type your text in the large text area.</li>
                <li><strong>Step 2:</strong> Click the <code>🔍 Count Words</code> button.</li>
                <li><strong>Step 3:</strong> View your results showing:
                    <ul>
                        <li>📝 Total Words</li>
                        <li>📏 Total Characters</li>
                        <li>📊 Total Lines</li>
                    </ul>
                </li>
                <li><strong>Step 4:</strong> If no text is entered, a warning message will appear.</li>
            </ol>
        </div>

        <!-- Code Highlights -->
        <div class="section">
            <h2>🔧 Code Highlights</h2>
            <pre># Simple and efficient text analysis
if text:
    # Calculate statistics
    words = len(text.split())
    characters = len(text)
    lines = len(text.splitlines())
    
    # Display results in columns
    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Words", words)
    col2.metric("📏 Characters", characters)
    col3.metric("📊 Lines", lines)
    
    # Success message
    st.success(f"✅ Found {words} words and {characters} characters!")
else:
    st.warning("⚠️ Please enter some text first")</pre>
        </div>

        <!-- Project Structure -->
        <div class="section">
            <h2>📁 Project Structure</h2>
            <pre>word-counter-app/
│
├── main.py              # Main Streamlit application
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignore file</pre>
        </div>

        <!-- Requirements -->
        <div class="section">
            <h2>📦 Requirements</h2>
            <p>Create a <code>requirements.txt</code> file:</p>
            <pre>streamlit==1.29.0</pre>
        </div>


        <!-- Future Improvements -->
        <div class="section">
            <h2>🔮 Future Improvements</h2>
            <ul>
                <li>📁 Add text file upload support (.txt, .docx, .pdf)</li>
                <li>⏱️ Show reading time estimation</li>
                <li>🌐 Support multiple languages</li>
                <li>📊 Word frequency analysis</li>
                <li>📈 Character count without spaces</li>
            </ul>
        </div>


        <!-- Author -->
        <div class="section">
            <h2>👨‍💻 Author</h2>
            <p><strong>Haider Ali Shah</strong></p>
            
        </div>

        <!-- License -->
        <div class="section">
            <h2>📜 License</h2>
            <p>This project is licensed under the <strong>MIT License</strong> - see the <a href="#">LICENSE</a> file for details.</p>
            <p>MIT License © 2026 <a href="https://github.com/HaiderNeuralNet">Haider Ali Shah</a></p>
        </div>

      

        <hr>

        <div class="footer">
            <p>Made using Python and Streamlit</p>
            
        </div>
    </div>
</body>
</html>
