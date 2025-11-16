import React, { useEffect, useState } from "react";
import { getLegislatorSummary } from "../api/api";

const LegislatorSummary = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getLegislatorSummary();
      setData(result);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Legislators Summary</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Supported Bills</th>
            <th>Opposed Bills</th>
          </tr>
        </thead>
        <tbody>
          {data.map((leg) => (
            <tr key={leg.legislator_id}>
              <td>{leg.legislator_id}</td>
              <td>{leg.legislator_name}</td>
              <td>{leg.supported}</td>
              <td>{leg.opposed}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LegislatorSummary;
