import {
  Drawer,
  Box,
  Typography,
  Divider,
  Stack,
} from "@mui/material";

import {
  Timeline,
  TimelineItem,
  TimelineSeparator,
  TimelineDot,
  TimelineConnector,
  TimelineContent,
} from "@mui/lab";

import StatusChip from "../common/StatusChip";
import { useShipmentContext } from "../../context/useShipmentContext";
import useShipmentEvents from "../../hooks/useShipmentEvents";

export default function ShipmentDrawer() {
  const {
    selectedShipment,
    setSelectedShipment,
  } = useShipmentContext();

  const {
    events,
    loading,
  } = useShipmentEvents(
    selectedShipment?.shipmentId
  );

  return (
    <Drawer
      anchor="right"
      open={Boolean(selectedShipment)}
      onClose={() => setSelectedShipment(null)}
    >
      <Box
        sx={{
          width: 450,
          p: 3,
        }}
      >
        {!selectedShipment ? (
          <Typography>
            No shipment selected.
          </Typography>
        ) : (
          <>
            <Typography
              variant="h5"
              gutterBottom
            >
              {selectedShipment.shipmentId}
            </Typography>

            <Divider sx={{ mb: 3 }} />

            <Stack spacing={2}>

              <Box>
                <Typography variant="subtitle2">
                  Origin
                </Typography>

                <Typography>
                  {selectedShipment.origin}
                </Typography>
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  Destination
                </Typography>

                <Typography>
                  {selectedShipment.destination}
                </Typography>
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  Carrier
                </Typography>

                <Typography>
                  {selectedShipment.carrier}
                </Typography>
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  Current Location
                </Typography>

                <Typography>
                  {selectedShipment.currentLocation}
                </Typography>
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  ETA
                </Typography>

                <Typography>
                  {selectedShipment.eta}
                </Typography>
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  SLA Deadline
                </Typography>

                <Typography>
                  {selectedShipment.slaDeadline}
                </Typography>
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  Status
                </Typography>

                <StatusChip
                  status={selectedShipment.status}
                />
              </Box>

              <Box>
                <Typography variant="subtitle2">
                  SLA Risk
                </Typography>

                <StatusChip
                  status={selectedShipment.slaRisk}
                />
              </Box>

            </Stack>

            <Divider sx={{ my: 4 }} />

            <Typography
              variant="h6"
              gutterBottom
            >
              Shipment Timeline
            </Typography>

            {loading ? (
              <Typography>
                Loading timeline...
              </Typography>
            ) : (
              <Timeline position="right">

                {events.map((event, index) => (
                  <TimelineItem key={index}>

                    <TimelineSeparator>

                      <TimelineDot />

                      {index !== events.length - 1 && (
                        <TimelineConnector />
                      )}

                    </TimelineSeparator>

                    <TimelineContent>

                      <Typography
                        variant="subtitle2"
                      >
                        {event.eventType}
                      </Typography>

                      <Typography
                        variant="body2"
                        color="text.secondary"
                      >
                        {event.location}
                      </Typography>

                      <Typography
                        variant="body2"
                      >
                        {event.details}
                      </Typography>

                    </TimelineContent>

                  </TimelineItem>
                ))}

              </Timeline>
            )}

          </>
        )}
      </Box>
    </Drawer>
  );
}