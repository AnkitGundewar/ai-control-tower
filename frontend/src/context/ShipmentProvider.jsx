import { useState } from "react";
import { ShipmentContext } from "./ShipmentContext";

export default function ShipmentProvider({ children }) {
  const [selectedShipment, setSelectedShipment] = useState(null);

  return (
    <ShipmentContext.Provider
      value={{
        selectedShipment,
        setSelectedShipment,
      }}
    >
      {children}
    </ShipmentContext.Provider>
  );
}