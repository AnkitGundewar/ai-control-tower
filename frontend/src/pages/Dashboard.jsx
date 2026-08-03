import {
  Box,
  Container,
  Grid,
} from "@mui/material";

import useShipments from "../hooks/useShipments";
import { calculateMetrics } from "../utils/dashboardMetrics";

import Header from "../components/layout/Header";

import KPICard from "../components/dashboard/KPICard";
import SearchBar from "../components/dashboard/SearchBar";
import ShipmentGrid from "../components/dashboard/ShipmentGrid";
import ShipmentDrawer from "../components/dashboard/ShipmentDrawer";
import AlertPanel from "../components/dashboard/AlertPanel";
import ExecutiveSummary from "../components/dashboard/ExecutiveSummary";

import ChatPanel from "../components/chat/ChatPanel";

export default function Dashboard() {
  const {
    shipments,
    loading,
    error,
  } = useShipments();

  const metrics = calculateMetrics(shipments);

  if (loading) {
    return <div>Loading shipments...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <>
      <Header />

      <Container
        maxWidth="xl"
        sx={{
          mt: 4,
          mb: 4,
        }}
      >
        {/* ========================= KPI CARDS ========================= */}

        <Grid container spacing={3}>
          <Grid size={{ xs: 12, md: 3 }}>
            <KPICard
              title="Total Shipments"
              value={metrics.total}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 3 }}>
            <KPICard
              title="Delayed"
              value={metrics.delayed}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 3 }}>
            <KPICard
              title="High Risk"
              value={metrics.highRisk}
            />
          </Grid>

          <Grid size={{ xs: 12, md: 3 }}>
            <KPICard
              title="On Time"
              value={`${metrics.onTime}%`}
            />
          </Grid>
        </Grid>

        {/* ========================= SEARCH ========================= */}

        <Box mt={4}>
          <SearchBar />
        </Box>

        {/* ========================= SHIPMENT GRID ========================= */}

        <Box mt={4}>
          <ShipmentGrid
            shipments={shipments}
            loading={loading}
          />
        </Box>

        {/* ========================= ALERTS + SUMMARY ========================= */}

        <Grid
          container
          spacing={3}
          mt={1}
        >
          <Grid size={{ xs: 12, md: 6 }}>
            <AlertPanel />
          </Grid>

          <Grid size={{ xs: 12, md: 6 }}>
            <ExecutiveSummary />
          </Grid>
        </Grid>

        {/* ========================= CHAT ========================= */}

        <Box mt={4}>
          <ChatPanel />
        </Box>

        {/* ========================= SHIPMENT DRAWER ========================= */}

        <ShipmentDrawer />
      </Container>
    </>
  );
}