// App.jsx
import React from "react";
import { Link } from "react-router-dom";
import "./style.css";

export default function App() {
  return (
    <div>
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">Space Debris Detector</div>
        <div className="nav-links">
          <Link to="/upload">Upload Image</Link>
          <Link to="/result">Results</Link>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="hero">
        <div className="hero-content">
          <h1>Space Debris</h1>
          <p>
            Space debris, or “space junk,” is made up of broken satellites, rocket parts,
            and other fragments left behind in Earth's orbit. These objects travel at extremely
            high speeds, and even small pieces can damage active satellites or spacecraft.
            Our system helps detect and analyze this debris, providing vital information
            to protect space missions and keep Earth’s orbit safe.
          </p>
          <Link to="/upload" className="cta-btn">Upload Image</Link>
        </div>
      </header>
    </div>
  );
}









