import { useEffect, useState } from "react";
import api from "../services/api";

export default function useShipmentEvents(shipmentId) {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!shipmentId) {
      setEvents([]);
      return;
    }

    async function loadEvents() {
      setLoading(true);

      try {
        const response = await api.get(
          `/shipments/${shipmentId}/events`
        );

        setEvents(response.data);
      } catch (error) {
        console.error(error);
        setEvents([]);
      } finally {
        setLoading(false);
      }
    }

    loadEvents();
  }, [shipmentId]);

  return {
    events,
    loading,
  };
}