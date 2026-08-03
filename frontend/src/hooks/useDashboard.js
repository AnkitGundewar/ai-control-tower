import { useEffect, useState } from "react";
import api from "../services/api";

export default function useDashboard() {
  const [summary, setSummary] = useState("");
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [summaryResponse, alertsResponse] = await Promise.all([
          api.get("/dashboard/summary"),
          api.get("/dashboard/alerts"),
        ]);

        setSummary(summaryResponse.data.summary);
        setAlerts(alertsResponse.data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  return {
    summary,
    alerts,
    loading,
  };
}