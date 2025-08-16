// Result.jsx
import React from "react";
import { useLocation, Link } from "react-router-dom";
import "./style.css";

export default function Result() {
  const location = useLocation();
  const data = location.state;

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">Space Debris Detector</div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/upload">Upload</Link>
        </div>
      </nav>

      {/* Hero Header (consistent style) */}
      <header className="hero">
        <div className="hero-content">
          <h1>Detection Results</h1>
          <p>
            Below are the detection results from the uploaded image.  
            The model highlights debris with bounding boxes and provides confidence levels.
          </p>
        </div>
      </header>

      {/* Results Section */}
      <div className="results-container">
        {data?.image_url ? (
          <div className="card">
            <img
              src={`http://127.0.0.1:8000${data.image_url}`}
              alt="Detection Result"
              className="result-img"
            />
          </div>
        ) : (
          <p>No result image found. Please upload again.</p>
        )}

        {/* Results Table */}
        {data?.predictions?.length > 0 && (
          <table>
            <thead>
              <tr>
                <th>Label</th>
                <th>Confidence</th>
                <th>Bounding Box</th>
              </tr>
            </thead>
            <tbody>
              {data.predictions.map((p, i) => (
                <tr key={i}>
                  <td>{p.label}</td>
                  <td>{(p.confidence * 100).toFixed(2)}%</td>
                  <td>({p.bbox.join(", ")})</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}

        <Link to="/upload" className="btn back-btn">
          ⬅ Back to Upload
        </Link>
      </div>
    </div>
  );
}


