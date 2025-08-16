import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./style.css";

export default function Upload() {
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      if (!selectedFile.type.startsWith("image/")) {
        setErrorMsg("⚠ Please upload a valid image file.");
        setPreview(null);
        setFile(null);
        return;
      }
      setErrorMsg("");
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    }
  };

  const handleAnalyze = async (e) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Failed to analyze");

      const data = await res.json();
      navigate("/result", { state: data }); // pass backend result
    } catch (err) {
      setErrorMsg("❌ Error analyzing image. Make sure backend is running.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">Space Debris Detector</div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/result">Results</Link>
        </div>
      </nav>

      {/* Hero Header (same style as Home) */}
      <header className="hero">
        <div className="hero-content">
          <h1>Upload Satellite Image</h1>
          <p>
            Upload your satellite image below.  
            Our AI-powered model will analyze it and detect possible space debris,  
            marking them for better visualization.
          </p>
        </div>
      </header>

      {/* Upload Section */}
      <div className="upload-container">
        <h2>Upload Your Image</h2>

        {preview && (
          <div className="preview-box">
            <img src={preview} alt="Preview" />
          </div>
        )}

        {errorMsg && <div className="error-msg">{errorMsg}</div>}

        <form onSubmit={handleAnalyze}>
          <input
            type="file"
            accept="image/*"
            required
            onChange={handleFileChange}
          />
          <button type="submit" className="btn analyze-btn" disabled={loading}>
            {loading ? "Processing..." : "Analyze Image"}
          </button>
        </form>
      </div>
    </div>
  );
}
