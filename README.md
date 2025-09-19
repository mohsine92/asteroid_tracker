<h1>NEO Watch ⎟ Asteroid Tracker Dashboard</h1>
<img src="https://github.com/user-attachments/assets/2fc1fdf1-7682-4c2f-8742-2ec56b36bb54" width="440"/>

<img src="https://github.com/user-attachments/assets/9b0bc311-42e2-4a98-9182-45003137669d" width="300" />

<h2>Introduction</h2>

<p>This project is not just a simple tracker — it is part of a broader scientific research and data modeling effort. Leveraging NASA’s Near-Earth Object (NEO) datasets, it demonstrates how raw space data can be collected, modeled, and transformed into meaningful insights.

The goal is to explore how data science, visualization, and interactive applications can support space research and help both scientists and the public better understand potential asteroid threats and celestial dynamics.

By integrating real NASA APIs, data exploitation techniques, and interactive visualizations, this project bridges the gap between raw astrophysical data and human interpretation, contributing to the vision of open scientific exploration and collaborative research.</p>

Data provided by NASA Near Earth Object Web Service (NeoWs) (https://api.nasa.gov/).

## Research Methodology

This project follows a scientific approach :

- Define the research question.
- Acquire and preprocess NASA NEO datasets.
- Model asteroid characteristics and potential risks.
- Visualize data for interpretation and accessibility.
- Contribute to research by enabling reproducible and open exploration.

<h2>Features</h2>
<ul>
  <li>Select a date range to retrieve asteroid passes.</li>
  <li>Interactive table with name, estimated diameter, date, and hazardous status.</li>
  <li>Scatter plot visualizing asteroid size by date.</li>
  <li>Automatic alerts for potentially hazardous asteroids.</li>
</ul>

<h2>Technologies</h2>
<ul>
  <li>Python</li>
  <li>Streamlit for the web interface</li>
  <li>Requests for API calls</li>
  <li>Pandas for data manipulation</li>
  <li>Matplotlib for plotting</li>
</ul>

<h2>Installation & Run Locally</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/mohsine92/asteroid_tracker.git
cd asteroid_tracker</code></pre>
  </li>
  <li>Create a virtual environment (optional but recommended):
    <pre><code>python3 -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Add your NASA API key:
    <ul>
      <li>On <strong>Streamlit Cloud</strong>: Settings → Secrets →<br>
      <code>NASA_API_KEY = "your_api_key_here"</code></li>
      <li>Locally: you can also use a <code>.env</code> or set an environment variable <code>NASA_API_KEY</code></li>
    </ul>
  </li>
  <li>Run the app:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

<h2>Project Structure</h2>
<pre><code>asteroid_tracker/
├── app.py
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml  # ignored by git</code></pre>

<h2>Notes</h2>
<ul>
  <li>Never push your API key to GitHub.</li>
  <li>The <code>.streamlit/secrets.toml</code> file is ignored by git.</li>
  <li>Use your personal NASA key instead of the <code>DEMO_KEY</code> for higher API limits.</li>
</ul>

<h2>Optional Enhancements</h2>
<ul>
  <li>Add filtering by asteroid size or hazardous status.</li>
  <li>Include a chart showing the number of asteroids per day.</li>
  <li>Integrate additional NASA datasets for enriched visualization.</li>
</ul>
