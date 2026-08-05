import {
  Box,
  CircularProgress,
  Container,
  Paper,
  Stack,
  Typography,
} from "@mui/material";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import AutorenewIcon from "@mui/icons-material/Autorenew";

export default function DashboardLoading() {
  return (
    <Container
      maxWidth="md"
      sx={{
        height: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Paper
        elevation={4}
        sx={{
          p: 6,
          width: "100%",
          maxWidth: 700,
          borderRadius: 3,
        }}
      >
        <Box
          sx={{
            textAlign: "center",
            mb: 5,
          }}
        >
          <Typography
            variant="h4"
            sx={{
              fontWeight: 700,
              mb: 1,
            }}
          >
            🤖 NovaMed AI Control Tower
          </Typography>

          <Typography
            variant="h6"
            color="text.secondary"
          >
            Initializing operational dashboard...
          </Typography>
        </Box>

        <Stack spacing={2.5}>
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 2,
            }}
          >
            <CheckCircleIcon color="success" />

            <Typography>
              Connecting to DynamoDB
            </Typography>
          </Box>

          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 2,
            }}
          >
            <CheckCircleIcon color="success" />

            <Typography>
              Loading shipment metadata
            </Typography>
          </Box>

          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 2,
            }}
          >
            <AutorenewIcon
              color="primary"
              className="spin"
            />

            <Typography>
              Analyzing shipment risks
            </Typography>
          </Box>

          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 2,
            }}
          >
            <AutorenewIcon
              color="primary"
              className="spin"
            />

            <Typography>
              Building executive summary
            </Typography>
          </Box>
        </Stack>

        <Box
          sx={{
            mt: 6,
            textAlign: "center",
          }}
        >
          <CircularProgress />

          <Typography
            color="text.secondary"
            sx={{
              mt: 2,
            }}
          >
            Loading live supply chain...
          </Typography>
        </Box>

        <style>
          {`
            .spin {
              animation: spin 1.2s linear infinite;
            }

            @keyframes spin {
              from {
                transform: rotate(0deg);
              }
              to {
                transform: rotate(360deg);
              }
            }
          `}
        </style>
      </Paper>
    </Container>
  );
}