import React from "react";

export default function ResultCard({ label, score }) {
  const isPositive = label && label.toLowerCase().includes("pos");
  const color = isPositive ? "#2e7d32" : "#c62828";

  return (
    <div style={{ border: `2px solid ${color}`, padding: 12, borderRadius: 6, width: 380 }}>
      <h3 style={{ color }}>{label}</h3>
      <p>Confidence: {(score * 100).toFixed(2)}%</p>
      <p style={{ fontSize: 13, color: "#444" }}>
        {isPositive ? "This text expresses a positive sentiment." : "This text expresses a negative sentiment."}
      </p>
    </div>
  );
}
