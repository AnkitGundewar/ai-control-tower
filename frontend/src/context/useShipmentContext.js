import { useContext } from "react";
import { ShipmentContext } from "./ShipmentContext";

export function useShipmentContext() {
  return useContext(ShipmentContext);
}