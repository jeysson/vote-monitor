import React, { useEffect, useState } from "react";
import { getBillSummary } from "../api/api";

const BillSummary = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getBillSummary();
      setData(result);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Bills Summary</h2>
      <table border="1" cellPadding="5">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Supporters</th>
            <th>Opposers</th>
            <th>Primary Sponsor</th>
          </tr>
        </thead>
        <tbody>
          {data.map((bill) => (
            <tr key={bill.bill_id}>
              <td>{bill.bill_id}</td>
              <td>{bill.bill_title}</td>
              <td>{bill.supporters}</td>
              <td>{bill.opposers}</td>
              <td>{bill.primary_sponsor}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BillSummary;
