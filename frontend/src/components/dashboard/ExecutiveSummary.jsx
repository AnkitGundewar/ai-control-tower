import {
  Paper,
  Typography,
  CircularProgress,
  Box,
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
        height: 200,
      }}
    >
      <Typography
        variant="h6"
        gutterBottom
      >
        Executive Summary
      </Typography>

      {loading ? (
        <Box
          display="flex"
          justifyContent="center"
          py={4}
        >
          <CircularProgress />
        </Box>
      ) : (
        <Typography
          color="text.secondary"
          lineHeight={1.8}
        >
          {summary}
        </Typography>
      )}
    </Paper>
  );
}