import React from "react";
import LegislatorSummary from "./components/LegislatorSummary";
import BillSummary from "./components/BillSummary";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>Vote Monitor</h1>
      <LegislatorSummary />
      <hr />
      <BillSummary />
    </div>
  );
}

export default App;
