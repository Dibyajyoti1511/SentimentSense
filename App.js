import React from "react";
import SentimentForm from "./components/SentimentForm";

function App() {
  return (
    <div style={{fontFamily: "Arial, sans-serif", padding: 20, maxWidth: 900, margin: "auto"}}>
      <h1>SentimentSense</h1>
      <p>Enter text below to analyze sentiment (Positive / Negative) — powered by Transformers.</p>
      <SentimentForm />
    </div>
  );
}

export default App;
