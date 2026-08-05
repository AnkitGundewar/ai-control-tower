import { useEffect, useState } from "react";
import api from "../services/api";

export default function useShipmentEvents(
  shipmentId,
) {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!shipmentId) {
      return;
    }

    let cancelled = false;

    async function loadEvents() {
      setLoading(true);

      try {
        const response = await api.get(
          `/shipments/${shipmentId}/context`
        );

        if (!cancelled) {
          setEvents(
            response.data.events ?? []
          );
        }
      } catch (error) {
        console.error(error);

        if (!cancelled) {
          setEvents([]);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadEvents();

    return () => {
      cancelled = true;
    };
  }, [shipmentId]);

  return {
    events,
    loading,
  };
}