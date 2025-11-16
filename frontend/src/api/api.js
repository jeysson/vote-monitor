import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export const getLegislatorSummary = async () => {
  const res = await axios.get(`${API_BASE}/legislators/summary`);
  return res.data;
};

export const getBillSummary = async () => {
  const res = await axios.get(`${API_BASE}/bills/summary`);
  return res.data;
};
