import { useEffect, useState } from "react";

import api from "../services/api";

export default function useShipments() {
  const [shipments, setShipments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchShipments() {
      try {
        const response = await api.get("/shipments/");
        setShipments(response.data);
      } catch (err) {
        console.error(err);
        setError("Unable to load shipments.");
      } finally {
        setLoading(false);
      }
    }

    fetchShipments();
  }, []);

  return {
    shipments,
    loading,
    error,
  };
}