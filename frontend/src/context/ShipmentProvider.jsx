import { useState } from "react";
import { ShipmentContext } from "./ShipmentContext";

export default function ShipmentProvider({ children }) {
  const [selectedShipment, setSelectedShipment] = useState(null);

  const [searchQuery, setSearchQuery] = useState("");

  const value = {
    selectedShipment,
    setSelectedShipment,

    searchQuery,
    setSearchQuery,
  };

  return (
    <ShipmentContext.Provider value={value}>
      {children}
    </ShipmentContext.Provider>
  );
}