import { Paper } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";

import StatusChip from "../common/StatusChip";
import { useShipmentContext } from "../../context/useShipmentContext";

export default function ShipmentGrid({
  shipments,
  loading,
}) {
  const { setSelectedShipment } = useShipmentContext();

  const columns = [
    {
      field: "shipmentId",
      headerName: "Shipment ID",
      flex: 1.2,
    },
    {
      field: "origin",
      headerName: "Origin",
      flex: 1,
    },
    {
      field: "destination",
      headerName: "Destination",
      flex: 1,
    },
    {
      field: "carrier",
      headerName: "Carrier",
      flex: 1,
    },
    {
      field: "status",
      headerName: "Status",
      flex: 1,
      renderCell: (params) => (
        <StatusChip status={params.value} />
      ),
    },    
  ];

  const rows = shipments.map((shipment) => ({
    id: shipment.shipmentId,
    ...shipment,
  }));

  return (
    <Paper
      elevation={3}
      sx={{
        height: 500,
        width: "100%",
      }}
    >
      <DataGrid
        rows={rows}
        columns={columns}
        loading={loading}
        pageSizeOptions={[5, 10, 20]}
        initialState={{
          pagination: {
            paginationModel: {
              page: 0,
              pageSize: 10,
            },
          },
        }}
        disableRowSelectionOnClick
        onRowClick={(params) => {
          setSelectedShipment(params.row);
        }}
      />
    </Paper>
  );
}