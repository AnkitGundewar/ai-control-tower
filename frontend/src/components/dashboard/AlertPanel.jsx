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
        height: 540,
        display: "flex",
        flexDirection: "column",
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
          alignItems="center"
          flex={1}
        >
          <CircularProgress />
        </Box>
      ) : alerts.length === 0 ? (
        <Typography color="text.secondary">
          No active alerts.
        </Typography>
      ) : (
        <Box
          sx={{
            flex: 1,
            overflowY: "auto",
            pr: 1,

            "&::-webkit-scrollbar": {
              width: 8,
            },

            "&::-webkit-scrollbar-thumb": {
              backgroundColor: "#c7c7c7",
              borderRadius: 4,
            },

            "&::-webkit-scrollbar-track": {
              backgroundColor: "transparent",
            },
          }}
        >
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
        </Box>
      )}
    </Paper>
  );
}