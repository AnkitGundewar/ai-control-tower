export function calculateMetrics(shipments) {
  const total = shipments.length;

  const delayed = shipments.filter(
    (shipment) => shipment.status === "Delayed"
  ).length;

  const highRisk = shipments.filter(
    (shipment) => shipment.slaRisk === "High"
  ).length;

  const onTime =
    total === 0
      ? 0
      : Math.round(((total - delayed) / total) * 100);

  return {
    total,
    delayed,
    highRisk,
    onTime,
  };
}