import {
  Paper,
  Typography,
  Stack,
  Alert,
  CircularProgress,
  Box,
} from "@mui/material";

export default function AlertPanel({
  alerts,
  loading,
}) {
  return (
    <Paper
      elevation={3}
      sx={{
        p: 3,
        height: "100%",
      }}
    >
      <Typography
        variant="h6"
        gutterBottom
      >
        Operational Alerts
      </Typography>

      {loading ? (
        <Box
          display="flex"
          justifyContent="center"
          py={4}
        >
          <CircularProgress />
        </Box>
      ) : alerts.length === 0 ? (
        <Typography color="text.secondary">
          No active alerts.
        </Typography>
      ) : (
        <Stack spacing={2}>
          {alerts.map((alert, index) => (
            <Alert
              key={index}
              severity={
                alert.severity === "High"
                  ? "error"
                  : "warning"
              }
            >
              <Typography fontWeight={600}>
                {alert.title}
              </Typography>

              <Typography variant="body2">
                {alert.description}
              </Typography>
            </Alert>
          ))}
        </Stack>
      )}
    </Paper>
  );
}