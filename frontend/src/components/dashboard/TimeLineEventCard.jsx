import {
  Paper,
  Typography,
  Stack,
} from "@mui/material";

export default function TimelineEventCard({ event }) {
  return (
    <Paper
      variant="outlined"
      sx={{
        p: 2,
        mb: 2,
      }}
    >
      <Typography
        variant="subtitle1"
        fontWeight={600}
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
        sx={{ mt: 1 }}
      >
        {event.details}
      </Typography>

      <Typography
        variant="caption"
        color="text.secondary"
        sx={{
          mt: 1,
          display: "block",
        }}
      >
        {new Date(event.timestamp).toLocaleString()}
      </Typography>
    </Paper>
  );
}