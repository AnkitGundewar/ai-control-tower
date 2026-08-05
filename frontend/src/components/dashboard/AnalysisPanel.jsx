import { useState } from "react";

import {
  Box,
  Button,
  CircularProgress,
  Divider,
  Paper,
  Typography,
} from "@mui/material";

import api from "../../services/api";
import { useShipmentContext } from "../../context/useShipmentContext";

export default function AnalysisPanel() {

  const { selectedShipment } = useShipmentContext();

  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState(null);

  async function analyzeShipment() {

    if (!selectedShipment) {
      return;
    }

    setLoading(true);

    try {

      const response = await api.post(
        "/ai/analyze",
        {
          request_id: crypto.randomUUID(),
          correlation_id: crypto.randomUUID(),
          session_id: crypto.randomUUID(),
          user_role: "operator",
          shipment_ids: [
            selectedShipment.shipmentId,
          ],
          payload: {},
        }
      );

      setAnalysis(
        response.data,
      );

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  }

  return (

    <Paper
      variant="outlined"
      sx={{
        p: 3,
      }}
    >

      <Typography
        variant="h6"
        gutterBottom
      >
        🤖 AI Analysis
      </Typography>

      <Button
        variant="contained"
        onClick={analyzeShipment}
        disabled={
          loading ||
          !selectedShipment
        }
      >
        Analyze Shipment
      </Button>

      {loading && (

        <Box
          sx={{
            mt: 3,
            display: "flex",
            justifyContent: "center",
          }}
        >
          <CircularProgress />
        </Box>

      )}

      {!loading && analysis && (

        <>

          <Divider sx={{ my: 3 }} />

          <Typography
            variant="subtitle2"
            fontWeight="bold"
          >
            Risk
          </Typography>

          <Typography
            paragraph
          >
            {analysis.risk.riskAnalysis.riskLevel}
          </Typography>

          <Typography
            variant="subtitle2"
            fontWeight="bold"
          >
            Root Cause
          </Typography>

          <Typography
            paragraph
          >
            {analysis.rootCause.rootCauseAnalysis.rootCause}
          </Typography>

          <Typography
            variant="subtitle2"
            fontWeight="bold"
          >
            Recommended Action
          </Typography>

          <Typography
            paragraph
          >
            {
              analysis.recommendation
                .recommendation
                .recommendations[0]
            }
          </Typography>

          <Typography
            variant="subtitle2"
            fontWeight="bold"
          >
            Executive Summary
          </Typography>

          <Typography>
            {
              analysis.executiveSummary
                .executiveSummary
                .summary
            }
          </Typography>

        </>

      )}

    </Paper>

  );

}