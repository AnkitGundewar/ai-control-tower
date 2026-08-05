import {
  Paper,
  Typography,
  CircularProgress,
  Box,
  Divider,
} from "@mui/material";

export default function ExecutiveSummary({
  summary,
  loading,
}) {
  return (
    <Paper
      elevation={3}
      sx={{
        p: 3,
        minHeight: 220,
        display: "flex",
        flexDirection: "column",
      }}
    >
      <Typography
        variant="h6"
        fontWeight={600}
      >
        📈 Executive Summary
      </Typography>

      <Typography
        variant="caption"
        color="text.secondary"
        sx={{
          mt: 0.5,
        }}
      >
        AI-generated operational overview
      </Typography>

      <Divider
        sx={{
          my: 1,
        }}
      />

      {loading ? (
        <Box
          sx={{
            flex: 1,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <CircularProgress />
        </Box>
      ) : (
        <Typography
          variant="body2"
          sx={{
            color: "text.primary",
            lineHeight: 1.5,
            whiteSpace: "pre-line",
          }}
        >
          {summary}
        </Typography>
      )}
    </Paper>
  );
}