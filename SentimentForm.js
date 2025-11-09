import React, { useState } from "react";
import axios from "axios";
import ResultCard from "./ResultCard";

export default function SentimentForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    if (!text.trim()) return alert("Please enter text.");
    setLoading(true);
    setResult(null);
    try {
      const res = await axios.post("http://localhost:5000/predict", { text });
      setResult(res.data);
    } catch (err) {
      alert("Error: " + (err.response?.data?.error || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea
        rows="6"
        cols="80"
        placeholder="Type or paste text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{ padding: 8, fontSize: 14 }}
      ></textarea>
      <div style={{ marginTop: 10 }}>
        <button onClick={analyze} disabled={loading} style={{ padding: "8px 16px" }}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </div>

      <div style={{ marginTop: 20 }}>
        {result && <ResultCard label={result.label} score={result.score} />}
      </div>
    </div>
  );
}
