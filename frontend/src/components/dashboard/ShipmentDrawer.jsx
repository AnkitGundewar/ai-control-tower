import {
  Box,
  Divider,
  Drawer,
  Paper,
  Stack,
  Typography,
} from "@mui/material";

import StatusChip from "../common/StatusChip";
import { useShipmentContext } from "../../context/useShipmentContext";

export default function ShipmentDrawer() {
  const {
    selectedShipment,
    setSelectedShipment,
  } = useShipmentContext();

  return (
    <Drawer
      anchor="right"
      open={Boolean(selectedShipment)}
      onClose={() => setSelectedShipment(null)}
    >
      <Box
        sx={{
          width: 420,
          height: "100%",
          p: 3,
          overflowY: "auto",
          bgcolor: "background.default",
        }}
      >
        {!selectedShipment ? (
          <Typography>No shipment selected.</Typography>
        ) : (
          <>
            {/* ================================================= */}
            {/* Header */}
            {/* ================================================= */}

            <Typography
              variant="h5"
              fontWeight={600}
            >
              {selectedShipment.shipmentId}
            </Typography>

            <Typography
              variant="body2"
              color="text.secondary"
              sx={{ mt: 0.5 }}
            >
              {selectedShipment.carrier}
            </Typography>

            <Divider sx={{ my: 3 }} />

            {/* ================================================= */}
            {/* Shipment Details */}
            {/* ================================================= */}

            <Stack spacing={2}>
              <Paper
                variant="outlined"
                sx={{ p: 2 }}
              >
                <Typography
                  variant="subtitle2"
                  color="text.secondary"
                >
                  Origin
                </Typography>

                <Typography variant="body1">
                  {selectedShipment.origin}
                </Typography>
              </Paper>

              <Paper
                variant="outlined"
                sx={{ p: 2 }}
              >
                <Typography
                  variant="subtitle2"
                  color="text.secondary"
                >
                  Destination
                </Typography>

                <Typography variant="body1">
                  {selectedShipment.destination}
                </Typography>
              </Paper>

              <Paper
                variant="outlined"
                sx={{ p: 2 }}
              >
                <Typography
                  variant="subtitle2"
                  color="text.secondary"
                >
                  ETA
                </Typography>

                <Typography variant="body1">
                  {selectedShipment.eta}
                </Typography>
              </Paper>

              <Paper
                variant="outlined"
                sx={{ p: 2 }}
              >
                <Typography
                  variant="subtitle2"
                  color="text.secondary"
                  gutterBottom
                >
                  Status
                </Typography>

                <StatusChip
                  status={selectedShipment.status}
                />
              </Paper>

              <Paper
                variant="outlined"
                sx={{ p: 2 }}
              >
                <Typography
                  variant="subtitle2"
                  color="text.secondary"
                >
                  SLA Risk
                </Typography>

                <Typography
                  variant="body1"
                  fontWeight={600}
                >
                  {selectedShipment.slaRisk}
                </Typography>
              </Paper>
            </Stack>

            <Divider sx={{ my: 4 }} />

            {/* ================================================= */}
            {/* AI Analysis */}
            {/* ================================================= */}

            <Typography
              variant="h6"
              gutterBottom
            >
              AI Analysis
            </Typography>

            <Paper
              variant="outlined"
              sx={{ p: 2 }}
            >
              <Typography color="text.secondary">
                AI insights will appear here once the
                Tracking Agent and Risk Agent are connected.
              </Typography>
            </Paper>

            <Divider sx={{ my: 4 }} />

            {/* ================================================= */}
            {/* Recommendations */}
            {/* ================================================= */}

            <Typography
              variant="h6"
              gutterBottom
            >
              Recommended Actions
            </Typography>

            <Paper
              variant="outlined"
              sx={{ p: 2 }}
            >
              <Typography color="text.secondary">
                Recommendations will appear here after
                AI analysis is complete.
              </Typography>
            </Paper>
          </>
        )}
      </Box>
    </Drawer>
  );
}